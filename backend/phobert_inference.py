import torch
import numpy as np
from pathlib import Path
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from backend.data_crawler import DataCrawler
from backend.explanation_engine import build_explanation
from backend.text_utils import preprocess_text
from backend.verdict import result_label_from_verdict, verdict_from_prob

PROJECT_DIR = Path(__file__).resolve().parent.parent


class PhoBERTInferenceSystem:
    """
    Hệ thống phát hiện tin giả: PhoBERTForSequenceClassification.
    """

    def __init__(
        self,
        model_path=None,
        verbose=True,
    ):
        self.crawler = DataCrawler()
        self.verbose = verbose

        model_path = model_path or PROJECT_DIR / "backend/models/phobert-fakenews-final"
        
        if self.verbose:
            print("[*] Khởi tạo Hệ thống AI...")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        model_path_obj = Path(model_path)
        if model_path_obj.exists():
            self.tokenizer = AutoTokenizer.from_pretrained(str(model_path_obj))
            self.phobert_model = AutoModelForSequenceClassification.from_pretrained(str(model_path_obj)).to(self.device)
            self.phobert_model.eval()
            self.model_loaded = True
        else:
            if self.verbose:
                print(f"CẢNH BÁO: Không tìm thấy thư mục mô hình tại {model_path}")
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
        """Trích xuất logits từ PhoBERT model đã fine-tune."""
        if self.verbose:
            print("--- MODULE 2: Dự đoán với PhoBERT ---")

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
            logits = outputs.logits.cpu().numpy()[0]

        if self.verbose:
            print(f" > PhoBERT logits: {logits}")
        return logits

    def module_3_classification(self, logits):
        """Tính xác suất, phân loại và trả về xác suất + nhãn 3 mức."""
        if self.verbose:
            print("--- MODULE 3: Phân loại ---")
            
        exp_logits = np.exp(logits - np.max(logits))
        probs = exp_logits / exp_logits.sum(axis=-1)
        
        fake_prob = float(probs[1] * 100.0)
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
                "message": "Chưa tìm thấy mô hình đã train. Hãy chạy notebook train trước.",
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

        logits = self.module_2_phobert_embedding(clean_content)
        result, fake_prob, verdict = self.module_3_classification(logits)

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
            "phobert_shape": logits.shape,
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
