---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 28px;
  }
  h1 {
    color: #1e3a8a; /* Deep blue */
    font-size: 48px;
  }
  h2 {
    color: #1e3a8a;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 10px;
    margin-bottom: 25px;
    font-size: 36px;
  }
  strong {
    color: #0369a1;
  }
  ul {
    line-height: 1.5;
  }
  li {
    margin-bottom: 15px;
  }
---

<!-- _class: lead -->
# Xây dựng hệ thống phát hiện tin giả tiếng Việt (ShieldAI)
**Bảo vệ Luận văn Tốt nghiệp - Khoa Công nghệ Thông tin**
**Sinh viên:** Hà Minh Chiến

---

## 1. Bối cảnh và lý do chọn đề tài

- Mạng xã hội thúc đẩy tốc độ lan truyền tin giả (Fake News).
- Tin giả gây ảnh hưởng tiêu cực đến an ninh và nhận thức cộng đồng.
- Nhu cầu cấp thiết về công cụ hỗ trợ người dùng kiểm chứng thông tin.
- Hệ thống ShieldAI được đề xuất nhằm tự động hóa quy trình phát hiện tin giả.

---

## 2. Bài toán nghiên cứu

- Phân loại văn bản tin tức tiếng Việt thành các mức độ tin cậy.
- Bài toán cốt lõi: Phân loại chuỗi (Sequence Classification).
- Thách thức 1: Tính đa dạng và phức tạp của ngữ pháp tiếng Việt.
- Thách thức 2: Thiếu tính minh bạch trong các mô hình học sâu (hộp đen).

---

## 3. Mục tiêu nghiên cứu

- Xây dựng mô hình phân loại tin giả tiếng Việt có độ chính xác cao.
- Phát triển cơ chế giải thích kết quả dự đoán nhằm tăng tính minh bạch.
- Thiết kế và triển khai ứng dụng Web hoàn chỉnh phục vụ thực tiễn.

---

## 4. Tổng quan các nghiên cứu liên quan

- Phương pháp học máy truyền thống: Logistic Regression, SVM (đặc trưng TF-IDF).
- Mạng nơ-ron hồi quy: BiLSTM, GRU (đặc trưng Word2Vec).
- Kiến trúc Transformer: PhoBERT, mBERT (nắm bắt ngữ cảnh hai chiều).

---

## 5. Khoảng trống nghiên cứu

- Tập trung vào độ chính xác, bỏ qua khả năng diễn giải (Explainability).
- Các thuật toán giải thích (SHAP, LIME) đòi hỏi chi phí tính toán lớn.
- Khó tích hợp các thuật toán XAI phức tạp vào API yêu cầu thời gian thực.
- Thiếu các nền tảng ứng dụng khép kín hỗ trợ người dùng cuối.

---

## 6. Đề xuất hệ thống ShieldAI

- Ứng dụng mô hình PhoBERT Fine-tuning cho tác vụ Sequence Classification.
- Cảnh báo ba mức độ: Tin thật, Đáng ngờ, Tin giả.
- Tích hợp cơ chế Heuristic Explanation định hướng tính minh bạch.
- Tối ưu hóa kiến trúc xử lý nhằm đảm bảo tốc độ phản hồi nhanh.

---

## 7. Kiến trúc tổng thể hệ thống

- Trình bày kiến trúc Client-Server đa tầng độc lập.
- Frontend: Tương tác người dùng (Web Application).
- Backend: Cào dữ liệu, xử lý nghiệp vụ và quản trị cơ sở dữ liệu.
- AI Model: Khối suy luận xử lý ngôn ngữ tự nhiên.

---

## 8. Mô hình PhoBERT và lý do lựa chọn

- PhoBERT là mô hình ngôn ngữ dựa trên kiến trúc Transformers.
- Được tiền huấn luyện độc quyền trên 20GB ngữ liệu tiếng Việt.
- Tối ưu hóa việc nắm bắt cú pháp và ngữ nghĩa đặc thù của tiếng Việt.
- Thư viện Transformers và PyTorch hỗ trợ tích hợp linh hoạt.

---

## 9. Quy trình xử lý dữ liệu

- Tổng hợp hơn 22.000 bài báo tiếng Việt đã gán nhãn.
- Làm sạch (Data Cleaning): Loại bỏ HTML, liên kết, ký tự nhiễu.
- Tách từ (Word Segmentation) bằng công cụ PyVi.
- Phân tầng dữ liệu (Stratified Split) với tỷ lệ 76-12-12.

---

## 10. Cơ chế Heuristic Explanation

- Đây là cơ chế giải thích hậu xử lý (Post-hoc Explanation).
- Hoạt động độc lập, không tác động vào trọng số mô hình PhoBERT.
- Cung cấp bằng chứng: Từ ngữ giật gân, Cảm xúc, Mật độ in hoa.
- Giải quyết vấn đề XAI mà không yêu cầu chi phí tính toán lớn.

---

## 11. Triển khai hệ thống Web

- Backend: Sử dụng khung làm việc FastAPI xử lý bất đồng bộ.
- Database: Tích hợp hệ quản trị cơ sở dữ liệu SQLite.
- Frontend: Xây dựng giao diện tương tác bằng Next.js.
- Web Crawler: Trích xuất nội dung bài báo tự động theo thời gian thực.

---

## 12. Kết quả thực nghiệm

- Kết quả trên tập kiểm thử nội bộ (Khoảng 2.716 mẫu).
- Accuracy đạt 96.32% (so với SVM 85.34%, BiLSTM 89.67%).
- F1-Score đạt 93.42% đảm bảo cân bằng giữa Precision và Recall.
- Kết quả External Test (kiểm thử ngoại lai) đạt Accuracy 91.5%.

---

## 13. Phân tích và đánh giá kết quả

- Accuracy 96.32% chứng tỏ mô hình bao quát tốt cả hai nhãn.
- F1-Score 93.42% phản ánh sự ổn định trên dữ liệu không cân bằng.
- Tỷ lệ bỏ lọt tin giả (False Negative) được kiểm soát ở mức rất thấp.
- Cơ chế giải thích hoạt động ổn định với thời gian trễ dưới 1 giây.

---

## 14. Hạn chế

- Mô hình nhầm lẫn đối với các bài báo hình sự có văn phong giật gân.
- Bỏ lọt các văn bản lừa đảo bắt chước hoàn hảo văn phong hành chính nhà nước.
- Dễ bị biến thiên độ tin cậy khi độ dài văn bản quá ngắn (dưới 3 câu).
- Chưa có khả năng kiểm chứng chéo sự kiện với thế giới thực.

---

## 15. Kết luận và hướng phát triển

- Tích hợp thành công PhoBERT vào ứng dụng thực tiễn.
- Cơ chế Heuristics giải quyết hiệu quả bài toán giải thích hậu xử lý.
- Hướng phát triển 1: Tích hợp Tri thức đồ thị (Knowledge Graph) để kiểm chứng.
- Hướng phát triển 2: Áp dụng RAG truy xuất báo chí chính thống thời gian thực.

---

<!-- _class: lead -->
# Xin chân thành cảm ơn!
## Phần Hỏi đáp (Q&A)

---

## Slide Dự phòng (Backup 1) - Tại sao không dùng SHAP/LIME?

- SHAP/LIME đòi hỏi chi phí tính toán (Computational Cost) rất lớn.
- Phải sinh nhiễu và chạy lại mô hình hàng nghìn lần cho mỗi văn bản.
- Gây độ trễ (Latency) không thể chấp nhận được trên môi trường Web API.
- Heuristic đáp ứng tốc độ phản hồi cực thấp (dưới 1s) với chi phí $O(N)$.

---

## Slide Dự phòng (Backup 2) - Phân biệt Accuracy và F1-Score

- Accuracy đo tỷ lệ dự đoán đúng chung trên toàn bộ tập dữ liệu.
- Trong dữ liệu mất cân bằng, Accuracy có thể gây ngộ nhận về hiệu năng.
- F1-Score kết hợp Precision (độ chuẩn xác) và Recall (độ bao phủ).
- F1-Score đánh giá khách quan hơn sự ổn định của hệ thống phòng vệ.
