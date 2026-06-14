import torch
import numpy as np
import joblib
from pathlib import Path
from transformers import AutoModel, AutoTokenizer
from backend.data_crawler import DataCrawler
from backend.explanation_engine import build_explanation
from backend.feature_extraction import build_meta_vector
from backend.text_cleaner import TextCleaner

PROJECT_DIR = Path(__file__).resolve().parent.parent

class HybridInferenceSystem:
    """
    3.3. Thiết kế Hệ thống Phát hiện Tin giả (System Architecture)
    Hệ thống được chia làm 4 module chính hoạt động liên hoàn.
    """
    def __init__(
        self,
        model_path=None,
        scaler_path=None,
        meta_scaler_path=None,
        verbose=True,
    ):
        self.crawler = DataCrawler()
        self.cleaner = TextCleaner()
        self.verbose = verbose

        model_path = model_path or PROJECT_DIR / "backend/models/hybrid_mlp_model.joblib"
        scaler_path = scaler_path or PROJECT_DIR / "backend/models/hybrid_scaler.joblib"
        meta_scaler_path = meta_scaler_path or PROJECT_DIR / "backend/models/hybrid_scaler_meta.joblib"

        if self.verbose:
            print("[*] Khởi tạo Hệ thống AI...")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
        self.phobert_model = AutoModel.from_pretrained("vinai/phobert-base").to(self.device)
        self.phobert_model.eval()

        paths = [Path(model_path), Path(scaler_path), Path(meta_scaler_path)]
        if all(p.exists() for p in paths):
            self.classifier = joblib.load(paths[0])
            self.scaler = joblib.load(paths[1])
            self.scaler_meta = joblib.load(paths[2])
            self.model_loaded = True
        else:
            missing = [p.name for p in paths if not p.exists()]
            if self.verbose:
                print(f"CẢNH BÁO: Thiếu file mô hình: {', '.join(missing)}")
            self.model_loaded = False

    def module_1_data_acquisition_and_preprocessing(
        self, url=None, article_text=None, article_title=None, facebook_text=None, facebook_meta=None
    ):
        """
        3.3.1. Module 1: Thu thập và Tiền xử lý (Data Acquisition)
        - URL: crawler báo điện tử
        - Văn bản: người dùng dán trực tiếp
        """
        if self.verbose:
            print("\n--- MODULE 1: Thu thập Dữ Liệu và Tiền xử lý ---")
        meta = facebook_meta or {}
        text_input = article_text or facebook_text

        if url:
            raw_data = self.crawler.crawl_news_article(url)
            raw_data["metadata"] = meta
        elif text_input:
            raw_data = self.crawler.get_article_from_text(text_input, title=article_title or "", author_metadata=meta)
        else:
            raise ValueError("Phải cung cấp url hoặc article_text")

        if raw_data["status"] == "error":
            if self.verbose:
                print("Lỗi khi tải dữ liệu:", raw_data["message"])
            return None, raw_data

        content = raw_data.get("content", "")
        if len(str(content).split()) < 5:
            return None, {
                "status": "error",
                "message": "Nội dung quá ngắn hoặc crawler không trích xuất được bài báo. Hãy thử nhập văn bản thủ công.",
            }

        clean_content = self.cleaner.pipeline_clean(content)
        if self.verbose:
            print(" > Đã làm sạch văn bản.")
        return clean_content, raw_data

    def module_2_parallel_feature_extraction(self, clean_content, raw_data):
        """
        3.3.2. Module 2: Trích xuất đặc trưng song song
        - Nhánh 1 (Deep Learning): PhoBERT -> Contextual Embedding
        - Nhánh 2 (Statistical): Đặc trưng thống kê + User metadata
        """
        print("--- MODULE 2: Trích xuất đặc trưng song song ---")
        
        # Nhánh 1: PhoBERT
        with torch.no_grad():
            encoded = self.tokenizer(clean_content, padding=True, truncation=True, max_length=256, return_tensors="pt")
            input_ids = encoded['input_ids'].to(self.device)
            attention_mask = encoded['attention_mask'].to(self.device)
            
            outputs = self.phobert_model(input_ids, attention_mask=attention_mask)
            phobert_vector = outputs.last_hidden_state[:, 0, :].cpu().numpy()[0]
            
        # Nhánh 2: Statistical
        title = raw_data.get("title", "")
        content = raw_data.get("content", "")
        meta_vector = build_meta_vector(title, content, raw_data.get("metadata", {}))
        
        print(f" > Nhánh 1 (Deep Learning) - Contextual Embedding : {phobert_vector.shape}")
        print(f" > Nhánh 2 (Statistical) - Metadata Vector        : {meta_vector.shape}")
        
        return phobert_vector, meta_vector

    def module_3_feature_fusion(self, phobert_vector, meta_vector):
        """
        3.3.3. Module 3: Tầng hợp nhất (Feature Fusion Layer)
        - Dùng Concatenation nối 2 vector
        """
        print("--- MODULE 3: Tầng hợp nhất (Feature Fusion Layer) ---")
        
        # Sửa lỗi: Cần chuẩn hóa meta_vector bằng scaler_meta (như trong lúc train) trước khi nối
        if self.model_loaded:
            meta_vector_scaled = self.scaler_meta.transform(meta_vector.reshape(1, -1))[0]
        else:
            meta_vector_scaled = meta_vector
            
        combined_vector = np.hstack((phobert_vector, meta_vector_scaled)).reshape(1, -1)
        print(f" > Nối (Concatenation): {phobert_vector.shape[0]} + {meta_vector_scaled.shape[0]} = {combined_vector.shape[1]} features")
        return combined_vector

    def module_4_classification_and_output(self, combined_vector):
        """
        3.3.4. Module 4: Phân loại và Cảnh báo (Classification & Output)
        - Đưa qua Fully Connected Layer (MLP)
        - Hàm Softmax đưa ra xác suất
        """
        print("--- MODULE 4: Phân loại và Cảnh báo (Classification & Output) ---")
        scaled_vector = self.scaler.transform(combined_vector)
        prediction = self.classifier.predict(scaled_vector)
        confidence = self.classifier.predict_proba(scaled_vector)
        
        try:
            class_index = list(self.classifier.classes_).index(True)
        except ValueError:
            class_index = 1
            
        # Áp dụng Softmax ẩn (predict_proba của MLP dùng Softmax layer cho phân loại đa lớp)
        fake_prob = confidence[0][class_index] * 100.0
        
        result = "TIN GIẢ (FAKE)" if prediction[0] in [1, True] else "TIN THẬT (REAL)"
        print(f">> GHI NHẬN TỪ HỆ THỐNG: {result} (Xác suất qua Softmax: {fake_prob:.2f}%)")
        return result, fake_prob

    def infer(
        self,
        url=None,
        article_text=None,
        article_title=None,
        facebook_text=None,
        facebook_meta=None,
    ):
        """Điều phối 4 module: thu thập → đặc trưng → fusion → phân loại."""
        if not self.model_loaded:
            return {"status": "error", "message": "Chưa tìm thấy mô hình đã train (.joblib). Hãy chạy notebook train trước."}

        clean_content, raw_data = self.module_1_data_acquisition_and_preprocessing(
            url=url,
            article_text=article_text,
            article_title=article_title,
            facebook_text=facebook_text,
            facebook_meta=facebook_meta,
        )
        if clean_content is None:
            return {"status": "error", "message": raw_data.get("message", "Không xử lý được dữ liệu đầu vào.")}

        # Module 2
        phobert_vector, meta_vector = self.module_2_parallel_feature_extraction(clean_content, raw_data)

        # Module 3
        combined_vector = self.module_3_feature_fusion(phobert_vector, meta_vector)

        result, fake_prob = self.module_4_classification_and_output(combined_vector)

        fb_meta = raw_data.get("metadata", facebook_meta or {})
        explanation = build_explanation(
            fake_prob=fake_prob,
            raw_data=raw_data,
            meta=fb_meta,
            meta_vector=meta_vector.tolist(),
        )

        return {
            "status": "success",
            "result": result,
            "fake_prob": fake_prob,
            "raw_data": raw_data,
            "cleaned_text": clean_content,
            "meta_vector": meta_vector.tolist(),
            "phobert_shape": phobert_vector.shape,
            "combined_shape": combined_vector.shape,
            "explanation": explanation,
        }

# Kịch bản Test thử toàn bộ Hybrid Pipeline
if __name__ == "__main__":
    print("========== KHỞI ĐỘNG HỆ THỐNG HYBRID INFERENCE ==========")
    system = HybridInferenceSystem()
    
    fb_text = "Hàng ngàn người đang hoảng loạn tháo chạy vì vụ cháy quá lớn!!!!! Tin cực hot mọi người ơi chia sẻ gấp!!!!"
    fb_meta = {
        'account_age_days': 2.0,     
        'followers': 10.0,           
        'is_verified': 0.0,          
        'share_speed': 65.0,         
        'angry_ratio': 0.8           
    }
    
    print("\n\n[TEST CASE]")
    system.infer(facebook_text=fb_text, facebook_meta=fb_meta)
