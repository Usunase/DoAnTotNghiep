# Lý do lựa chọn phương án — Dự án ShieldAI

Tài liệu giải thích **các quyết định thiết kế** trong đồ án phát hiện tin giả tiếng Việt (phiên bản **PhoBERT text-only**), phù hợp Chương phương pháp / thiết kế trong luận văn.

---

## 1. Bài toán và hướng tiếp cận

**Bài toán:** Phân loại văn bản tiếng Việt thành tin thật / tin giả (huấn luyện nhị phân); hiển thị **3 mức** cho người dùng (tin thật, đáng ngờ, tin giả).

**Hướng được chọn:**

```
Nội dung văn bản ──► preprocess_text ──► PhoBERT ──► Vector 768 chiều
                                                          │
                                                          ▼
                                              StandardScaler + MLP (128, 64)
                                                          │
                                                          ▼
                                              Xác suất tin giả + verdict 3 mức
```

---

## 2. Vì sao chọn PhoBERT + MLP (text-only)?

| Lý do | Giải thích |
|-------|------------|
| Dữ liệu sẵn có | `full_dataset.csv` có title/content/is_fake — đủ cho pipeline văn bản |
| Nhất quán train/inference | Cùng `preprocess_text`, tránh lệch pipeline |
| Triển khai gọn | Không cần form metadata, không mô phỏng tín hiệu MXH |
| Kết quả thực nghiệm | F1 **93,71%**, ROC-AUC **98,50%** (hold-out 30%) |

**Hướng mở rộng:** Khi có siêu dữ liệu MXH thực, có thể thử nghiệm mô hình lai (concat embedding + metadata) — không nằm trong phạm vi triển khai hiện tại.

---

## 3. Vì sao chọn PhoBERT?

- Pre-train trên corpus tiếng Việt ~20 GB (VinAI, 2020).
- Vector **[CLS]** 768 chiều đại diện ngữ cảnh câu/đoạn.
- So với mBERT/BERT tiếng Anh: phù hợp task tiếng Việt hơn.

---

## 4. Vì sao PhoBERT frozen (không fine-tune)?

- Tiết kiệm GPU và thời gian đồ án.
- Embedding lưu `.npy` — tái sử dụng khi thử MLP/hyperparameter.
- F1 ~94% đủ chứng minh tính khả thi; fine-tune là hướng cải thiện sau.

---

## 5. Vì sao chọn MLP?

- Học phi tuyến trên vector dense 768 chiều.
- `predict_proba` cho xác suất tin giả.
- Huấn luyện nhanh trên CPU với ~169k mẫu (embedding đã tính sẵn).
- Siêu tham số: `(128, 64)`, ReLU, Adam, `early_stopping=True`, `alpha=0.1`.

---

## 6. Vì sao tiền xử lý `preprocess_text`?

| Bước | Mục đích |
|------|----------|
| Lowercase | Chuẩn hóa chữ |
| Xóa URL | Giảm nhiễu liên kết spam |
| Chuẩn hóa khoảng trắng | Ổn định đầu vào |
| PyVi tokenize | Phù hợp vocab PhoBERT |

**Quan trọng:** Cùng hàm cho `dataset_cleaner` (train) và `phobert_inference` (runtime).

---

## 7. Vì sao verdict 3 mức?

| Ngưỡng `fake_prob` | Verdict | Nhãn hiển thị |
|--------------------|---------|---------------|
| ≥ 75% | fake | TIN GIẢ |
| 35–74% | suspicious | ĐÁNG NGỜ |
| &lt; 35% | real | TIN THẬT |

- Một ngưỡng 50% nhị phân dễ gây hiểu nhầm với xác suất trung gian.
- Logic tập trung tại `backend/verdict.py` — frontend đọc `verdict` từ API.

---

## 8. Vì sao kiến trúc 3 module inference?

| Module | Chức năng |
|--------|-----------|
| 1 | Crawl URL / nhận text + `preprocess_text` |
| 2 | PhoBERT embedding |
| 3 | Scale + MLP + `ExplanationEngine` |

File: `backend/phobert_inference.py` — class `PhoBERTInferenceSystem`.

---

## 9. Vì sao FastAPI + Next.js?

- FastAPI: tích hợp Python ML, OpenAPI, async.
- Next.js 14: UI TypeScript, App Router, phù hợp demo bảo vệ.
- Tách frontend/backend — dễ mở rộng API mobile sau này.

---

## 10. Vì sao giải thích rule-based?

- Dễ đọc cho người dùng phổ thông (tiếng Việt).
- Không cần GPU thêm cho SHAP/LIME.
- Quét tín hiệu văn bản: giật gân, in hoa, dấu chấm than, độ dài bài...
- **Lưu ý:** Giải thích bổ sung, không thay thế quyết định MLP.

---

## 11. Thiết kế thí nghiệm

- Hold-out **30%** stratified, `random_state=42`.
- **5-fold** stratified CV.
- Chỉ số: Accuracy, Precision, Recall, F1, ROC-AUC.
- Script: `backend/experiments/run_experimental_evaluation.py`.

**Kết quả (tham chiếu):**

| Chỉ số | Hold-out | CV (mean ± std) |
|--------|----------|-----------------|
| F1 | 93,71% | 93,17% ± 1,33% |
| ROC-AUC | 98,50% | 98,21% ± 0,50% |

---

## 12. Kết luận — phương án cuối cùng

ShieldAI triển khai **PhoBERT embedding + MLP** trên văn bản tiếng Việt, với tiền xử lý thống nhất, verdict 3 mức, giải thích rule-based và ứng dụng web FastAPI + Next.js. Phương án cân bằng **độ chính xác**, **tính nhất quán** và **khả năng bảo vệ/demo** trong phạm vi đồ án tốt nghiệp.
