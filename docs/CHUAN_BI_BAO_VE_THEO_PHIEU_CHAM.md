# Checklist chuẩn bị bảo vệ — theo Phiếu chấm TTU

Tài liệu phụ trợ `TIEU_LUAN_SHIELDAI.md` (phiên bản 5.0 — PhoBERT text-only).

## Bảng ánh xạ tiêu chí → nội dung luận văn

| Tiêu chí | Điểm max | Vị trí trong luận văn | Việc cần làm thêm (Word) |
|----------|:--------:|----------------------|---------------------------|
| 1. Đầy đủ & format | 1.5 | Toàn bộ mục lục đầu | Font/lề thống nhất; Mục lục tự động |
| 2. Lý thuyết | 2.0 | Chương 1–3 | Chèn sơ đồ Hình 3.1–3.4 |
| 3. Thực nghiệm | 2.5 | Chương 4 | Chạy eval → chèn Hình 4.1–4.6; screenshot web |
| 4. Hỏi đáp | 2.0 | Phụ lục D + mục 5.2.2 | Luyện trả lời FAQ |
| 5. Tính mới | 1.0 | Mục 5.2.1 | Nhấn mạnh pipeline end-to-end + verdict 3 mức |
| 6. Trình bày | 1.0 | Toàn văn | Trích dẫn [n] trong đoạn văn |

## Câu hỏi hội đồng thường gặp — gợi ý trả lời

**1. Vì sao không fine-tune PhoBERT?**  
→ Tiết kiệm tài nguyên; F1 93,71% đủ mạnh; embedding tái sử dụng qua `.npy`; fine-tune là hướng phát triển.

**2. Vì sao không dùng metadata mạng xã hội?**  
→ Tập train không có MXH thực; triển khai text-only đảm bảo nhất quán train/inference; metadata là hướng mở rộng khi có dữ liệu.

**3. Đóng góp của em là gì, khác gì PhoBERT có sẵn?**  
→ Pipeline end-to-end: `preprocess_text` thống nhất, MLP + scaler, verdict 3 mức, `ExplanationEngine`, web FastAPI + Next.js, lịch sử SQLite, đánh giá hold-out + 5-fold CV.

**4. Vì sao chọn MLP thay vì XGBoost/SVM?**  
→ Phi tuyến, nhanh trên vector 768 chiều dense, `predict_proba`, ổn định với regularization.

**5. False positive nguy hiểm thế nào?**  
→ Gán nhầm tin thật là giả; UI hiển thị xác suất + mức "đáng ngờ" (35–74%), không khẳng định tuyệt đối.

**6. Hệ thống có CSDL không?**  
→ SQLite lưu user và lịch sử phân tích; mô hình lưu file `.joblib` / `.npy`.

## Slide bảo vệ gợi ý (15–20 phút)

1. Đặt vấn đề (2 slide)  
2. Mục tiêu SMART (1 slide)  
3. Kiến trúc PhoBERT + MLP (2 slide, Hình 3.1–3.2)  
4. Kết quả Bảng 4.3 + ROC/confusion matrix (2 slide)  
5. Demo live hoặc video (2 slide)  
6. Đóng góp & hạn chế (2 slide)  
7. Hướng phát triển (metadata, fine-tune) (1 slide)
