# Huấn luyện mô hình

## Notebook chính

**`train_phobert_model.ipynb`** — pipeline train + đánh giá thực nghiệm (PhoBERT text-only + MLP).

## Module backend dùng chung

| File | Vai trò |
|------|---------|
| `text_utils.py` | Tiền xử lý chung train + inference (`preprocess_text`) |
| `dataset_cleaner.py` | Lọc CSV trước train |
| `text_cleaner.py` | Wrapper tương thích; `pipeline_clean` gọi `preprocess_text` |
| `phobert_inference.py` | Suy luận PhoBERT + MLP + giải thích |
| `verdict.py` | Phân loại 3 mức (tin thật / đáng ngờ / tin giả) |

## Chạy suy luận thử

```bash
python -m backend.phobert_inference
```

## Artifact sau khi train (ghi vào `backend/models/`)

| File | Mô tả |
|------|--------|
| `phobert_mlp_model.joblib` | MLP + hyperparameter đã chọn |
| `phobert_scaler.joblib` | Scaler fit trên tập train |
| `phobert_base_features.npy` | Ma trận embedding 768-d (cache) |
| `phobert_base_labels.npy` | Vector nhãn 0/1 |

Các file trên được track trong Git để clone repo có thể chạy inference ngay. Pipeline cũ `hybrid_*.joblib` không còn dùng.
