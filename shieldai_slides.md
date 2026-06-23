---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 30px;
  }
  h1 {
    color: #1e3a8a; /* Deep blue */
    font-size: 55px;
  }
  h2 {
    color: #1e3a8a;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 10px;
    margin-bottom: 30px;
  }
  strong {
    color: #0369a1;
  }
  ul {
    line-height: 1.5;
  }
---

<!-- _class: lead -->
# Xây dựng hệ thống phát hiện tin giả tiếng Việt
## (Hệ thống ShieldAI)

**Sinh viên:** Hà Minh Chiến - 2202095
**Giảng viên hướng dẫn:** ThS. Trần Ngọc Anh
**Ngành:** Khoa Học Máy Tính

---

## 1. Đặt vấn đề & Lý do chọn đề tài

- **Thực trạng:** Sự bùng nổ của mạng xã hội khiến tin giả lây lan nhanh, gây hậu quả nghiêm trọng.
- **Hạn chế của AI hiện tại:** Các mô hình học sâu truyền thống thường mang tính chất **"hộp đen"** (black-box), khó diễn giải quyết định cho người dùng.
- **Giải pháp:** Hệ thống **ShieldAI** ra đời nhằm cung cấp công cụ kiểm chứng thông tin:
  - **Độ chính xác cao**
  - **Tính minh bạch** (Có khả năng giải thích)

---

## 2. Ý nghĩa tên gọi "ShieldAI"

- **"Shield" (Lá chắn) + "AI" (Trí tuệ nhân tạo)**
- **Sứ mệnh:** Xây dựng một lá chắn công nghệ thông minh và tự động.
- **Mục tiêu:** Bảo vệ người dùng mạng xã hội tại Việt Nam trước các luồng thông tin độc hại, sai lệch và lừa đảo.

---

## 3. Kiến trúc Tổng thể Hệ thống

- **Frontend (Next.js 14):** Giao diện tương tác người dùng thân thiện, ổn định.
- **Backend (FastAPI):** Xử lý bất đồng bộ, tốc độ cao.
- **Core AI:** Mô hình ngôn ngữ lớn **PhoBERT** (Tối ưu hóa bằng Fine-tuning).
- **Data Flow:** Tích hợp **Web Crawler** (BeautifulSoup) tự động trích xuất nội dung từ URL bài báo.

---

## 4. Xử lý Ngôn ngữ Tự nhiên với PhoBERT

- **Mô hình PhoBERT:** Kiến trúc Transformer tối ưu chuyên biệt cho tiếng Việt.
- **Phương pháp tiếp cận:** Phân loại chuỗi (Sequence Classification).
- **Quy trình:**
  - Trích xuất đặc trưng ngữ nghĩa từ token `[CLS]`.
  - Khắc phục hạn chế của các phương pháp đếm từ truyền thống (như TF-IDF).
  - Khả năng nắm bắt cấu trúc ngữ pháp phức tạp.

---

## 5. Động cơ Giải thích (Explanation Engine)

Giải quyết vấn đề "Hộp đen" của AI thông qua Cơ chế Heuristics (Rule-based):

- **Phân tích Cảm xúc (Sentiment):** Phát hiện ngôn từ kích động.
- **Mật độ In hoa:** Phát hiện việc lạm dụng VIẾT HOA ĐỂ GÂY CHÚ Ý.
- **Từ ngữ Giật gân:** Đếm các từ khóa clickbait ("sốc", "kinh hoàng").
- **Tính chủ quan:** Tỷ lệ từ ngữ thể hiện quan điểm cá nhân thay vì sự thật khách quan.

*Mỗi dự đoán của mô hình đều đi kèm với các bằng chứng cụ thể.*

---

## 6. Dữ liệu Huấn luyện & Tiền xử lý

- **Quy mô:** Hơn **22.000** bài báo.
- **Làm sạch (TextCleaner):** Khử nhiễu HTML, loại bỏ trùng lặp (Deduplication) để tránh rò rỉ dữ liệu (Data Leakage).
- **Tách từ (Tokenization):** Sử dụng thư viện **PyVi** chuẩn hóa tiếng Việt.
- **Phân chia:** Stratified Split (76% Train - 12% Validation - 12% Test) giúp cân bằng nhãn phân loại.

---

## 7. Cơ chế Phân loại đa mức độ (Thresholds)

Không sử dụng phân loại nhị phân (Thật/Giả) cứng nhắc, ShieldAI áp dụng 3 mức độ tinh tế:

1. **Tin thật:** Xác suất < 35% (Vùng an toàn)
2. **Đáng ngờ:** 35% - 74% (Cần xác minh thêm)
3. **Tin giả:** Xác suất ≥ 75% (Cảnh báo đỏ)

*Điểm cắt 75% được chọn khắt khe để bảo vệ độ chuẩn xác (Precision), tránh đánh oan tin chính thống.*

---

## 8. Kết quả Thực nghiệm Nội bộ (Internal Test)

Đánh giá trên tập kiểm thử độc lập (2.716 mẫu):

| Mô hình (Model) | Accuracy | F1-Score |
| :--- | :---: | :---: |
| Logistic Regression (TF-IDF) | 82.15% | 80.82% |
| Support Vector Machine (SVM) | 85.34% | 84.10% |
| BiLSTM (Word2Vec) | 89.67% | 88.66% |
| **ShieldAI (PhoBERT Fine-tuned)** | **96.32%** | **93.42%** |

*Hiệu năng vượt trội nhờ khả năng thấu hiểu ngữ cảnh sâu của PhoBERT.*

---

## 9. Kiểm thử Độc lập & Chịu tải

- **External Validation:** Thử nghiệm trên 100 bài báo mới xuất bản năm 2026.
  - Kết quả: Đạt độ chính xác **91.5%**.
  - Chứng minh mô hình không bị "học vẹt" (Overfitting).
- **Latency & Throughput (JMeter):**
  - Tốc độ phản hồi (End-to-End): **< 1 giây**.
  - Thông lượng: 15-20 requests/second.
  - Đáp ứng tốt nhu cầu xử lý thời gian thực.

---

## 10. Phân tích Sai số (Error Analysis)

- **Dương tính giả (Báo nhầm tin thật thành tin giả):**
  - Xảy ra ở các bài báo hình sự/thể thao dùng văn phong giật gân (Clickbait) quá giống tin lừa đảo.
- **Âm tính giả (Bỏ lọt tin giả):**
  - Xảy ra khi tin giả được ngụy trang cực kỳ tinh vi dưới dạng văn bản hành chính nhà nước (VD: thông báo phạt nguội).

---

## 11. Trải nghiệm Người dùng (UX)

- Người dùng chỉ cần sao chép và **dán URL bài báo**.
- Hệ thống tự động bóc tách và phân tích.
- Hiển thị trực quan:
  - Điểm số tin cậy (Confidence Score).
  - Nhãn cảnh báo (Verdict).
  - Chi tiết các nguyên nhân (Heuristic Explanations).

---

## 12. Tổng kết & Đóng góp

- **Thành tựu cốt lõi:**
  - Áp dụng thành công kiến trúc PhoBERT vào bài toán thực tế.
  - Xây dựng hệ thống Web phân tán (Client-Server) hoàn chỉnh.
  - Giải quyết bài toán giải thích (XAI) thông qua Heuristics minh bạch.
- **Ý nghĩa:** Chuyển giao AI từ phòng thí nghiệm thành một ứng dụng thiết thực, bảo vệ người dùng mạng.

---

## 13. Hướng phát triển tương lai

- Cải tiến nhận diện bằng phương pháp **Fact-Checking** (Kiểm chứng sự kiện).
- Tích hợp **Tri thức Đồ thị (Knowledge Graph)**.
- Áp dụng kỹ thuật RAG (Retrieval-Augmented Generation) để đối chiếu thông tin với các nguồn báo chí chính thống theo thời gian thực.

---

<!-- _class: lead -->
# Xin chân thành cảm ơn!
## Q & A
*Cảm ơn Quý Thầy Cô và Hội đồng đã lắng nghe.*
