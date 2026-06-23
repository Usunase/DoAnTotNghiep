# Kịch bản thuyết trình bảo vệ Tiểu luận Tốt nghiệp - ShieldAI
**Tổng thời lượng dự kiến:** 20 phút
**Tốc độ nói:** Vừa phải, nhấn nhá vào các từ khóa kỹ thuật.

---

### Slide Mở đầu: Tiêu đề (1 phút)
**Lời thoại:**
"Kính chào quý Thầy Cô trong Hội đồng bảo vệ tiểu luận. Em là Hà Minh Chiến. Hôm nay, em xin phép trình bày đề tài tiểu luận tốt nghiệp của mình với tựa đề: **Xây dựng hệ thống phát hiện tin giả tiếng Việt - ShieldAI**. Đề tài được thực hiện nhằm giải quyết một vấn đề đang rất nhức nhối trên không gian mạng hiện nay."

---

### Slide 1: Bối cảnh và lý do chọn đề tài (1.5 phút)
**Lời thoại:**
"Như quý Thầy Cô đã biết, sự phát triển bùng nổ của mạng xã hội đã thay đổi cách chúng ta tiếp nhận thông tin. Tuy nhiên, nó cũng tạo môi trường lý tưởng cho tin giả lan truyền với tốc độ chóng mặt. **Tin giả (Fake News) có thể được hiểu là những thông tin sai lệch, được cố ý ngụy tạo và phát tán nhằm mục đích đánh lừa người đọc, thu hút sự chú ý hoặc trục lợi.** Hậu quả của nó là vô cùng nghiêm trọng, từ việc gây hoang mang dư luận, thiệt hại kinh tế cho đến ảnh hưởng an ninh trật tự.
Thực tế hiện nay, người dùng bình thường rất khó tự kiểm chứng thông tin vì khối lượng dữ liệu quá lớn. Nhu cầu cấp thiết đặt ra là phải có một công cụ tự động, hỗ trợ đánh giá mức độ tin cậy của bài báo. Đó chính là lý do em xây dựng hệ thống ShieldAI."

---

### Slide 2: Mục tiêu nghiên cứu và Đối tượng sử dụng (1.5 phút)
**Lời thoại:**
"Từ bối cảnh cấp thiết đó, nghiên cứu của em đặt ra 3 mục tiêu cốt lõi:
1. Xây dựng một mô hình AI phân loại tin giả tiếng Việt có độ chính xác cao, nắm bắt được ngữ cảnh.
2. Phát triển một cơ chế giải thích kết quả dự đoán nhằm tăng tính minh bạch cho hệ thống.
3. Thiết kế và triển khai mô hình thành một ứng dụng Web hoàn chỉnh phục vụ thực tiễn.

Và để hệ thống thực sự mang lại giá trị thực tiễn, ShieldAI được thiết kế hướng tới 3 nhóm đối tượng người dùng:
- **Người dùng phổ thông và mạng xã hội:** Có một công cụ trực quan để tự kiểm chứng các tin tức gây sốc hàng ngày.
- **Cơ quan báo chí, người làm truyền thông:** Dùng làm bộ lọc sơ bộ để đối chiếu chéo các nguồn tin lạ trước khi xuất bản.
- **Quản trị viên cộng đồng (Admin diễn đàn/group):** Có thể tích hợp trực tiếp API của hệ thống để tự động rà soát và kiểm duyệt tin giả trên quy mô lớn."

---

### Slide 3: Bài toán nghiên cứu (1 phút)
**Lời thoại:**
"Để hiện thực hóa các mục tiêu trên, dưới góc độ khoa học máy tính, bài toán cốt lõi chúng ta phải giải quyết ở đây là Phân loại chuỗi văn bản (Sequence Classification). Cụ thể là phân loại văn bản tin tức tiếng Việt thành các mức độ tin cậy khác nhau.
Bài toán này đối mặt với hai thách thức lớn:
Thứ nhất, tiếng Việt có cấu trúc ngữ pháp phức tạp, nhiều từ ghép, từ mượn và cách diễn đạt đa dạng.
Thứ hai, đa số các mô hình học sâu hiện nay hoạt động như một 'hộp đen' (Black-box), chúng đưa ra kết quả nhưng thiếu tính minh bạch, khiến người dùng khó lòng tin tưởng hoàn toàn."

---

### Slide 4: Tổng quan các nghiên cứu liên quan (1 phút)
**Lời thoại:**
"Nhìn lại quá trình phát triển của các phương pháp phân loại văn bản:
Ban đầu, các phương pháp học máy truyền thống như SVM hay Logistic Regression kết hợp TF-IDF được sử dụng, có ưu điểm là nhanh nhưng không hiểu được ngữ cảnh.
Sau đó, mạng nơ-ron hồi quy như BiLSTM ra đời, giải quyết phần nào bài toán ngữ cảnh nhưng lại kém hiệu quả với văn bản dài.
Gần đây, kiến trúc Transformer đã tạo ra bước đột phá. Các mô hình như BERT, đặc biệt là PhoBERT, có khả năng nắm bắt ngữ cảnh hai chiều một cách sâu sắc và vượt trội so với các phương pháp cũ."

---

### Slide 5: Khoảng trống nghiên cứu (1 phút)
**Lời thoại:**
"Dù đã có nhiều nghiên cứu áp dụng Transformer, em nhận thấy vẫn còn một số khoảng trống:
Thứ nhất, phần lớn nghiên cứu chỉ chạy đua về độ chính xác (Accuracy) mà bỏ qua khả năng diễn giải (Explainability).
Thứ hai, nếu áp dụng các thuật toán giải thích chuyên sâu như SHAP hay LIME, chi phí tính toán sẽ rất khổng lồ, gây độ trễ lớn, không thể đáp ứng được yêu cầu phản hồi thời gian thực của một Web API.
Cuối cùng, vẫn rất thiếu các nền tảng được đóng gói khép kín, thân thiện với người dùng cuối."

---

### Slide 6: Đề xuất hệ thống ShieldAI (1.5 phút)
**Lời thoại:**
"Để lấp đầy các khoảng trống đó, em đề xuất hệ thống ShieldAI. So với các dự án và nghiên cứu tương tự, ShieldAI được tối ưu hóa vượt trội ở 3 điểm cốt lõi:
Thứ nhất, **tối ưu về tính thực tiễn (End-to-End)**: Đa số các dự án khác chỉ dừng lại ở việc huấn luyện mô hình học máy trên máy tính cá nhân. ShieldAI là một hệ thống web khép kín, có khả năng tự động cào dữ liệu báo chí theo thời gian thực (Real-time Web Crawler) để phân tích khi người dùng nhập URL.
Thứ hai, **tối ưu về độ phân giải nhãn (Granularity)**: Thay vì chỉ phân loại cứng nhắc nhị phân (Đúng/Sai), ShieldAI chia kết quả làm 3 mức độ (Tin thật, Đáng ngờ, Tin giả). Điều này phản ánh sát với thực tế tin tức và cung cấp độ cảnh báo mềm dẻo hơn.
Thứ ba, và cũng là quan trọng nhất, **tối ưu về tốc độ phản hồi giải thích (XAI)**: Nếu dùng các thuật toán như SHAP hay LIME, một bài báo mất hàng chục giây để xử lý. ShieldAI tự phát triển cơ chế 'Heuristic Explanation' độc lập, giúp hệ thống vừa giải thích được chi tiết lý do nghi ngờ tin giả, vừa giữ được tốc độ phản hồi cực nhanh (dưới 1 giây)."

---

### Slide 7: Kiến trúc tổng thể hệ thống (1 phút)
**Lời thoại:**
"Về mặt kiến trúc, ShieldAI được thiết kế theo mô hình Client-Server đa tầng độc lập.
Frontend đóng vai trò tương tác trực quan với người dùng.
Backend xử lý các nghiệp vụ nặng như cào dữ liệu (crawl), lưu trữ cơ sở dữ liệu.
Và lõi AI Model là một khối độc lập chuyên nhận văn bản và trả về kết quả suy luận. Thiết kế này giúp hệ thống dễ dàng nâng cấp hoặc mở rộng tải trong tương lai."

---

### Slide 8: Mô hình PhoBERT và lý do lựa chọn (1 phút)
**Lời thoại:**
"Lý do em chọn PhoBERT thay vì các mô hình đa ngôn ngữ khác là vì PhoBERT được tiền huấn luyện độc quyền trên 20GB ngữ liệu tiếng Việt. Nó sinh ra để dành cho tiếng Việt, do đó nó tối ưu hóa cực tốt việc nắm bắt cú pháp, từ vựng đặc thù. Kết hợp với bộ thư viện Transformers của HuggingFace, quá trình Fine-tuning diễn ra rất trơn tru và hiệu quả."

---

### Slide 9: Quy trình xử lý dữ liệu (1.5 phút)
**Lời thoại:**
"Chất lượng của mô hình phụ thuộc vào dữ liệu. Quá trình này được em làm rất kỹ lưỡng.
Từ hơn 22.000 bài báo tiếng Việt đã gán nhãn, em tiến hành làm sạch, loại bỏ các thẻ HTML, ký tự nhiễu.
Tiếp theo, em sử dụng công cụ PyVi để tách từ (Word Segmentation), nối các từ ghép lại để mô hình hiểu đúng nghĩa (ví dụ: sinh_viên thay vì sinh, viên rời rạc).
Sau đó, dữ liệu được chia theo tỷ lệ 76% cho huấn luyện, 12% validation và 12% kiểm thử bằng phương pháp Stratified Split nhằm đảm bảo tỷ lệ nhãn đồng đều."

---

### Slide 10: Luồng thuật toán & Cơ chế Heuristic (1.5 phút)
**Lời thoại:**
"Đây là phần cốt lõi tạo nên sự minh bạch cho ShieldAI: Cơ chế Heuristic.
Thay vì can thiệp vào trọng số của PhoBERT gây tốn tài nguyên, Heuristic hoạt động như một bộ lọc hậu xử lý (Post-hoc).
Sau khi PhoBERT đưa ra dự đoán, thuật toán Heuristic sẽ quét qua văn bản để tìm kiếm các 'bằng chứng' vi phạm như: sự xuất hiện dày đặc của từ ngữ giật gân, sắc thái cảm xúc tiêu cực cực đoan, hay việc lạm dụng viết hoa sai quy chuẩn. Cách tiếp cận này giải quyết bài toán diễn giải chỉ trong tích tắc với độ phức tạp $O(N)$."

---

### Slide 11: Cơ sở dữ liệu & Triển khai hệ thống (1 phút)
**Lời thoại:**
"Để đưa hệ thống vào thực tiễn, em sử dụng các công nghệ hiện đại nhất.
Backend được xây dựng bằng framework FastAPI giúp xử lý bất đồng bộ, tối ưu hóa thời gian cào dữ liệu từ Web Crawler.
Frontend được triển khai bằng Next.js mang lại trải nghiệm mượt mà.
Cơ sở dữ liệu SQLite được sử dụng để lưu lại lịch sử quét, hỗ trợ người dùng xem lại kết quả đã phân tích."

---

### Slide 12: Giao diện trực quan của hệ thống (1 phút)
**Lời thoại:**
"Quý Thầy Cô có thể thấy trên giao diện, tính dễ sử dụng được đặt lên hàng đầu.
Người dùng chỉ cần dán một URL bài báo bất kỳ. Hệ thống sẽ tự động bóc tách nội dung, phân tích và trả về giao diện trực quan gồm:
Điểm số tin cậy (Confidence Score), Nhãn cảnh báo với màu sắc rõ ràng, và đặc biệt là phần diễn giải (Heuristic Explanations) chỉ đích danh những yếu tố gây nghi ngờ trong bài."

---

### Slide 13: Kết quả thực nghiệm (1.5 phút)
**Lời thoại:**
"Về kết quả thực nghiệm, trên tập kiểm thử nội bộ với hơn 2.700 mẫu, mô hình PhoBERT đạt độ chính xác (Accuracy) lên tới 96.32%, vượt xa các thuật toán cơ sở như SVM hay BiLSTM.
Chỉ số F1-Score đạt 93.42%, chứng tỏ mô hình xử lý rất tốt vấn đề mất cân bằng dữ liệu giữa nhãn Thật và Giả.
Để khẳng định tính ổn định, em đã chạy kiểm thử ngoại lai (External Test) trên các mẫu hoàn toàn mới từ Internet, và mô hình vẫn duy trì độ chính xác ở mức 91.5%."

---

### Slide 14: Phân tích và đánh giá kết quả (1.5 phút)
**Lời thoại:**
"Từ kết quả trên, có thể rút ra một số đánh giá quan trọng.
Đầu tiên, hệ thống đã kiểm soát tỷ lệ bỏ lọt tin giả (False Negative) ở mức rất thấp, điều kiện tiên quyết đối với một hệ thống cảnh báo.
Thứ hai, việc kết hợp giữa mô hình học sâu và cơ chế Heuristic đã chứng minh được tính hiệu quả: Hệ thống vừa cung cấp được độ chính xác của Deep Learning, vừa đảm bảo tính minh bạch, mà thời gian trễ tổng thể vẫn luôn dưới 1 giây cho mỗi truy vấn."

---

### Slide 15: Hạn chế (1 phút)
**Lời thoại:**
"Tuy nhiên, hệ thống hiện tại vẫn tồn tại một số hạn chế nhất định.
Thứ nhất, mô hình đôi khi nhầm lẫn với các bài báo thuộc lĩnh vực hình sự, do văn phong nhóm này thường chứa nhiều từ ngữ mạnh, mang sắc thái tiêu cực.
Thứ hai, hệ thống chủ yếu phân tích dựa trên đặc trưng ngôn ngữ, nên khó phát hiện nếu kẻ gian tạo ra tin giả bằng cách sao chép y hệt văn phong nhà nước và chỉ thay đổi các số liệu, địa danh lịch sử.
Cuối cùng, với các văn bản quá ngắn (dưới 3 câu), độ tin cậy của phân tích sẽ giảm sút."

---

### Slide 16: Kết luận và hướng phát triển (1.5 phút)
**Lời thoại:**
"Tóm lại, đề tài đã hoàn thành xuất sắc các mục tiêu đề ra: Ứng dụng thành công PhoBERT vào thực tiễn và giải quyết hiệu quả bài toán giải thích bằng cơ chế Heuristic.
Trong tương lai, để khắc phục các hạn chế, em đề xuất 2 hướng phát triển:
Một là tích hợp Tri thức đồ thị (Knowledge Graph) để hệ thống có thể đối chiếu các thực thể, sự kiện lịch sử.
Hai là ứng dụng công nghệ RAG (Retrieval-Augmented Generation) để tự động truy xuất đối chiếu thông tin với các trang báo chính thống theo thời gian thực."

---

### Slide 17 & Q&A (0.5 phút)
**Lời thoại:**
"Phần trình bày của em đến đây là kết thúc. Em xin chân thành cảm ơn quý Thầy Cô trong Hội đồng đã lắng nghe.
Em rất mong nhận được những nhận xét, góp ý và các câu hỏi từ Thầy Cô để đề tài được hoàn thiện hơn ạ."

---

### 💡 Lưu ý khi bị đặt câu hỏi (Dựa trên Slide Backup):
- **Nếu bị hỏi: "Tại sao không dùng SHAP/LIME để giải thích?"**
  *Trả lời:* Dựa vào slide backup 1. Khẳng định SHAP/LIME phải sinh nhiễu và chạy lại mô hình hàng nghìn lần, mất từ 10-30 giây cho một bài báo, không thể làm API thời gian thực. Heuristic giải quyết bài toán thời gian với chi phí thuật toán rất thấp.
- **Nếu bị hỏi: "Tại sao phải báo cáo cả F1-Score khi Accuracy đã rất cao?"**
  *Trả lời:* Dựa vào slide backup 2. Trong thực tế, số lượng tin giả ít hơn tin thật rất nhiều (dữ liệu mất cân bằng). Accuracy đôi khi gây ngộ nhận, còn F1-Score là trung bình điều hòa giữa Precision và Recall, phản ánh chính xác nhất năng lực bắt tin giả thực sự của hệ thống.
