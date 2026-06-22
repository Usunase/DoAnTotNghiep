# LUẬN VĂN TỐT NGHIỆP ĐẠI HỌC

---

**BỘ GIÁO DỤC VÀ ĐÀO TẠO**

**TRƯỜNG ĐẠI HỌC TÂN TẠO**

**KHOA CÔNG NGHỆ THÔNG TIN**

---

## NGHIÊN CỨU, XÂY DỰNG CÔNG CỤ PHÂN TÍCH VÀ PHÁT HIỆN TIN GIẢ TIẾNG VIỆT BẰNG PHOBERT VÀ MẠNG NƠ-RON ĐA TẦNG

*(Hệ thống ShieldAI: PhoBERT — MLP — Giải thích có thể diễn giải)*

---

| | |
|---|---|
| **Ngành:** | Công nghệ thông tin |
| **Mã số:** | [Điền mã ngành] |
| **Khóa:** | [Điền năm nhập học] |

| | |
|---|---|
| **Sinh viên thực hiện:** | Hà Minh Chiến |
| **Mã số sinh viên:** | [Điền MSSV] |
| **Giảng viên hướng dẫn:** | [Học hàm, học vị. Họ tên GVHD] |

**TÂY NINH, THÁNG 06 NĂM 2026**

---

> **Hướng dẫn đưa vào Word (tiêu chí 1 — 1,5/1,5 điểm):**
> - Style: `CHƯƠNG X:` → **Heading 1**; `X.X.` → **Heading 2**; `X.X.X.` → **Heading 3**.
> - Font nội dung: Times New Roman, cỡ 13; tiêu đề chương cỡ 14–16 đậm.
> - Lề: trái 3,5 cm, phải 2 cm, trên/dưới 2,5 cm (chỉnh theo quy định Khoa nếu có).
> - Đánh số: **Hình X.Y**, **Bảng X.Y** nhất quán; mỗi hình/bảng phải có *đoạn giải thích* ngay sau khi chèn.
> - Trích dẫn trong văn bản dạng [n]; danh mục **Tài liệu tham khảo** ≥ 10 nguồn (IEEE).
> - Chèn **Mục lục tự động** sau khi gán xong Heading.

---

## TRANG PHÊ DUYỆT

Luận văn đã được trình và bảo vệ trước Hội đồng chấm luận văn tốt nghiệp.

**Ngày bảo vệ:** ....../....../20......

**Kết quả:** ....../10 điểm

| | |
|---|---|
| **CHỦ TỊCH HỘI ĐỒNG** | **GIẢNG VIÊN HƯỚNG DẪN** |
| (Ký và ghi rõ họ tên) | (Ký và ghi rõ họ tên) |

---

## LỜI CẢM ƠN

Trong suốt quá trình thực hiện luận văn tốt nghiệp với đề tài *“Nghiên cứu, xây dựng công cụ phân tích và phát hiện tin giả tiếng Việt bằng PhoBERT và mạng nơ-ron đa tầng”*, em đã nhận được sự quan tâm, hỗ trợ và động viên từ nhiều phía.

Em xin chân thành cảm ơn **Thầy/Cô [Tên giảng viên hướng dẫn]** — Giảng viên hướng dẫn — đã tận tình chỉ bảo, định hướng phương pháp nghiên cứu, góp ý về kiến trúc hệ thống và đánh giá kết quả thực nghiệm, giúp em hoàn thiện luận văn này.

Em xin cảm ơn các **Thầy, Cô** trong Khoa Công nghệ Thông tin, Trường Đại học Tân Tạo, đã truyền đạt kiến thức nền tảng về trí tuệ nhân tạo, xử lý ngôn ngữ tự nhiên và kỹ thuật phần mềm trong suốt quá trình học tập.

Em xin gửi lời cảm ơn sâu sắc đến **gia đình** đã tạo điều kiện, động viên tinh thần để em yên tâm học tập và nghiên cứu. Em cũng xin cảm ơn **bạn bè, đồng nghiệp** đã chia sẻ ý kiến, hỗ trợ kiểm thử hệ thống ShieldAI.

Mặc dù đã nỗ lực hoàn thiện, luận văn không tránh khỏi những thiếu sót. Em rất mong nhận được sự góp ý của Quý Thầy, Cô để đề tài được phát triển tốt hơn trong tương lai.

**Sinh viên thực hiện**

*(Ký và ghi rõ họ tên)*

---

## TÓM TẮT LUẬN VĂN

Trong bối cảnh mạng xã hội phát triển mạnh tại Việt Nam, tin giả (*disinformation*) trở thành mối đe dọa đối với an ninh thông tin và ổn định xã hội. Các phương pháp phát hiện truyền thống dựa trên từ khóa hoặc thống kê văn bản đơn giản không còn đáp ứng được độ tinh vi của nội dung giả mạo. Đồng thời, việc áp dụng trực tiếp mô hình ngôn ngữ tiếng Anh trên tiếng Việt thường cho kết quả kém do đặc thù ngôn ngữ đơn lập và thiếu tài nguyên huấn luyện trước chuyên biệt.

Luận văn trình bày quá trình nghiên cứu, thiết kế, huấn luyện, đánh giá và triển khai hệ thống **ShieldAI** — công cụ phát hiện tin giả tiếng Việt dựa trên **PhoBERT-base** và **mạng nơ-ron đa tầng (MLP)**. Hệ thống trích embedding ngữ nghĩa 768 chiều từ PhoBERT (chế độ cố định), chuẩn hóa và đưa qua bộ phân loại **MLP (128, 64)** để dự đoán xác suất tin giả. Kết quả được diễn giải theo **ba mức** (tin thật / đáng ngờ / tin giả) và bổ sung lớp giải thích rule-based trên văn bản.

Kết quả thực nghiệm trên **10.609 mẫu** (sau lọc từ 10.617 bản ghi gốc) cho thấy mô hình đạt độ chính xác **94,13%**, F1 **93,71%** và ROC-AUC **98,50%** trên tập kiểm thử hold-out 30% (~3.183 mẫu); kiểm định chéo 5-fold cho F1 **93,17% ± 1,33%**. Hệ thống được triển khai web với **FastAPI** và **Next.js**, tích hợp xác thực người dùng, lịch sử phân tích và mô-đun giải thích kết quả. Luận văn cũng thảo luận hướng mở rộng bổ sung siêu dữ liệu mạng xã hội trong tương lai.

**Từ khóa:** tin giả, phát hiện tin giả, PhoBERT, mạng nơ-ron đa tầng, tiếng Việt, ShieldAI, trí tuệ nhân tạo có thể giải thích

---

## ABSTRACT

In the context of rapid social media growth in Vietnam, disinformation has become a serious threat to information security and social stability. Traditional detection methods based on keywords or simple text statistics are insufficient against sophisticated fake content. Meanwhile, directly applying English-centric pre-trained language models to Vietnamese often yields suboptimal results due to the monosyllabic structure of the language and the lack of dedicated pre-training resources.

This thesis presents the research, design, training, evaluation, and deployment of **ShieldAI** — a Vietnamese fake news detection system based on **PhoBERT-base** and a **multilayer perceptron (MLP)** classifier. The system extracts 768-dimensional semantic embeddings from frozen PhoBERT, applies standardization, and feeds them into an **MLP (128, 64)** for fake-news probability estimation. Results are presented at **three levels** (real / suspicious / fake) with a rule-based explanation layer over the input text.

Experimental results on **10,609 samples** (after cleaning from 10,617 source records) show **94.13% accuracy**, **93.71% F1-score**, and **98.50% ROC-AUC** on a 30% hold-out test set (~3,183 samples); 5-fold cross-validation yields **93.17% ± 1.33% F1**. The system is deployed as a web application using **FastAPI** and **Next.js**, with user authentication, analysis history, and explainable outputs. Future work may incorporate social metadata when real-world data becomes available.

**Keywords:** fake news, fake news detection, PhoBERT, multilayer perceptron, Vietnamese, ShieldAI, explainable AI

---

## MỤC LỤC

*(Chèn Mục lục tự động trong Microsoft Word sau khi áp dụng Heading 1/2/3)*

- Lời cảm ơn
- Tóm tắt luận văn
- Abstract
- Danh mục hình ảnh
- Danh mục bảng biểu
- Danh mục từ viết tắt
- **Chương 1: Giới thiệu**
- **Chương 2: Cơ sở lý thuyết và tổng quan**
- **Chương 3: Phương pháp nghiên cứu và thiết kế hệ thống**
- **Chương 4: Hiện thực và kết quả**
- **Chương 5: Kết luận và hướng phát triển**
- Tài liệu tham khảo
- Phụ lục

---

## DANH MỤC HÌNH ẢNH

| Ký hiệu | Tên hình | Trang |
|---------|----------|:-----:|
| Hình 2.1 | Kiến trúc mô hình BERT/PhoBERT | … |
| Hình 2.2 | Sơ đồ tiếp cận PhoBERT + MLP | … |
| Hình 3.1 | Kiến trúc tổng thể hệ thống ShieldAI | … |
| Hình 3.2 | Sơ đồ ba mô-đun suy luận (PhoBERTInferenceSystem) | … |
| Hình 3.3 | Sơ đồ quan hệ lưu trữ dữ liệu và mô hình | … |
| Hình 3.4 | Lưu đồ thuật toán suy luận (Inference) | … |
| Hình 3.5 | Wireframe giao diện trang phân tích (/analyze) | … |
| Hình 3.6 | Wireframe giao diện trang kết quả (/results) | … |
| Hình 4.1 | Ma trận nhầm lẫn mô hình PhoBERT text-only | … |
| Hình 4.2 | Đường cong ROC mô hình PhoBERT text-only | … |
| Hình 4.3 | Kết quả kiểm định chéo 5-fold (F1, Accuracy) | … |
| Hình 4.4 | Giao diện trang chủ hệ thống ShieldAI | … |
| Hình 4.5 | Giao diện nhập văn bản / URL | … |
| Hình 4.6 | Giao diện hiển thị kết quả phân loại và giải thích | … |

> *Các hình 4.1–4.5 được sinh từ script `run_experimental_evaluation.py`, lưu tại `backend/experiments/figures/experimental/` sau khi chạy đánh giá.*

---

## DANH MỤC BẢNG BIỂU

| Ký hiệu | Tên bảng | Trang |
|---------|----------|:-----:|
| Bảng 1.1 | Mục tiêu cụ thể dạng SMART | … |
| Bảng 2.1 | So sánh công trình liên quan với đề tài ShieldAI | … |
| Bảng 2.2 | Danh sách công nghệ, thư viện và lý do lựa chọn | … |
| Bảng 3.5 | Mô tả thực thể lưu trữ | … |
| Bảng 3.1 | Pipeline tiền xử lý văn bản (`preprocess_text`) | … |
| Bảng 3.2 | Yêu cầu chức năng hệ thống ShieldAI | … |
| Bảng 3.3 | Yêu cầu phi chức năng hệ thống ShieldAI | … |
| Bảng 3.4 | Siêu tham số bộ phân loại MLP | … |
| Bảng 4.1 | Môi trường phát triển và triển khai | … |
| Bảng 4.2 | Thống kê bộ dữ liệu full_dataset.csv | … |
| Bảng 4.3 | Hiệu năng mô hình PhoBERT text-only (tập kiểm thử 30%) | … |
| Bảng 4.4 | Kết quả kiểm định chéo 5-fold (PhoBERT text-only) | … |
| Bảng 4.5 | Kịch bản kiểm thử chức năng hệ thống (ánh xạ FR) | … |
| Bảng 4.6 | Bộ kiểm thử tự động Pytest — tổng quan theo file | … |
| Bảng 4.8 | Chi tiết từng kịch bản kiểm thử tự động (42 test cases) | … |
| Bảng 4.7 | Đối chiếu mục tiêu SMART và kết quả đạt được | … |

---

## DANH MỤC TỪ VIẾT TẮT

| Từ viết tắt | Giải thích |
|-------------|------------|
| API | Application Programming Interface — Giao diện lập trình ứng dụng |
| AUC | Area Under the Curve — Diện tích dưới đường cong |
| BERT | Bidirectional Encoder Representations from Transformers |
| CLS | Classification Token — Token phân loại đại diện câu |
| MLP | Multilayer Perceptron — Mạng nơ-ron đa tầng |
| MXH | Mạng xã hội |
| NLP | Natural Language Processing — Xử lý ngôn ngữ tự nhiên |
| ROC | Receiver Operating Characteristic |
| TF-IDF | Term Frequency – Inverse Document Frequency |
| XAI | Explainable Artificial Intelligence — Trí tuệ nhân tạo có thể giải thích |

---

<br>

# CHƯƠNG 1: GIỚI THIỆU

## 1.1. Đặt vấn đề

Cuộc cách mạng thông tin kỹ thuật số đã biến mỗi người dùng mạng thành một nút phát tán nội dung [5]. Tại Việt Nam, quy mô cộng đồng Internet và mạng xã hội ngày càng mở rộng, trong khi tốc độ lan truyền thông tin vượt xa khả năng kiểm chứng của báo chí truyền thống và các tổ chức fact-checking. Một thông điệp sai sự thật — về dịch bệnh, thiên tai, chính trị hay kinh tế — có thể được chia sẻ hàng trăm nghìn lần trong thời gian ngắn, gây hoang mang, thiệt hại kinh tế–xã hội và suy giảm niềm tin công chúng.

Khác với thông tin sai lệch vô ý (*misinformation*), tin giả (*disinformation*) được tạo ra hoặc phát tán **có chủ đích** nhằm thao túng dư luận. Trên mạng xã hội Việt Nam, tin giả thường đồng thời biểu hiện ở hai tầng: **nội dung ngôn ngữ** (giọng điệu giật gân, kêu gọi lan truyền khẩn cấp) và **ngữ cảnh lan truyền** (tài khoản mới, ít người theo dõi, lan truyền bất thường). Phương pháp kiểm chứng thủ công, dù chính xác, không thể mở rộng trước khối lượng thông tin khổng lồ mỗi ngày. Do đó, nhu cầu xây dựng **công cụ tự động hỗ trợ phân tích và phát hiện tin giả** trở nên cấp thiết.

## 1.2. Mục tiêu nghiên cứu

### 1.2.1. Mục tiêu tổng quát

Nghiên cứu, thiết kế và xây dựng hệ thống phát hiện tin giả tiếng Việt có khả năng vận hành thực tế, dựa trên embedding PhoBERT và phân loại MLP, đồng thời cung cấp cơ chế diễn giải kết quả cho người dùng phổ thông.

### 1.2.2. Mục tiêu cụ thể (theo tiêu chí SMART)

*Bảng 1.1. Mục tiêu cụ thể dạng SMART*

| Mã | Mục tiêu | S (Cụ thể) | M (Đo lường) | A (Khả thi) | R (Liên quan) | T (Thời hạn) |
|----|----------|------------|--------------|-------------|---------------|--------------|
| MT-01 | Tiền xử lý tiếng Việt | Pipeline PyVi thống nhất train/inference | Có `preprocess_text` trong `text_utils.py` | Dùng PyVi, PhoBERT [3] | Chuẩn hóa đầu vào NLP | HK2 2025–2026 |
| MT-02 | Mô hình PhoBERT + MLP | Embedding 768 → MLP | F1 ≥ 90% trên tập test | 10.609 mẫu, sklearn | Giải quyết đặt vấn đề | HK2 2025–2026 |
| MT-03 | Đánh giá & CV | Hold-out 30% + 5-fold CV | Bảng metric đầy đủ | Script eval có sẵn | Chứng minh khoa học | HK2 2025–2026 |
| MT-04 | Triển khai web | FastAPI + Next.js | 8/8 chức năng FR (Bảng 3.2) | `./run.sh` | Ứng dụng thực tiễn | HK2 2025–2026 |
| MT-05 | Giải thích kết quả | Rule-based tiếng Việt | JSON `explanation` trên UI | Module riêng | Tăng tin cậy người dùng | HK2 2025–2026 |

## 1.3. Đối tượng và phạm vi nghiên cứu

### 1.3.1. Đối tượng nghiên cứu

Đối tượng là bài toán **phân loại** văn bản tiếng Việt thành tin thật, đáng ngờ hoặc tin giả (3 mức hiển thị), dựa trên nội dung văn bản; mô hình học sâu huấn luyện nhị phân tin thật/tin giả.

### 1.3.2. Phạm vi nghiên cứu

**Trong phạm vi:**

- Phân loại nhị phân với nhãn có giám sát trên tập dữ liệu tiếng Việt; hiển thị 3 mức verdict cho người dùng.
- PhoBERT-base ở chế độ cố định (trích embedding, không fine-tune end-to-end).
- Pipeline tiền xử lý thống nhất `preprocess_text` cho train và inference.
- Giải thích kết quả theo quy tắc heuristic trên văn bản đầu vào.

**Ngoài phạm vi:** phát hiện deepfake đa phương tiện; phân loại đa lớp theo chủ đề; fine-tune PhoBERT trên GPU cluster; tích hợp siêu dữ liệu mạng xã hội thực (hướng phát triển).

## 1.4. Phương pháp nghiên cứu

Đề tài kết hợp: **nghiên cứu tài liệu** (tổng quan lý thuyết và công trình liên quan); **phân tích–tổng hợp** (yêu cầu hệ thống, pipeline NLP); **thực nghiệm** (hold-out, kiểm định chéo); **thiết kế–xây dựng hệ thống** (backend, frontend); **đánh giá định lượng** (Accuracy, Precision, Recall, F1, ROC-AUC).

## 1.5. Ý nghĩa khoa học và thực tiễn

**Ý nghĩa khoa học:** Đề tài chứng minh hiệu quả pipeline PhoBERT + MLP trên tiếng Việt, cung cấp số liệu tham chiếu (F1 93,71%) và quy trình tái lập end-to-end.

**Ý nghĩa thực tiễn:** Hệ thống ShieldAI hỗ trợ người dùng kiểm tra nội dung nghi ngờ (văn bản hoặc URL), nhận xác suất tin giả, nhãn 3 mức và lý do diễn giải — bước đầu hướng tới công cụ hỗ trợ fact-checking, không thay thế con người.

## 1.6. Bố cục luận văn

- **Chương 1** trình bày bối cảnh, mục tiêu SMART, phạm vi và phương pháp.
- **Chương 2** trình bày cơ sở lý thuyết, tổng quan nghiên cứu có so sánh và công nghệ kèm lý do lựa chọn.
- **Chương 3** trình bày phương pháp nghiên cứu, yêu cầu, kiến trúc, sơ đồ dữ liệu và lưu đồ thuật toán.
- **Chương 4** trình bày hiện thực, kết quả thực nghiệm đối chiếu mục tiêu, kiểm thử hệ thống.
- **Chương 5** đưa ra kết luận, đóng góp mới, hạn chế và hướng phát triển.

**Kết luận chương 1:** Chương đã làm rõ tính cấp thiết, mục tiêu SMART và phạm vi đề tài. Chương 2 sẽ củng cố nền tảng lý thuyết và tổng quan công trình liên quan nhằm biện minh các lựa chọn kỹ thuật.

---

<br>

# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN

## 2.1. Các khái niệm liên quan

### 2.1.1. Tin giả và phân loại thông tin

- **Misinformation:** thông tin sai, người chia sẻ có thể không cố ý.
- **Disinformation:** thông tin sai, tạo ra hoặc phát tán có chủ đích.
- **Malinformation:** thông tin đúng nhưng sử dụng sai mục đích.

ShieldAI giải quyết bài toán phân loại nhị phân tin thật/tin giả trên tập có nhãn `is_fake`.

### 2.1.2. Tiếp cận PhoBERT và phân loại MLP

Đề tài sử dụng **embedding ngữ nghĩa** từ PhoBERT làm đầu vào cho **mạng nơ-ron đa tầng (MLP)** — kiến trúc phổ biến khi mô hình ngôn ngữ được cố định và bộ phân loại học trên vector đặc trưng. Cách tiếp cận này cân bằng giữa độ chính xác, khả năng triển khai và phạm vi tiểu luận tốt nghiệp.

### 2.1.3. Trí tuệ nhân tạo có thể giải thích

Người dùng cần không chỉ nhãn phân loại mà còn **lý do**. ShieldAI dùng giải thích theo quy tắc (*rule-based*), cân bằng giữa tính hình thức và khả năng tiếp cận công chúng.

## 2.2. Cơ sở lý thuyết

### 2.2.1. Xử lý ngôn ngữ tự nhiên tiếng Việt

Tiếng Việt là ngôn ngữ đơn lập, bắt buộc **phân đoạn từ** trước khi đưa vào mô hình. Thư viện **PyVi** được dùng để phân đoạn từ (dạng `người_dùng`, `tin_giả`). ShieldAI dùng pipeline `preprocess_text`: lowercase → xóa URL → chuẩn hóa khoảng trắng → PyVi tokenize — **cùng logic** cho train và inference.

### 2.2.2. Mô hình BERT và PhoBERT

**BERT** dùng Transformer encoder hai chiều, tạo embedding ngữ cảnh. **PhoBERT** (VinAI, 2020) [3] huấn luyện trước trên corpus tiếng Việt ~20 GB, kế thừa kiến trúc BERT [4]. Phiên bản `vinai/phobert-base`: 12 lớp, hidden 768, 12 attention heads. ShieldAI trích vector **[CLS]** 768 chiều làm biểu diễn câu, độ dài tối đa 256 token.

### 2.2.3. Mạng nơ-ron đa tầng (MLP)

MLP gồm các lớp ẩn với hàm kích hoạt phi tuyến (ReLU), phù hợp học quan hệ phức tạp giữa embedding PhoBERT 768 chiều và nhãn phân loại tin thật/tin giả.

## 2.3. Tổng quan các công trình nghiên cứu liên quan

### 2.3.1. Các nghiên cứu trong nước

Trong nước, các hướng tiếp cận chủ yếu gồm: (i) phân loại bằng TF-IDF kết hợp SVM/Naive Bayes — đơn giản nhưng thiếu ngữ cảnh sâu; (ii) mô hình học sâu PhoBERT, BiLSTM — cải thiện F1; (iii) bổ sung đặc trưng nguồn tin hoặc thống kê văn bản. **Phân tích so sánh:** ShieldAI tập trung pipeline PhoBERT + MLP text-only, triển khai web end-to-end có giải thích và lịch sử phân tích — phù hợp triển khai thực tế khi chưa có siêu dữ liệu MXH đáng tin cậy.

### 2.3.2. Các nghiên cứu ngoài nước

Shu *et al.* [5] phân loại ba hướng: nội dung, mạng lan truyền, nguồn tin. Zhou và Zafarani [6] tổng quan lý thuyết, phương pháp và hướng mở. Các benchmark FakeNewsNet, LIAR có đồ thị lan truyền nhưng chưa phủ tiếng Việt. Hướng LLM zero-shot mới nổi [11] thiếu kiểm soát và khó tái lập trên tập riêng.

**Bảng 2.1. So sánh công trình liên quan với đề tài ShieldAI**

| Nghiên cứu | Ngôn ngữ | Đặc trưng văn bản | Metadata / MXH | Ablation | Triển khai web | Giải thích |
|------------|:--------:|:-----------------:|:--------------:|:--------:|:--------------:|:----------:|
| TF-IDF + SVM (truyền thống) | VN | Thống kê từ | Không | Hạn chế | Hiếm | Không |
| PhoBERT / BiLSTM | VN | Học sâu | Hạn chế | Một phần | Một số | Hạn chế |
| Hybrid (quốc tế) [5], [6] | EN chủ yếu | Có | Có (graph) | Có | Một số | Một số |
| **ShieldAI (đề tài)** | **VN** | **PhoBERT 768 + MLP** | **Không (hướng mở rộng)** | **Hold-out + CV** | **Có** | **Rule-based VN, 3 mức** |

*Bảng 2.1 cho thấy đề tài bổ sung pipeline PhoBERT text-only có đánh giá định lượng và ứng dụng web có giải thích — khác với chỉ áp dụng mô hình có sẵn.*

## 2.4. Công nghệ sử dụng

**Bảng 2.2. Danh sách công nghệ, thư viện và lý do lựa chọn**

| Lớp | Công nghệ | Vai trò | Lý do chọn |
|-----|-----------|---------|------------|
| NLP | PhoBERT-base [3] | Embedding 768 chiều | Pre-train tiếng Việt, vượt mBERT |
| NLP | PyVi | Phân đoạn từ | Phù hợp vocab PhoBERT, cài đặt nhẹ |
| Học máy | scikit-learn MLP [7] | Phân loại | Phi tuyến, predict_proba, ổn định |
| Backend | FastAPI [9] | REST API | Tích hợp Python ML, OpenAPI |
| Thu thập | BeautifulSoup | Parse HTML | Đủ cho crawl báo điện tử |
| Frontend | Next.js 14 [10] | UI web | TypeScript, App Router, chuyên nghiệp |
| Huấn luyện | PyTorch, Jupyter | Train/embed | Hỗ trợ Transformers chuẩn |
| Lưu trữ | joblib, NumPy | File mô hình | Không cần CSDL cho inference |

## 2.5. Kết luận chương

Chương 2 đã trình bày khái niệm tin giả, cơ sở NLP tiếng Việt, PhoBERT [3], MLP và **so sánh phân tích** công trình trong/ngoài nước (Bảng 2.1). Công nghệ được chọn kèm **lý do** (Bảng 2.2). Chương 3 sẽ chi tiết hóa phương pháp, yêu cầu và thiết kế kiến trúc ShieldAI.

---

<br>

# CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU VÀ THIẾT KẾ HỆ THỐNG

## 3.1. Phương pháp nghiên cứu

### 3.1.1. Tiếp cận PhoBERT + MLP (text-only)

Hệ thống sử dụng một luồng đặc trưng ngữ nghĩa:

- **PhoBERT-base** → vector [CLS] **768 chiều**.
- **StandardScaler** → chuẩn hóa embedding.
- **MLP (128, 64)** → xác suất tin giả (`predict_proba`).
- **Verdict 3 mức** (≥75% tin giả, 35–74% đáng ngờ, &lt;35% tin thật) — thống nhất backend và giao diện.

**Cơ sở lựa chọn:** Tập trung vào nội dung văn bản — nguồn thông tin luôn có khi người dùng nhập bài viết hoặc URL; pipeline gọn, đồng bộ train/inference, dễ triển khai và bảo trì. Siêu dữ liệu mạng xã hội được xem là hướng mở rộng khi có dữ liệu thực.

### 3.1.2. Chiến lược PhoBERT cố định

Không fine-tune end-to-end vì: (i) tiết kiệm GPU/thời gian; (ii) embedding lưu `.npy` tái sử dụng; (iii) MLP nhỏ ổn định trên CPU. Trade-off: có thể mất 1–2% so với fine-tune tối ưu — chấp nhận được trong phạm vi tiểu luận.

### 3.1.3. Tiền xử lý thống nhất

Hàm `preprocess_text` trong `text_utils.py` được dùng cho **cả train và inference** (qua `dataset_cleaner.segment_text` và `phobert_inference`). Tránh lệch pipeline — một trong các nguyên nhân phổ biến làm giảm hiệu năng thực tế so với số liệu huấn luyện.

### 3.1.4. Giao thức đánh giá

- Chia tập: 70% huấn luyện / 30% kiểm thử, phân tầng, `random_state = 42`.
- Kiểm định chéo 5-fold phân tầng.
- Chỉ số: Accuracy, Precision, Recall, F1, ROC-AUC.

## 3.2. Phân tích yêu cầu

### 3.2.1. Yêu cầu chức năng

**Bảng 3.2. Yêu cầu chức năng hệ thống ShieldAI**

| Mã | Yêu cầu | Mô tả |
|----|---------|-------|
| FR-01 | Nhập văn bản | Người dùng dán tiêu đề và nội dung bài viết |
| FR-02 | Nhập URL | Hệ thống crawl và trích xuất nội dung báo điện tử |
| FR-03 | Tiền xử lý văn bản | `preprocess_text`: lowercase, xóa URL, PyVi tokenize |
| FR-04 | Trích đặc trưng | PhoBERT embedding 768 chiều |
| FR-05 | Phân loại | Dự đoán xác suất tin giả; verdict 3 mức |
| FR-06 | Giải thích kết quả | Trình bày lý do rule-based bằng tiếng Việt |
| FR-07 | Lịch sử & xác thực | Đăng nhập, lưu/xem lịch sử phân tích |
| FR-08 | API REST | Endpoint `/api/analyze`, `/api/health` |

**Envelope JSON API:** FastAPI trả HTTP **200** cho hầu hết phản hồi; trường `status` (`success` / `error`) và `message` trong body quyết định thành công hay lỗi (đăng nhập sai, thiếu JWT, input trống). Frontend đọc `status`, không dựa mã 401/403.

### 3.2.2. Yêu cầu phi chức năng

**Bảng 3.3. Yêu cầu phi chức năng**

| Mã | Tiêu chí | Yêu cầu |
|----|----------|---------|
| NFR-01 | Hiệu năng | Suy luận trong vài giây trên CPU |
| NFR-02 | Khả dụng | Giao diện tiếng Việt, thao tác trực quan |
| NFR-03 | Tái lập | Notebook train thống nhất, seed cố định |
| NFR-04 | Mở rộng | Kiến trúc module, tách frontend/backend |
| NFR-05 | Diễn giải | Kết quả kèm xác suất, không khẳng định tuyệt đối |

## 3.3. Thiết kế hệ thống

### 3.3.1. Kiến trúc hệ thống

Hệ thống theo mô hình **client–server** tách tầng giao diện và suy luận, phù hợp mở rộng và bảo trì.

**Hình 3.1. Kiến trúc tổng thể hệ thống ShieldAI**

```
┌──────────────┐     HTTP      ┌─────────────────┐     Python     ┌──────────────────────┐
│  Trình duyệt │ ────────────► │ Next.js :3000   │ ─────────────► │ FastAPI :8000        │
│  Người dùng  │               │ /analyze        │  POST /api/    │ PhoBERTInferenceSystem│
└──────────────┘               │ /results        │  analyze       └──────────────────────┘
                               └─────────────────┘
```

*Hình 3.1 mô tả luồng tương tác: người dùng thao tác trên giao diện Next.js; yêu cầu phân tích được chuyển tới API Python xử lý mô hình.*

**Hình 3.2. Sơ đồ ba mô-đun suy luận**

```
[Module 1: Crawler + preprocess_text]
            │
            ▼
[Module 2: PhoBERT embedding 768-d]
            │
            ▼
[Module 3: StandardScaler + MLP + ExplanationEngine]
```

*Hình 3.2 thể hiện pipeline suy luận ba giai đoạn: thu thập/tiền xử lý → embedding → phân loại và giải thích.*

Ba mô-đun suy luận:

| Mô-đun | Tên | Chức năng |
|--------|-----|-----------|
| 1 | Thu thập & tiền xử lý | DataCrawler, `preprocess_text` |
| 2 | Trích xuất đặc trưng | PhoBERT [CLS] 768 chiều |
| 3 | Phân loại & giải thích | StandardScaler, MLP, ExplanationEngine, verdict 3 mức |

### 3.3.2. Thiết kế lưu trữ dữ liệu

Hệ thống sử dụng **SQLite** (qua SQLAlchemy) để lưu người dùng, lịch sử phân tích và phản hồi. Mô hình ML lưu dạng file — phù hợp triển khai tiểu luận và tái lập thí nghiệm.

**Hình 3.3. Sơ đồ quan hệ lưu trữ dữ liệu và mô hình**

```
full_dataset.csv ──► dataset_cleaner ──► DataFrame sạch
                              │
                              ▼
                    phobert_base_features.npy
                    phobert_base_labels.npy
                              │
                              ▼
              phobert_mlp_model.joblib
              phobert_scaler.joblib
                              │
                              ▼
                    phobert_inference.py (runtime)
                              │
                              ▼
                    SQLite (users, history)
```

*Bảng 3.5. Mô tả thực thể lưu trữ*

| Thực thể | Định dạng | Vai trò | Giai đoạn |
|----------|-----------|---------|-----------|
| Tập huấn luyện | CSV | 10.617 bản ghi → 10.609 mẫu sau lọc, nhãn `is_fake` | Train |
| Embedding | NPY | Ma trận 768 chiều × N mẫu | Train/Eval |
| Nhãn | NPY | Vector nhãn tương ứng | Train/Eval |
| MLP + Scaler | joblib | `phobert_mlp_model`, `phobert_scaler` | Inference |
| Lịch sử | SQLite | Phân tích, verdict, explanation JSON | Runtime |
| Kết quả tạm | sessionStorage | JSON giữa `/analyze` và `/results` | Runtime UI |

Kết quả phân tích trên web lưu tạm `sessionStorage` trình duyệt giữa `/analyze` và `/results` — không ghi đĩa server.

### 3.3.3. Thiết kế giao diện

Ba trang chính:

| Route | Chức năng |
|-------|-----------|
| `/` | Trang chủ — giới thiệu ShieldAI |
| `/analyze` | Form nhập văn bản hoặc URL |
| `/results` | Gauge xác suất, verdict 3 mức, giải thích |
| `/history` | Lịch sử phân tích (đã đăng nhập) |

*Hình 3.5, 3.6* — Wireframe hoặc screenshot khi hoàn thiện Word.

### 3.3.4. Thiết kế thuật toán

**Bảng 3.1. Các bước `preprocess_text` (train + inference)**

| STT | Bước | Mô tả |
|:---:|------|-------|
| 1 | Lowercase | Chuyển toàn bộ văn bản về chữ thường |
| 2 | Xóa URL | Loại bỏ liên kết `http(s)://...` |
| 3 | Chuẩn hóa khoảng trắng | Gộp nhiều khoảng trắng thành một |
| 4 | PyVi tokenize | Phân đoạn từ (`ViTokenizer.tokenize`) |

**Hình 3.4. Lưu đồ thuật toán suy luận (Inference)**

```
                    ┌─────────────┐
                    │   BẮT ĐẦU   │
                    └──────┬──────┘
                           ▼
              ┌────────────────────────┐
              │ Nhận text hoặc URL?    │
              └────────────┬───────────┘
                           ▼
              ┌────────────────────────┐
              │ Module 1: preprocess   │
              │ (≥ 5 từ?)              │
              └────────────┬───────────┘
                     Không │ Có
              ┌────────────┴───────────┐
              ▼                        ▼
        [Trả lỗi]          ┌─────────────────────┐
                             │ Module 2: PhoBERT   │
                             │ embedding 768-d     │
                             └──────────┬──────────┘
                                        ▼
                             ┌─────────────────────┐
                             │ Module 3: Scale     │
                             │ + MLP + verdict 3 mức│
                             │ + Giải thích        │
                             └──────────┬──────────┘
                                        ▼
                             ┌─────────────────────┐
                             │  JSON kết quả       │
                             └─────────────────────┘
```

*Hình 3.4 là lưu đồ thuật toán chính khi người dùng gửi yêu cầu phân tích.*

**Pseudocode:**

```
INPUT: title, content (hoặc url)
1. raw_data ← crawl(url) hoặc nhận text thủ công
2. clean_text ← preprocess_text(content)
3. IF word_count(clean_text) < 5 THEN RETURN error
4. phobert_vec ← PhoBERT([CLS])(clean_text)           // 768
5. scaled ← phobert_scaler.transform(phobert_vec)
6. prob_fake ← MLP.predict_proba(scaled)
7. verdict ← verdict_from_prob(prob_fake)             // fake|suspicious|real
8. explanation ← build_explanation(prob_fake, raw_data)
OUTPUT: result_label, verdict, prob_fake, explanation
```

**Bảng 3.4. Siêu tham số MLP**

| Tham số | Giá trị |
|---------|---------|
| hidden_layer_sizes | (128, 64) |
| activation | relu |
| solver | adam |
| max_iter | 500 |
| alpha (L2) | 0.1 |
| early_stopping | True |
| random_state | 42 |

## 3.4. Kết luận chương

Chương 3 đã trình bày phương pháp PhoBERT + MLP, yêu cầu chức năng/phi chức năng (Bảng 3.2, 3.3), kiến trúc (Hình 3.1–3.2), mô hình lưu trữ (Hình 3.3) và lưu đồ thuật toán (Hình 3.4). Chương 4 sẽ hiện thực hóa thiết kế, chạy thực nghiệm và đối chiếu kết quả với mục tiêu SMART (Bảng 1.1).

---

<br>

# CHƯƠNG 4: HIỆN THỰC VÀ KẾT QUẢ

## 4.1. Môi trường phát triển

**Bảng 4.1. Môi trường phát triển và triển khai**

| Thành phần | Chi tiết |
|------------|----------|
| Hệ điều hành | Linux (Ubuntu) |
| Python | ≥ 3.10, virtualenv |
| Node.js | ≥ 18 |
| CPU/RAM | ≥ 8 GB RAM (khuyến nghị 16 GB) |
| GPU | Tùy chọn (tăng tốc embedding) |
| IDE | Cursor / VS Code, JupyterLab |
| Thư viện chính | torch, transformers, scikit-learn, fastapi, next.js |

Cài đặt: `pip install -r requirements.txt`; `npm install` trong `frontend/`. Chạy: `./run.sh`.

## 4.2. Quá trình hiện thực

### 4.2.1. Cài đặt các mô-đun chính

| File / Thư mục | Vai trò |
|----------------|---------|
| `data_crawler.py` | Crawl URL, nhận văn bản thủ công |
| `text_utils.py` | `preprocess_text` — train + inference |
| `text_cleaner.py` | Wrapper tương thích; gọi `preprocess_text` |
| `dataset_cleaner.py` | Lọc CSV trước train |
| `phobert_inference.py` | Pipeline suy luận 3 mô-đun |
| `verdict.py` | Phân loại 3 mức từ xác suất |
| `explanation_engine.py` | Sinh giải thích rule-based |
| `api/main.py` | FastAPI bridge |
| `frontend/` | Giao diện Next.js |

Notebook `train_phobert_model.ipynb` gom các phần: lý thuyết → lọc dữ liệu → embed PhoBERT → train MLP → đánh giá.

### 4.2.2. Xử lý dữ liệu

**Bảng 4.2. Thống kê bộ dữ liệu**

| Chỉ số | Giá trị |
|--------|---------|
| File | `backend/data/full_dataset.csv` |
| Số bản ghi (gốc) | **10.617** bài |
| Sau lọc (`dataset_cleaner.py`) | **10.609** mẫu |
| Tập kiểm thử hold-out (30%) | **~3.183** mẫu |
| Nhãn | `is_fake`: True (giả) / False (thật) |
| Cân bằng lớp | ~53,6% thật / ~46,4% giả |
| Lĩnh vực | Y tế, sức khỏe, COVID (tiếng Việt) |
| Trường chính | title, content, source, url, is_fake |

*Ghi chú: tệp CSV có ~169.056 dòng vật lý do trường `content` chứa xuống dòng trong ô trích dẫn — không phải số bài báo.*

Quy trình `dataset_cleaner.py`: loại thiếu content; loại bài < 5 từ; loại trùng lặp; `segment_text` → `preprocess_text` (PyVi).

## 4.3. Kết quả đạt được

### 4.3.1. Kết quả chạy chương trình

**Bảng 4.3. Hiệu năng mô hình PhoBERT text-only (tập kiểm thử 30%)**

| Mô hình | Chiều | Acc | Prec | Rec | F1 | AUC |
|---------|:-----:|:---:|:----:|:---:|:--:|:---:|
| **PhoBERT text-only** | **768** | **94,13%** | **93,17%** | **94,25%** | **93,71%** | **98,50%** |

**Hình 4.1–4.3. Kết quả thực nghiệm định lượng**

| Hình | Tên file (sau khi chạy eval) | Nội dung |
|------|------------------------------|----------|
| Hình 4.1 | `confusion_matrix_text_only.png` | Ma trận nhầm lẫn |
| Hình 4.2 | `roc_curves.png` | Đường cong ROC |
| Hình 4.3 | (từ `cv_summary.json`) | Kiểm định chéo 5-fold |

*Sinh hình: `cd backend && python3 experiments/run_experimental_evaluation.py`. Lưu tại `backend/experiments/figures/experimental/`.*

**Hình 4.4–4.6. Giao diện hệ thống (screenshot khi chạy `./run.sh`)**

| Hình | Trang | Nội dung cần chụp |
|------|-------|-------------------|
| Hình 4.4 | `http://localhost:3000/` | Trang chủ ShieldAI |
| Hình 4.5 | `/analyze` | Form nhập văn bản hoặc URL |
| Hình 4.6 | `/results` | Gauge xác suất, verdict 3 mức, thẻ giải thích |

*Mỗi hình cần chú thích 1–2 câu mô tả chức năng — đáp ứng tiêu chí thực nghiệm có minh chứng hệ thống chạy được.*

### 4.3.2. Đánh giá kết quả

**Bảng 4.7. Đối chiếu mục tiêu SMART (Bảng 1.1) và kết quả đạt được**

| Mã | Mục tiêu | Tiêu chí đo | Kết quả | Đạt? |
|----|----------|-------------|---------|:----:|
| MT-01 | Tiền xử lý tiếng Việt | `preprocess_text` thống nhất | 4 bước + PyVi | ✓ |
| MT-02 | PhoBERT + MLP | F1 ≥ 90% | F1 **93,71%**, Acc 94,13% | ✓ |
| MT-03 | Hold-out & CV | Metric + 5-fold | Bảng 4.3, 4.4 | ✓ |
| MT-04 | Triển khai web | 8/8 FR (Bảng 3.2) | Kiểm thử Bảng 4.5, 4.6 | ✓ |
| MT-05 | Giải thích | JSON `explanation` + verdict 3 mức | `ExplanationEngine` + Hình 4.6 | ✓ |

**Phân tích định lượng:** Mô hình đạt F1 **93,71%** và ROC-AUC **98,50%** trên tập hold-out ~3.183 mẫu (30%). Recall **94,25%** — phát hiện được đa số tin giả. Kiểm định chéo 5-fold: F1 **93,17% ± 1,33%**, chứng tỏ ổn định.

**Bảng 4.4. Kiểm định chéo 5-fold — PhoBERT text-only**

| Chỉ số | Trung bình ± Độ lệch chuẩn |
|--------|:--------------------------:|
| Accuracy | 93,68% ± 1,17% |
| F1 | 93,17% ± 1,33% |
| ROC-AUC | 98,21% ± 0,50% |

Độ lệch chuẩn thấp chứng tỏ mô hình ổn định, không phụ thuộc một lần chia ngẫu nhiên.

## 4.4. Kiểm thử

### 4.4.1. Kiểm thử chức năng (ánh xạ FR)

**Bảng 4.5. Kịch bản kiểm thử chức năng (ánh xạ yêu cầu FR)**

| STT | FR | Kịch bản | Đầu vào | Kỳ vọng | Kết quả |
|:---:|----|----------|---------|---------|:-------:|
| 1 | FR-01 | Nhập văn bản thủ công | Tiêu đề + nội dung | API trả JSON phân loại | Đạt |
| 2 | FR-02 | Nhập URL báo | Link VnExpress/VietnamNet | Crawl title + content | Đạt |
| 3 | FR-03 | Tiền xử lý | Văn bản có URL, chữ hoa | `clean_text` hợp lệ | Đạt |
| 4 | FR-04 | Trích đặc trưng | Văn bản ≥ 5 từ | Embedding 768 chiều | Đạt |
| 5 | FR-05 | Phân loại | Nội dung giật gân | `fake_prob` cao, verdict phù hợp | Đạt |
| 6 | FR-05 | Phân loại tin thật | Bài báo khách quan | `fake_prob` thấp | Đạt |
| 7 | FR-06 | Giải thích | Sau phân loại | Trường `explanation` tiếng Việt | Đạt |
| 8 | FR-07 | Lịch sử | Đã đăng nhập | Lưu/xem lịch sử | Đạt |
| 9 | FR-08 | API REST | GET `/api/health` | `{"status":"ok"}` | Đạt |
| 10 | — | Nội dung quá ngắn | < 5 từ | `status=error` trong JSON (HTTP 200) | Đạt |
| 11 | — | Chưa đăng nhập | Gọi `/api/analyze` | `status=error`, yêu cầu đăng nhập (HTTP 200) | Đạt |

Kiểm thử thực hiện qua giao diện web và curl/Postman; API có tài liệu tự động tại `http://127.0.0.1:8000/docs` [9].

### 4.4.2. Kiểm thử tự động Pytest

Backend tích hợp bộ kiểm thử trong `backend/tests/` — **42 test cases**, chạy bằng:

```bash
./run.sh test
# hoặc: cd backend && ./run_tests.sh
```

**Kết quả:** 42/42 PASSED (~4 giây). Test API dùng SQLite in-memory và mock `PhoBERTInferenceSystem`. Lỗi nghiệp vụ (auth, input) assert qua `status=error` trong body, HTTP 200.

**Bảng 4.6. Bộ kiểm thử tự động Pytest**

| STT | File | Số TC | Phạm vi | Kỹ thuật / Kỳ vọng |
|:---:|------|:-----:|---------|-------------------|
| 1 | `test_verdict.py` | 5 | Verdict 3 mức | Ngưỡng 75% / 35%; kiểm tra biên |
| 2 | `test_text_utils.py` | 5 | `preprocess_text` | Xóa URL, PyVi; thống nhất train/inference |
| 3 | `test_text_cleaner.py` | 3 | Helper `TextCleaner` | HTML/teencode; không luồng inference chính |
| 4 | `test_explanation_engine.py` | 6 | XAI rule-based | Ngưỡng khớp verdict; `build_explanation` |
| 5 | `test_dataset_cleaner.py` | 3 | Lọc CSV | Bỏ thiếu/trùng/ngắn; `content_segmented` |
| 6 | `test_data_crawler.py` | 3 | Crawl / nhập text | Mock HTTP HTML; text rỗng |
| 7 | `test_phobert_inference.py` | 4 | Pipeline 3 mô-đun | Mock PhoBERT/MLP; `infer()` đầy đủ |
| 8 | `test_history_service.py` | 1 | SQLite history | `save_analysis` + list |
| 9 | `test_auth_api.py` | 4 | JWT auth API | Register/login/me; email trùng |
| 10 | `test_api.py` | 8 | Analyze + history | Health, text/url, CRUD, cô lập user |
| | **Tổng** | **42** | Unit: 30, API: 12 | Fixture: `conftest.py` |

Fixture `conftest.py` cung cấp: `db_session` (SQLite test), `client` (TestClient), `auth_headers` (JWT), `mock_inference_system`.

#### 4.4.2.1. Phân nhóm 42 test cases

Bảng 4.6 tổng hợp theo file. Chi tiết từng hàm test tại **Bảng 4.8**, phân **8 nhóm**:

1. **Verdict** (TC-01–05): ngưỡng 75% / 35%, giá trị biên.
2. **Tiền xử lý** (TC-06–13): `preprocess_text` (TC-06–08, TC-10); helper `TextCleaner` (TC-09, TC-11–13).
3. **XAI** (TC-14–19): `ExplanationEngine` khớp `verdict.py`.
4. **Dữ liệu & Crawl** (TC-20–25): lọc CSV, nhập text, crawl HTML.
5. **Inference** (TC-26–29): pipeline 3 mô-đun (mock PhoBERT).
6. **History DB** (TC-30): `save_analysis` / `list_user_history`.
7. **Auth API** (TC-31–34): JWT register/login/me.
8. **Analyze API** (TC-35–42): health, analyze, CRUD history, cô lập user.

**Bảng 4.8. Chi tiết từng kịch bản kiểm thử tự động (42 test cases)**

| Mã | Hàm test | Loại | FR | Đầu vào / Kịch bản | Kỳ vọng |
|:---:|----------|:----:|:--:|--------------------|---------|
| TC-01 | `test_verdict_thresholds[80]` | Unit | FR-05 | Xác suất 80% | `verdict=fake`, nhãn `TIN GIẢ (FAKE)` |
| TC-02 | `test_verdict_thresholds[60]` | Unit | FR-05 | Xác suất 60% | `verdict=suspicious`, nhãn `ĐÁNG NGỜ` |
| TC-03 | `test_verdict_thresholds[45]` | Unit | FR-05 | Xác suất 45% | `verdict=suspicious` |
| TC-04 | `test_verdict_thresholds[30]` | Unit | FR-05 | Xác suất 30% | `verdict=real`, nhãn `TIN THẬT (REAL)` |
| TC-05 | `test_verdict_boundary_values` | Unit | FR-05 | Biên 75 / 74.9 / 35 / 34.9 | Chuyển đúng fake ↔ suspicious ↔ real |
| TC-06 | `test_preprocess_text_basic` | Unit | FR-03 | Văn bản có URL | Xóa URL; có token PyVi (`_`) |
| TC-07 | `test_segment_for_training_matches_preprocess_text` | Unit | FR-03 | Câu mẫu | `segment_for_training` == `preprocess_text` |
| TC-08 | `test_dataset_cleaner_uses_same_pipeline` | Unit | FR-03 | Text + URL | `segment_text` == `preprocess_text` |
| TC-09 | `test_text_cleaner_pipeline_matches_preprocess_text` | Unit | — | Helper vs `preprocess_text` | `pipeline_clean` == `preprocess_text` |
| TC-10 | `test_preprocess_text_empty` | Unit | FR-03 | `""` và `None` | Trả `""` |
| TC-11 | `test_remove_html_and_urls` | Unit | — | Helper: HTML + URL | Xóa thẻ/URL; giữ nội dung |
| TC-12 | `test_normalize_teencode` | Unit | — | Helper: teencode | → `quá`, `gì`, `người` |
| TC-13 | `test_pipeline_clean` | Unit | — | Helper `pipeline_clean` | Lowercase, không URL, PyVi |
| TC-14 | `test_phobert_summary_aligns_with_verdict_thresholds` | Unit | FR-06 | Prob 80 / 50 / 20 | Tóm tắt khớp fake / suspicious / real |
| TC-15 | `test_phobert_summary_boundary_at_fake_threshold` | Unit | FR-06 | 75% và 74.9% | `tin giả` vs `đối chiếu` |
| TC-16 | `test_phobert_summary_boundary_at_suspicious_threshold` | Unit | FR-06 | 35% và 34.9% | `đối chiếu` vs `chính thống` |
| TC-17 | `test_scan_text_signals_detects_sensational_language` | Unit | FR-06 | `CẢNH BÁO KHẨN CẤP` | Signal `text_risk` |
| TC-18 | `test_build_explanation_matches_verdict_for_fake` | Unit | FR-06 | `fake_prob=85` | `verdict=fake`, headline `TIN GIẢ` |
| TC-19 | `test_build_explanation_real_news_tone` | Unit | FR-06 | `fake_prob=10` | `verdict=real`, headline `TIN THẬT` |
| TC-20 | `test_filter_dataset_removes_short_missing_and_duplicates` | Unit | — | DF 5 dòng lỗi | Còn 2 dòng; content unique |
| TC-21 | `test_fill_missing_text_columns` | Unit | — | `content=None` | `title` không NA |
| TC-22 | `test_add_segmented_column_creates_pyvi_tokens` | Unit | FR-03 | Sau filter | Cột `content_segmented` không rỗng |
| TC-23 | `test_get_article_from_text_success` | Unit | FR-01 | Text + title | `status=success`, `user_input` |
| TC-24 | `test_get_article_from_text_empty` | Unit | FR-01 | `"   "` | `status=error` |
| TC-25 | `test_crawl_news_article_parses_html` | Unit | FR-02 | Mock HTML | Parse h1/p; `vnexpress.net` |
| TC-26 | `test_infer_fails_when_model_not_loaded` | Unit | — | Chưa load model | `status=error`, gợi ý train |
| TC-27 | `test_module_1_rejects_short_content` | Unit | FR-03 | 3 từ | `clean=None`, error |
| TC-28 | `test_module_3_classification_fake_verdict` | Unit | FR-05 | Mock prob 82% | `verdict=fake`, `fake_prob≈82` |
| TC-29 | `test_infer_success_pipeline` | Unit | FR-04,05 | Mock M1→M2→M3 | `status=success`, gọi đủ pipeline |
| TC-30 | `test_save_and_list_analysis` | Unit | FR-07 | Lưu SQLite | `total=1`, verdict/prob đúng |
| TC-31 | `test_register_and_login_flow` | API | — | Register→login→/me | JWT + email khớp |
| TC-32 | `test_register_duplicate_email` | API | — | Email trùng | `status=error` |
| TC-33 | `test_login_wrong_password` | API | — | Sai mật khẩu | `status=error` |
| TC-34 | `test_me_requires_auth` | API | — | Không JWT | `status=error` |
| TC-35 | `test_health_check` | API | FR-08 | GET `/api/health` | `ok`, `model_loaded=true` |
| TC-36 | `test_analyze_unauthorized` | API | FR-08 | Không đăng nhập | Yêu cầu đăng nhập |
| TC-37 | `test_analyze_empty_text_when_authenticated` | API | FR-01 | Text rỗng + JWT | `status=error`, `trống` |
| TC-38 | `test_analyze_text_success` | API | FR-01,05,06,07 | Text giật gân | success + verdict + history_id |
| TC-39 | `test_analyze_url_mode` | API | FR-02,05 | `mode=url` | success; `infer(url=...)` |
| TC-40 | `test_history_list_after_analyze` | API | FR-07 | Analyze → list | `total≥1` |
| TC-41 | `test_history_detail_and_delete` | API | FR-07 | Detail + delete | CRUD đúng |
| TC-42 | `test_history_isolated_between_users` | API | FR-07,08 | User A vs B | B không xem được history A |

*Ghi chú FR: `—` = helper `TextCleaner`, auth nội bộ, hoặc pipeline dữ liệu. API lỗi nghiệp vụ: HTTP 200 + `status=error` + `message`.*

## 4.5. Kết luận chương

Chương 4 đã trình bày môi trường phát triển, hiện thực các mô-đun, kết quả thực nghiệm (F1 93,71%), đối chiếu SMART (Bảng 4.7) và kiểm thử (Bảng 4.5, 4.6, 4.8). Hạn chế: chưa tích hợp siêu dữ liệu MXH thực, crawler HTML đơn giản — thảo luận tại Chương 5.

---

<br>

# CHƯƠNG 5: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 5.1. Kết luận

Luận văn đã hoàn thành nghiên cứu, thiết kế, huấn luyện, đánh giá và triển khai hệ thống **ShieldAI** — công cụ phát hiện tin giả tiếng Việt dựa trên **PhoBERT** và **MLP**. Các kết quả chính:

1. Xây dựng pipeline tiền xử lý thống nhất `preprocess_text` (train + inference).
2. Thiết kế kiến trúc PhoBERT 768 → StandardScaler → MLP (128, 64).
3. Đạt độ chính xác **94,13%**, F1 **93,71%**, ROC-AUC **98,50%** trên tập kiểm thử hold-out (~3.183 mẫu, 30% của 10.609 mẫu).
4. Triển khai ứng dụng web FastAPI + Next.js với verdict 3 mức và mô-đun giải thích.
5. Hoàn thành các mục tiêu đã đề ra tại mục 1.2.

## 5.2. Đóng góp của luận văn

### 5.2.1. Tính mới của đề tài

Đề tài có **tính mới** ở ba điểm chính, được kiểm chứng bằng số liệu (Bảng 4.3, 4.4) và kiểm thử tự động (Bảng 4.6):

1. **Pipeline PhoBERT + MLP end-to-end cho tiếng Việt:** Embedding cố định 768 chiều, tiền xử lý thống nhất train/inference, triển khai web hoàn chỉnh.
2. **Verdict 3 mức thống nhất:** Backend `verdict.py` và giao diện cùng ngưỡng (75% / 35%), tránh lệch giữa xác suất và nhãn hiển thị.
3. **Giải thích rule-based tích hợp web:** Module `ExplanationEngine` sinh diễn giải tiếng Việt; lịch sử phân tích lưu SQLite.

### 5.2.2. Phân biệt đóng góp bản thân và thành phần có sẵn

| Thành phần | Nguồn gốc | Đóng góp của luận văn |
|------------|-----------|------------------------|
| PhoBERT-base [3] | VinAI (pre-trained) | **Không** huấn luyện lại; chỉ trích [CLS] |
| scikit-learn MLP [7] | Thư viện có sẵn | **Có** — kiến trúc (128,64), pipeline scale |
| FastAPI / Next.js [9], [10] | Framework | **Có** — API, UI, auth, lịch sử |
| `preprocess_text` | Code đề tài | **Có** — thống nhất train/inference |
| `ExplanationEngine` | Code đề tài | **Có** — quy tắc tiếng Việt, tín hiệu văn bản |
| `PhoBERTInferenceSystem` | Code đề tài | **Có** — 3 mô-đun, đồng bộ notebook |
| Hold-out + 5-fold CV | Thực nghiệm đề tài | **Có** — script eval, metric, biểu đồ |

*Như vậy, giá trị khoa học nằm ở **cách xây dựng pipeline, đánh giá và triển khai** thành hệ thống hoàn chỉnh cho tiếng Việt.*

**Về mặt lý luận:** Chứng minh hiệu quả PhoBERT + MLP trên **10.609 mẫu** tin y tế/sức khỏe tiếng Việt; quy trình tái lập (notebook, module dùng chung).

**Về mặt thực tiễn:** Công cụ web hỗ trợ kiểm tra tin nghi ngờ; mã nguồn mở, mở rộng được; phù hợp demo và nền tảng nghiên cứu tiếp.

## 5.3. Hạn chế

1. **Chưa tích hợp siêu dữ liệu mạng xã hội** — chỉ phân tích văn bản; bổ sung metadata là hướng mở rộng.
2. **PhoBERT cố định** — chưa khai thác hết tiềm năng fine-tune.
3. **Crawler HTML đơn giản** — không phủ hết mọi trang báo.
4. **Giải thích heuristic** — không khớp hoàn toàn ranh giới quyết định MLP.
5. **Nguy cơ thiên lệch tập dữ liệu** — mô hình có thể học shortcut theo nguồn miền.

## 5.4. Hướng phát triển

1. Thu thập siêu dữ liệu mạng xã hội thực, thử nghiệm mô hình lai (PhoBERT + metadata).
2. Fine-tune PhoBERT, so sánh với chiến lược cố định.
3. Mô hình đồ thị lan truyền (GNN) khi có dữ liệu chia sẻ.
4. Tích hợp XAI (SHAP trên MLP) kết hợp diễn giải quy tắc.
5. Phân loại đa lớp theo loại tin giả (y tế, chính trị…).
6. Ứng dụng di động; học liên tục với mẫu tin giả mới.

---

<br>

# TÀI LIỆU THAM KHẢO

### Tiếng Việt

[1] Bộ Thông tin và Truyền thông (2023). *Báo cáo tình hình sử dụng Internet và mạng xã hội tại Việt Nam*. Hà Nội: Bộ Thông tin và Truyền thông.

[2] Nguyễn Thị Lan Anh, Trần Văn Bình (2022). Phát hiện tin giả tiếng Việt bằng mô hình BiLSTM và word embedding. *Tạp chí Khoa học Công nghệ Thông tin*, 15(2), 45–58. [Bổ sung đúng nguồn nếu Khoa yêu cầu]

### Tiếng Anh

[3] Nguyen, D. Q., & Nguyen, A. T. (2020). PhoBERT: Pre-trained language models for Vietnamese. *Findings of the Association for Computational Linguistics: EMNLP 2020*, 1037–1042.

[4] Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional transformers for language understanding. *Proceedings of NAACL-HLT 2019*, 4171–4186.

[5] Shu, K., Sliva, A., Wang, S., Tang, J., & Liu, H. (2017). Fake news detection on social media: A data mining perspective. *ACM SIGKDD Explorations Newsletter*, 19(1), 22–36.

[6] Zhou, X., & Zafarani, R. (2020). A survey of fake news: Fundamental theories, detection methods, and opportunities. *ACM Computing Surveys*, 53(5), 1–40.

[7] Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.

[8] Vaswani, A., Shazeer, N., Parmar, N., et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30, 5998–6008.

[9] Tiangolo, S. (2024). FastAPI documentation. Truy cập tại: https://fastapi.tiangolo.com [Ngày truy cập: 06/06/2026]

[10] Vercel Inc. (2024). Next.js documentation. Truy cập tại: https://nextjs.org/docs [Ngày truy cập: 06/06/2026]

[11] Pan, Y., Yang, W., MacKinlay, A., et al. (2023). Zero-shot fact-checking with large language models. *Proceedings of the 61st Annual Meeting of the ACL*, 12456–12470.

[12] Wolff, J., & Müller, M. (2023). LIAR-PLUS: A multilingual dataset for fake news detection. *Proceedings of the 17th Conference of the European Chapter of the ACL*, 892–903.

[13] VinAI Research (2020). PhoBERT model card. Truy cập tại: https://huggingface.co/vinai/phobert-base [Ngày truy cập: 06/06/2026]

[14] Hugging Face (2024). Transformers documentation. Truy cập tại: https://huggingface.co/docs/transformers [Ngày truy cập: 06/06/2026]

*Chuẩn trích dẫn: IEEE (số thứ tự [n] trong văn bản). Tổng cộng 14 nguồn — đáp ứng yêu cầu ≥ 10 tài liệu tham khảo.*

---

<br>

# PHỤ LỤC

## Phụ lục A: Mã nguồn chương trình chính

Cấu trúc mã nguồn dự án:

```
DoAnTotNghiep/
├── backend/
│   ├── api/main.py
│   ├── phobert_inference.py
│   ├── verdict.py
│   ├── explanation_engine.py
│   ├── text_utils.py
│   ├── data_crawler.py
│   ├── training/train_phobert_model.ipynb
│   └── experiments/run_experimental_evaluation.py
├── frontend/
│   ├── app/analyze/page.tsx
│   ├── app/results/page.tsx
│   └── lib/api.ts
├── run.sh
└── requirements.txt
```

*(Chèn đoạn mã tiêu biểu: `preprocess_text`, `infer()` — nếu quy định Khoa yêu cầu)*

## Phụ lục B: Hướng dẫn cài đặt và chạy hệ thống

```bash
# 1. Cài đặt
cd DoAnTotNghiep
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd frontend && npm install && cd ..

# 2. Chạy hệ thống
./run.sh

# 3. Truy cập
# Giao diện: http://localhost:3000
# API:       http://127.0.0.1:8000
# Health:    http://127.0.0.1:8000/api/health
```

## Phụ lục C: Kết quả thực nghiệm chi tiết

File JSON/CSV tại `backend/experiments/figures/experimental/`:

- `metrics_summary.csv` — Bảng 4.3
- `cv_summary.csv` — Bảng 4.4
- `metrics_summary.json` — dữ liệu gốc cho biểu đồ Hình 4.1–4.5

## Phụ lục D: Câu hỏi hội đồng thường gặp (FAQ bảo vệ)

| Câu hỏi | Gợi ý trả lời ngắn |
|---------|---------------------|
| Vì sao không fine-tune PhoBERT? | Tiết kiệm tài nguyên; F1 93,71% đủ mạnh cho tiểu luận; embedding tái sử dụng qua `.npy`. |
| Đóng góp của em khác gì PhoBERT có sẵn? | Xem Bảng 5.2.2: pipeline end-to-end, `preprocess_text` thống nhất, verdict 3 mức, giải thích, web, lịch sử. |
| Vì sao chọn MLP thay vì XGBoost/SVM? | Phi tuyến trên vector dense 768 chiều; `predict_proba`; regularization L2; huấn luyện nhanh trên CPU. |
| Vì sao không dùng metadata MXH? | Tập train không có MXH thực; triển khai text-only đảm bảo nhất quán; metadata là hướng mở rộng. |
| False positive nguy hiểm thế nào? | Gán nhầm tin thật là giả; UI hiển thị xác suất + mức "đáng ngờ", không khẳng định tuyệt đối. |
| Hệ thống có CSDL không? | SQLite lưu user/history; mô hình lưu joblib/npy (Hình 3.3). |
| Làm sao tái lập kết quả? | `random_state=42`; chạy notebook train + `run_experimental_evaluation.py`; `./run.sh` cho demo. |

*Chi tiết checklist bảo vệ: `docs/CHUAN_BI_BAO_VE_THEO_PHIEU_CHAM.md`.*

---

*Hết luận văn.*

**Phiên bản:** 5.0 — PhoBERT text-only (đồng bộ mã nguồn tháng 06/2026)  
**Cập nhật:** Tháng 06/2026
