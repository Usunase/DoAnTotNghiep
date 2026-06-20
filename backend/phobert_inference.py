import torch
import numpy as np
import joblib
from pathlib import Path
from transformers import AutoModel, AutoTokenizer
from backend.data_crawler import DataCrawler
from backend.explanation_engine import build_explanation
from backend.text_utils import preprocess_text
from backend.verdict import result_label_from_verdict, verdict_from_prob

PROJECT_DIR = Path(__file__).resolve().parent.parent


class PhoBERTInferenceSystem:
    """
    Hệ thống phát hiện tin giả: PhoBERT embedding + MLP classifier.
    """

    def __init__(
        self,
        model_path=None,
        scaler_path=None,
        verbose=True,
    ):
        self.crawler = DataCrawler()
        self.verbose = verbose

        model_path = model_path or PROJECT_DIR / "backend/models/phobert_mlp_model.joblib"
        scaler_path = scaler_path or PROJECT_DIR / "backend/models/phobert_scaler.joblib"

        if self.verbose:
            print("[*] Khởi tạo Hệ thống AI...")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
        self.phobert_model = AutoModel.from_pretrained("vinai/phobert-base").to(self.device)
        self.phobert_model.eval()

        paths = [Path(model_path), Path(scaler_path)]
        if all(p.exists() for p in paths):
            self.classifier = joblib.load(paths[0])
            self.scaler = joblib.load(paths[1])
            self.model_loaded = True
        else:
            missing = [p.name for p in paths if not p.exists()]
            if self.verbose:
                print(f"CẢNH BÁO: Thiếu file mô hình: {', '.join(missing)}")
            self.model_loaded = False

    def module_1_data_acquisition_and_preprocessing(
        self, url=None, article_text=None, article_title=None, facebook_text=None
    ):
        """Thu thập và tiền xử lý dữ liệu đầu vào."""
        if self.verbose:
            print("\n--- MODULE 1: Thu thập Dữ Liệu và Tiền xử lý ---")
        text_input = article_text or facebook_text

        if url:
            raw_data = self.crawler.crawl_news_article(url)
        elif text_input:
            raw_data = self.crawler.get_article_from_text(
                text_input, title=article_title or ""
            )
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

        clean_content = preprocess_text(content)
        if not clean_content:
            return None, {
                "status": "error",
                "message": "Không trích xuất được nội dung hợp lệ sau tiền xử lý.",
            }
        if self.verbose:
            print(" > Đã làm sạch văn bản.")
        return clean_content, raw_data

    def module_2_phobert_embedding(self, clean_content):
        """Trích xuất embedding PhoBERT (768 chiều)."""
        if self.verbose:
            print("--- MODULE 2: Trích xuất đặc trưng PhoBERT ---")

        with torch.no_grad():
            encoded = self.tokenizer(
                clean_content,
                padding=True,
                truncation=True,
                max_length=256,
                return_tensors="pt",
            )
            input_ids = encoded["input_ids"].to(self.device)
            attention_mask = encoded["attention_mask"].to(self.device)

            outputs = self.phobert_model(input_ids, attention_mask=attention_mask)
            phobert_vector = outputs.last_hidden_state[:, 0, :].cpu().numpy()[0]

        if self.verbose:
            print(f" > PhoBERT embedding: {phobert_vector.shape}")
        return phobert_vector

    def module_3_classification(self, phobert_vector):
        """Chuẩn hóa, phân loại và trả về xác suất + nhãn 3 mức."""
        if self.verbose:
            print("--- MODULE 3: Phân loại (MLP) ---")
        feature_vector = phobert_vector.reshape(1, -1)
        scaled_vector = self.scaler.transform(feature_vector)
        confidence = self.classifier.predict_proba(scaled_vector)

        try:
            class_index = list(self.classifier.classes_).index(True)
        except ValueError:
            class_index = 1

        fake_prob = float(confidence[0][class_index] * 100.0)
        verdict = verdict_from_prob(fake_prob)
        result = result_label_from_verdict(verdict)

        if self.verbose:
            print(f">> GHI NHẬN TỪ HỆ THỐNG: {result} (Xác suất: {fake_prob:.2f}%)")
        return result, fake_prob, verdict

    def infer(
        self,
        url=None,
        article_text=None,
        article_title=None,
        facebook_text=None,
    ):
        """Điều phối pipeline: thu thập → PhoBERT → phân loại."""
        if not self.model_loaded:
            return {
                "status": "error",
                "message": "Chưa tìm thấy mô hình đã train (.joblib). Hãy chạy notebook train trước.",
            }

        clean_content, raw_data = self.module_1_data_acquisition_and_preprocessing(
            url=url,
            article_text=article_text,
            article_title=article_title,
            facebook_text=facebook_text,
        )
        if clean_content is None:
            return {
                "status": "error",
                "message": raw_data.get("message", "Không xử lý được dữ liệu đầu vào."),
            }

        phobert_vector = self.module_2_phobert_embedding(clean_content)
        result, fake_prob, verdict = self.module_3_classification(phobert_vector)

        explanation = build_explanation(
            fake_prob=fake_prob,
            raw_data=raw_data,
        )

        return {
            "status": "success",
            "result": result,
            "verdict": verdict,
            "fake_prob": fake_prob,
            "raw_data": raw_data,
            "cleaned_text": clean_content,
            "phobert_shape": phobert_vector.shape,
            "explanation": explanation,
        }


if __name__ == "__main__":
    print("========== KHỞI ĐỘNG HỆ THỐNG INFERENCE ==========")
    system = PhoBERTInferenceSystem()

    fb_text = (
        "Hàng ngàn người đang hoảng loạn tháo chạy vì vụ cháy quá lớn!!!!! "
        "Tin cực hot mọi người ơi chia sẻ gấp!!!!"
    )

    print("\n\n[TEST CASE]")
    system.infer(facebook_text=fb_text)
