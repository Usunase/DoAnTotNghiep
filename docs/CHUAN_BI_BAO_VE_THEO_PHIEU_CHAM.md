# Checklist chuẩn bị bảo vệ — theo Phiếu chấm TTU

Tài liệu phụ trợ `TIEU_LUAN_SHIELDAI.md` (phiên bản 4.0). Mục tiêu: tối đa hóa tiêu chí 4 (Hỏi đáp) và 5 (Tính mới).

## Bảng ánh xạ tiêu chí → nội dung luận văn

| Tiêu chí | Điểm max | Vị trí trong luận văn | Việc cần làm thêm (Word) |
|----------|:--------:|----------------------|---------------------------|
| 1. Đầy đủ & format | 1.5 | Toàn bộ mục lục đầu | Font/lề thống nhất; Mục lục tự động |
| 2. Lý thuyết | 2.0 | Chương 1–3 | Chèn sơ đồ Hình 3.1–3.4 |
| 3. Thực nghiệm | 2.5 | Chương 4 | Chạy eval → chèn Hình 4.1–4.8; screenshot web |
| 4. Hỏi đáp | 2.0 | Phụ lục D + mục 5.2.2 | Luyện trả lời FAQ |
| 5. Tính mới | 1.0 | Mục 5.2.1 | Nhấn mạnh khi trình bày |
| 6. Trình bày | 1.0 | Toàn văn | Trích dẫn [n] trong đoạn văn |

## Câu hỏi hội đồng thường gặp — gợi ý trả lời

**1. Vì sao không fine-tune PhoBERT?**  
→ Tiết kiệm tài nguyên; mục tiêu chứng minh hybrid; F1 97,51% đủ mạnh; embedding tái sử dụng.

**2. Metadata MXH mô phỏng có tin được không?**  
→ Thừa nhận hạn chế; ablation vẫn valid; inference dùng metadata thật do user nhập; hướng phát triển: thu thập dữ liệu thực.

**3. Đóng góp của em là gì, khác gì PhoBERT có sẵn?**  
→ Pipeline lai 10 meta + MLP; module giải thích; 4 mô-đun inference; web app; ablation 7 cấu hình; code tích hợp end-to-end.

**4. Vì sao chọn MLP thay vì XGBoost/SVM?**  
→ Phi tuyến, nhanh trên 778 chiều dense, predict_proba, ổn định với regularization.

**5. False positive nguy hiểm thế nào?**  
→ Gán nhầm tin thật = giả; UI hiển thị xác suất + mức "đáng ngờ", không khẳng định tuyệt đối.

**6. Hệ thống có CSDL không?**  
→ Không dùng SQL; lưu file CSV/npy/joblib; phù hợp inference offline-first.

## Slide bảo vệ gợi ý (15–20 phút)

1. Đặt vấn đề (2 slide)  
2. Mục tiêu SMART (1 slide)  
3. Kiến trúc + pipeline (2 slide, Hình 3.1–3.2)  
4. Kết quả Bảng 4.3 + Hình 4.2 (2 slide)  
5. Demo live hoặc video (2 slide)  
6. Đóng góp & hạn chế (2 slide)  
7. Hướng phát triển (1 slide)
