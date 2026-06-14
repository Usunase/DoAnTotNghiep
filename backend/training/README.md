# Huấn luyện mô hình

## Notebook chính

**`train_hybrid_model.ipynb`** — pipeline train + đánh giá thực nghiệm.

## Module backend dùng chung

| File | Vai trò |
|------|---------|
| `text_utils.py` | Xóa URL/HTML, tách từ PyVi (train) |
| `feature_extraction.py` | Metadata mô phỏng + thống kê văn bản |
| `dataset_cleaner.py` | Lọc CSV trước train |
| `text_cleaner.py` | Làm sạch 1 bài lúc inference |
| `hybrid_inference.py` | Suy luận + giải thích |
