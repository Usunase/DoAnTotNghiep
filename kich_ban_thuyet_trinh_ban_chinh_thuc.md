# Kịch bản thuyết trình bảo vệ Tiểu luận Tốt nghiệp - Hệ thống ShieldAI
*(Phiên bản Tối ưu Nhịp điệu Thuyết trình - Kết hợp Văn phong Học thuật & Sự mượt mà khi nói)*

**Tổng số Slide:** 19 Slide (Bao gồm phần trình diễn Demo thực tế)
**Tổng thời lượng dự kiến:** 20 phút
**Lưu ý khi trình bày:** Đây là kịch bản đã được gọt giũa để **dễ thở, dễ ngắt nhịp** khi nói, nhưng vẫn giữ nguyên độ chính xác của các thuật ngữ chuyên ngành. Khi trình bày, bạn hãy kết hợp chỉ tay vào các sơ đồ tương ứng trên màn hình để tăng tính thuyết phục.

---

### Slide 1: Tiêu đề (0.5 phút)
**Lời thoại:**
"Kính chào quý Thầy Cô trong Hội đồng đánh giá Tiểu luận Tốt nghiệp. Em là Hà Minh Chiến. Hôm nay, em xin phép trình bày đề tài nghiên cứu của mình với tựa đề: **Xây dựng hệ thống phát hiện tin giả tiếng Việt - ShieldAI**."

---

### Slide 2: Bối cảnh và lý do chọn đề tài (1.5 phút)
**Lời thoại:**
"Kính thưa Hội đồng, sự bùng nổ của mạng xã hội đã thay đổi hoàn toàn cách chúng ta tiếp nhận thông tin. Cùng với đó, nó cũng tạo ra một môi trường hoàn hảo cho sự lây lan của tin giả.
Dưới góc độ nghiên cứu, tin giả không đơn thuần là những nhầm lẫn vô ý. Đó là những nội dung **được cố tình ngụy tạo** một cách tinh vi, với mục đích thao túng dư luận hoặc trục lợi. 
Vì người dùng bình thường không thể tự mình kiểm chứng mọi nguồn tin, chúng ta cần một công cụ tự động, đóng vai trò như một 'lớp lá chắn' trên không gian mạng. Đó chính là động lực để em thực hiện đề tài xây dựng hệ thống ShieldAI."

---

### Slide 3: Mục tiêu nghiên cứu và Đối tượng sử dụng (1.5 phút)
**Lời thoại:**
"Đề tài đặt ra ba mục tiêu cốt lõi:
Thứ nhất, xây dựng một mô hình Trí tuệ Nhân tạo phân loại chính xác tin tức tiếng Việt.
Thứ hai, phát triển một cơ chế minh bạch, giúp giải thích quyết định của mô hình cho người dùng hiểu.
Và thứ ba, triển khai hệ thống thành một ứng dụng Web hoàn chỉnh.
Hệ thống được thiết kế hướng tới 3 nhóm đối tượng: (1) Người dùng phổ thông tự kiểm chứng; (2) Cơ quan báo chí đối chiếu chéo; và (3) Quản trị viên sử dụng API để kiểm duyệt tự động."

---


### Slide 4: Tổng quan các hướng tiếp cận hiện tại (1.5 phút)
**Lời thoại:**
"Khảo lược các nghiên cứu trước đây, công nghệ phân loại văn bản đã trải qua 3 giai đoạn:
Giai đoạn đầu là Học máy truyền thống như SVM. Tuy chạy rất nhanh, nhưng lại yếu trong việc biểu diễn ngữ nghĩa.
Giai đoạn tiếp theo là Mạng nơ-ron hồi quy như BiLSTM. Phương pháp này gặp phải giới hạn suy giảm thông tin đối với các bài báo dài.
Và hiện tại là sự thống trị của kiến trúc **Transformer**. Điển hình như mô hình PhoBERT, nhờ cơ chế Self-Attention, nó đã giải quyết triệt để rào cản độ dài và cho phép trích xuất đặc trưng ngữ cảnh hai chiều một cách toàn diện."

---

### Slide 5: Khoảng trống nghiên cứu (1.5 phút)
**Lời thoại:**
"Dù Transformer rất mạnh, nhưng qua phân tích, em nhận thấy vẫn còn 3 khoảng trống lớn:
Thứ nhất, phần lớn các công trình chỉ tập trung vào điểm số Accuracy mà bỏ qua tính minh bạch (Explainable AI) đối với dự đoán của mô hình.
Thứ hai, một số nghiên cứu dùng SHAP hay LIME để giải thích, nhưng các thuật toán này tốn hàng chục giây cho mỗi bài báo, vi phạm ràng buộc về thời gian thực của môi trường Web API.
Và thứ ba, các nghiên cứu thường chỉ dừng ở mức mô hình thử nghiệm cục bộ, thiếu đi sự tích hợp thành một kiến trúc phần mềm hoàn chỉnh."

---


### Slide 6: Đề xuất Kiến trúc Phân tách ShieldAI (1.5 phút)
**Lời thoại:**
*(Chỉ tay vào sơ đồ phân tách luồng)*
"Kính thưa Hội đồng, đây là **Kiến trúc Phân tách** - điểm nhấn kỹ thuật tạo nên sự vượt trội của ShieldAI so với các nghiên cứu trước đây. Thay vì thiết kế một 'Hộp đen' AI khổng lồ, em tách hệ thống thành 2 luồng song song:

Luồng trên là **Lõi suy luận PhoBERT**, chuyên đọc hiểu ngữ cảnh sâu để tính toán chính xác xác suất tin giả.
Luồng dưới là **Cơ chế Heuristics**, chạy độc lập để quét các dấu hiệu bất thường bề mặt và tự động tạo lời giải thích.

**Điểm tối ưu đột phá nằm ở đâu?**
Các nghiên cứu khác thường dùng thuật toán giải thích (như SHAP hay LIME) lồng trực tiếp vào AI, khiến hệ thống mất hàng chục giây xử lý. 
Ngược lại, với cấu trúc tách rời này, ShieldAI vừa đập tan được rào cản 'hộp đen' minh bạch hóa kết quả, vừa giữ được tốc độ phản hồi cực nhanh dưới 1 giây — hoàn toàn đáp ứng được môi trường Web thời gian thực."

---

### Slide 7: Quy trình xử lý dữ liệu (2.0 phút)
**Lời thoại:**
*(Chỉ tay vào luồng xử lý dữ liệu trên màn hình)*
"Kính thưa Hội đồng, hệ thống được huấn luyện trên một tập dữ liệu quy mô lớn với hơn 22.000 bài báo tiếng Việt. Để mô hình học được các đặc trưng chính xác nhất, dữ liệu phải đi qua 3 bước xử lý nghiêm ngặt:

Bước đầu tiên là Tiền xử lý (Preprocessing). Mục tiêu ở đây là làm sạch văn bản thô, bóc tách và loại bỏ các thẻ HTML nhiễu, URL lỗi hay các ký tự rác.

Bước thứ hai, mang tính quyết định với ngôn ngữ tiếng Việt, là Tách từ (Word Segmentation) bằng bộ công cụ PyVi. Vì tiếng Việt là ngôn ngữ đơn lập, nếu để nguyên các chữ rời rạc, mô hình sẽ mất đi ý nghĩa của các từ ghép. PyVi giúp kết nối các âm tiết rời rạc lại với nhau, đảm bảo mô hình PhoBERT không bị hụt từ vựng và nắm bắt chính xác ngữ cảnh văn bản.

Cuối cùng là phân chia dữ liệu bằng kỹ thuật Phân tầng (Stratified Split) với tỷ lệ 76-12-12. Thay vì chia ngẫu nhiên, kỹ thuật phân tầng bảo đảm tỷ lệ phân phối nhãn 'Thật' - 'Giả' luôn đồng đều ở cả 3 tập (Train, Val, Test). Kỹ thuật này là cốt lõi để ngăn chặn sự thiên lệch (Bias) và bảo đảm quá trình hội tụ của mô hình là khách quan nhất."

---

### Slide 8: Mô hình PhoBERT và lý do lựa chọn (2 phút)
**Lời thoại:**
*(Chỉ tay vào luồng đi của sơ đồ kiến trúc PhoBERT)*
"Trong phần lõi AI, em áp dụng kiến trúc **PhoBERT Fine-tuned Sequence Classification**. 
Quá trình suy luận diễn ra như sau: Văn bản sẽ đi qua 12 lớp Transformer của PhoBERT. Toàn bộ ngữ nghĩa được nén lại thành một Vector đặc biệt [CLS] 768 chiều.
Vector này sau đó được truyền qua mạng nơ-ron MLP (kết hợp kỹ thuật Dropout để tránh Overfitting). Cuối cùng, hàm Softmax sẽ chuẩn hóa đầu ra thành **ma trận phân phối xác suất**. Dựa trên tỷ lệ này, hệ thống sẽ đưa ra phán quyết phân loại cuối cùng."

---

### Slide 9: Cơ sở dữ liệu & Triển khai hệ thống (1.5 phút)
**Lời thoại:**
"Về phương diện triển khai công nghệ, hệ thống sử dụng SQLite để quản trị cơ sở dữ liệu. Việc này hỗ trợ phương pháp lưu trữ bộ nhớ đệm (caching): Nghĩa là, nếu một URL đã từng được phân tích, hệ thống sẽ truy xuất lại kết quả ngay lập tức mà không cần gọi lại mô hình học sâu.
Đồng thời, kiến trúc xử lý bất đồng bộ (Asynchronous) của FastAPI giúp hệ thống điều phối song song các truy vấn một cách mượt mà, đáp ứng tốt tiêu chuẩn của một hệ thống thời gian thực."

---

### Slide 10: Giao diện trực quan của hệ thống (1.5 phút)
**Lời thoại:**
*(Chỉ tay minh họa các vùng trên giao diện kết quả)*
"Giao diện người dùng được thiết kế tối giản. Thay vì thao tác nhập liệu phức tạp, người dùng chỉ cần cung cấp URL bài báo.
Sau vài giây, kết quả được hiển thị qua hai phân hệ:
Phần trên hiển thị Nhãn cảnh báo và Điểm số tin cậy kết hợp cùng mã màu trực quan.
Phần dưới là **Động cơ Giải thích**. Hệ thống tự động biên dịch các dấu hiệu rủi ro thành các câu văn rõ ràng, minh bạch hóa hoàn toàn cơ sở ra quyết định của mô hình."

---

### Slide 11: Cơ chế Heuristic Explanation (1.5 phút)
**Lời thoại:**
*(Chỉ tay vào các module trong sơ đồ Heuristic)*
"Đóng góp trọng tâm về thuật toán của đề tài nằm ở Cơ chế **Heuristic Explanation**. 
Được thiết kế theo phương pháp giải thích hậu xử lý (Post-hoc), cơ chế này hoạt động độc lập và không can thiệp vào không gian vector của PhoBERT. 
Hệ thống sử dụng các bộ quy tắc để bóc tách các đặc trưng hình thức phổ biến của tin giả như: lạm dụng ký tự viết hoa, bất thường về dấu câu, hoặc dùng từ ngữ mang tính kích động.
Việc tách biệt rõ ràng giữa chức năng 'Phân loại' của PhoBERT và chức năng 'Giải thích' của Heuristic giúp hệ thống duy trì được độ trễ cực thấp ở mức mili-giây."

---

### Slide 12: Kết quả thực nghiệm (1.5 phút)
**Lời thoại:**
"Trong phần thực nghiệm trên tập Test độc lập, mô hình đạt độ chính xác (Accuracy) 96.32%. 
Tuy nhiên, do tập dữ liệu thực tế luôn mất cân bằng (Imbalanced Data) — số lượng văn bản an toàn chiếm ưu thế, em sử dụng chỉ số **F1-Score** làm thước đo chính.
Mô hình đạt F1-Score 93.42%. Kết quả này khẳng định năng lực phát hiện tin giả một cách ổn định, đạt sự cân bằng tối ưu giữa độ chuẩn xác và độ bao phủ."

---

### Slide 13: Phân tích và đánh giá kết quả (1.5 phút)
**Lời thoại:**
"Từ kết quả trên, em rút ra hai đánh giá quan trọng:
Thứ nhất, phân tích ma trận nhầm lẫn cho thấy hệ thống đã kiểm soát tỷ lệ Âm tính giả (False Negative - bỏ lọt tin giả) ở mức rất thấp. Đây là yếu tố then chốt khẳng định tính an toàn của hệ thống.
Thứ hai, Cơ chế Heuristic hoạt động với độ phức tạp thuật toán O(N), giúp giải quyết hiệu quả bài toán đánh đổi giữa Tính minh bạch và Chi phí tính toán. Hệ thống vừa cung cấp diễn giải chi tiết, vừa đảm bảo thời gian phản hồi dưới 1 giây."

---

### Slide 14: Hạn chế (1.5 phút)
**Lời thoại:**
"Kính thưa Hội đồng, dưới lăng kính khoa học, hệ thống hiện tại vẫn ghi nhận một số giới hạn:
Giới hạn thứ nhất là rủi ro 'Dương tính giả' (False Positive). Do nhạy cảm với các từ khóa mạnh, mô hình đôi khi cảnh báo nhầm các bài báo hình sự, pháp luật chính thống.
Giới hạn thứ hai xuất phát từ việc hệ thống hiện chỉ tập trung phân tích **văn phong học (Stylometry)** mà chưa có năng lực đối chiếu sự kiện thực tế (Fact-checking). Do đó, những văn bản giả mạo số liệu nhưng viết với văn phong chuẩn mực vẫn có nguy cơ vượt qua bộ lọc."

---

### Slide 15: Kết luận và hướng phát triển (1 phút)
**Lời thoại:**
"Tóm lại, đề tài đã thành công trong việc xây dựng một hệ thống khép kín, ứng dụng mô hình PhoBERT kết hợp cơ chế giải thích Heuristic để nhận diện tin giả với độ tin cậy cao và tốc độ ưu việt.
Trong tương lai, hướng phát triển cốt lõi là tích hợp Tri thức đồ thị (Knowledge Graph) và cơ chế RAG nhằm bổ sung năng lực kiểm chứng sự kiện thực tế bằng các nguồn báo chí chính thống."

---

### Slide 16: DEMO Hệ thống thực tế (2-3 phút)
**Lời thoại:**
"Sau đây, em xin phép được trình diễn trực tiếp hệ thống ShieldAI. Em sẽ thực hiện kiểm duyệt hai mẫu dữ liệu: một đường dẫn báo chính thống và một văn bản mạo danh trên mạng xã hội, để Hội đồng quan sát trực quan tốc độ phản hồi và năng lực giải thích của mô hình."
*(Thực hiện thao tác Demo)*

---

### Slide 17: Lời cảm ơn (0.5 phút)
**Lời thoại:**
"Phần trình bày tiểu luận của em đến đây là kết thúc. Em xin trân trọng cảm ơn quý Thầy Cô trong Hội đồng đã lắng nghe. Em rất mong nhận được những góp ý và câu hỏi phản biện từ Hội đồng để nghiên cứu được hoàn thiện hơn ạ."

---

### 💡 Ngân hàng Câu hỏi Phản biện (Q&A) - Tối ưu cho phản xạ giao tiếp:

- **"Tại sao đề tài không sử dụng các thuật toán giải thích chuyên sâu như SHAP hay LIME?"**
  *Trả lời:* Kính thưa Thầy/Cô, việc áp dụng SHAP hoặc LIME yêu cầu sinh nhiễu và chạy lại mô hình hàng nghìn lần. Chi phí tính toán khổng lồ đó sẽ đẩy độ trễ lên tới 10-30 giây, vi phạm ràng buộc thời gian thực (real-time) của API. Cơ chế Heuristic độc lập của em đáp ứng được yêu cầu minh bạch bề mặt (Post-hoc Global Explanation) nhưng chỉ mất vài mili-giây.

- **"Tại sao sử dụng F1-Score làm độ đo chính thay vì Accuracy?"**
  *Trả lời:* Dạ thưa Hội đồng, do đặc thù phân phối của dữ liệu tin tức luôn ở trạng thái mất cân bằng (Imbalanced Data), lượng tin thật luôn nhiều hơn tin giả. Trong trường hợp này, Accuracy có thể bị ảo và thiên lệch về nhãn đa số. F1-Score, là trung bình điều hòa của Precision và Recall, giúp phản ánh khách quan năng lực "bắt đúng tin giả" của mô hình.

- **"Bản chất Heuristic chỉ là đánh giá theo luật (If-Else), vậy Trí tuệ Nhân tạo thực sự nằm ở đâu?"**
  *Trả lời:* Kính thưa Thầy/Cô, chức năng phân loại cốt lõi và sự thấu hiểu ngữ nghĩa đa chiều hoàn toàn do bộ não học sâu PhoBERT đảm nhiệm. Heuristic chỉ đóng vai trò là một module hỗ trợ hậu xử lý (Post-hoc module). Sự kết hợp này là kiến trúc thực dụng nhằm dung hòa sự đánh đổi: Ta dùng AI phức tạp (PhoBERT) để lấy kết quả chuẩn, và dùng phương pháp truyền thống (Heuristic) để diễn giải với tốc độ nhanh nhất.
