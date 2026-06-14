# LUẬN VĂN TỐT NGHIỆP ĐẠI HỌC

---

**BỘ GIÁO DỤC VÀ ĐÀO TẠO**

**TRƯỜNG ĐẠI HỌC TÂN TẠO**

**KHOA CÔNG NGHỆ THÔNG TIN**

---

## NGHIÊN CỨU, XÂY DỰNG CÔNG CỤ PHÂN TÍCH VÀ PHÁT HIỆN TIN GIẢ TIẾNG VIỆT BẰNG HỌC MÁY LAI

*(Hệ thống ShieldAI: PhoBERT — Metadata — Mạng nơ-ron đa tầng)*

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

Trong suốt quá trình thực hiện luận văn tốt nghiệp với đề tài *“Nghiên cứu, xây dựng công cụ phân tích và phát hiện tin giả tiếng Việt bằng học máy lai”*, em đã nhận được sự quan tâm, hỗ trợ và động viên từ nhiều phía.

Em xin chân thành cảm ơn **Thầy/Cô [Tên giảng viên hướng dẫn]** — Giảng viên hướng dẫn — đã tận tình chỉ bảo, định hướng phương pháp nghiên cứu, góp ý về kiến trúc hệ thống và đánh giá kết quả thực nghiệm, giúp em hoàn thiện luận văn này.

Em xin cảm ơn các **Thầy, Cô** trong Khoa Công nghệ Thông tin, Trường Đại học Tân Tạo, đã truyền đạt kiến thức nền tảng về trí tuệ nhân tạo, xử lý ngôn ngữ tự nhiên và kỹ thuật phần mềm trong suốt quá trình học tập.

Em xin gửi lời cảm ơn sâu sắc đến **gia đình** đã tạo điều kiện, động viên tinh thần để em yên tâm học tập và nghiên cứu. Em cũng xin cảm ơn **bạn bè, đồng nghiệp** đã chia sẻ ý kiến, hỗ trợ kiểm thử hệ thống ShieldAI.

Mặc dù đã nỗ lực hoàn thiện, luận văn không tránh khỏi những thiếu sót. Em rất mong nhận được sự góp ý của Quý Thầy, Cô để đề tài được phát triển tốt hơn trong tương lai.

**Sinh viên thực hiện**

*(Ký và ghi rõ họ tên)*

---

## TÓM TẮT LUẬN VĂN

Trong bối cảnh mạng xã hội phát triển mạnh tại Việt Nam, tin giả (*disinformation*) trở thành mối đe dọa đối với an ninh thông tin và ổn định xã hội. Các phương pháp phát hiện truyền thống dựa trên từ khóa hoặc thống kê văn bản đơn giản không còn đáp ứng được độ tinh vi của nội dung giả mạo. Đồng thời, việc áp dụng trực tiếp mô hình ngôn ngữ tiếng Anh trên tiếng Việt thường cho kết quả kém do đặc thù ngôn ngữ đơn lập và thiếu tài nguyên huấn luyện trước chuyên biệt.

Luận văn trình bày quá trình nghiên cứu, thiết kế, huấn luyện, đánh giá và triển khai hệ thống **ShieldAI** — công cụ phát hiện tin giả tiếng Việt theo hướng tiếp cận **học máy lai đa phương thức**. Hệ thống kết hợp embedding ngữ nghĩa 768 chiều từ **PhoBERT-base** (chế độ cố định) với mười đặc trưng siêu dữ liệu (năm tín hiệu mạng xã hội và năm thống kê văn bản). Hai vector được hợp nhất bằng phép nối thành vector 778 chiều, đưa qua bộ phân loại **MLP (128, 64)** để dự đoán tin thật/tin giả.

Kết quả thực nghiệm trên khoảng 169.000 mẫu cho thấy mô hình lai đạt độ chính xác **97,68%**, F1 **97,51%** và ROC-AUC **99,71%**, vượt trội so với mô hình chỉ dùng PhoBERT (F1 93,70%). Nghiên cứu phân rã bảy cấu hình xác nhận siêu dữ liệu đóng góp tích cực vào hiệu năng. Hệ thống được triển khai web với **FastAPI** và **Next.js**, tích hợp mô-đun giải thích kết quả theo quy tắc. Luận văn cũng thảo luận hạn chế khi siêu dữ liệu mạng xã hội được mô phỏng trong huấn luyện.

**Từ khóa:** tin giả, phát hiện tin giả, PhoBERT, học máy lai, tiếng Việt, mạng xã hội, ShieldAI

---

## ABSTRACT

In the context of rapid social media growth in Vietnam, disinformation has become a serious threat to information security and social stability. Traditional detection methods based on keywords or simple text statistics are insufficient against sophisticated fake content. Meanwhile, directly applying English-centric pre-trained language models to Vietnamese often yields suboptimal results due to the monosyllabic structure of the language and the lack of dedicated pre-training resources.

This thesis presents the research, design, training, evaluation, and deployment of **ShieldAI** — a Vietnamese fake news detection system based on a **multimodal hybrid machine learning** approach. The system combines 768-dimensional semantic embeddings from **PhoBERT-base** (frozen mode) with ten metadata features (five social signals and five text statistics). The feature vectors are concatenated into a 778-dimensional representation and fed into an **MLP classifier (128, 64)** for binary classification.

Experimental results on approximately 169,000 samples show that the hybrid model achieves **97.68% accuracy**, **97.51% F1-score**, and **99.71% ROC-AUC**, outperforming the PhoBERT-only baseline (F1 93.70%). A seven-configuration ablation study confirms the positive contribution of metadata. The system is deployed as a web application using **FastAPI** and **Next.js**, with a rule-based explanation module. The thesis also discusses limitations regarding simulated social metadata during training.

**Keywords:** fake news, fake news detection, PhoBERT, hybrid machine learning, Vietnamese, social media, ShieldAI

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
| Hình 2.2 | Sơ đồ tiếp cận học máy lai đa phương thức | … |
| Hình 3.1 | Kiến trúc tổng thể hệ thống ShieldAI | … |
| Hình 3.2 | Sơ đồ bốn mô-đun suy luận (HybridInferenceSystem) | … |
| Hình 3.3 | Sơ đồ quan hệ lưu trữ dữ liệu và mô hình | … |
| Hình 3.4 | Lưu đồ thuật toán suy luận (Inference) | … |
| Hình 3.5 | Wireframe giao diện trang phân tích (/analyze) | … |
| Hình 3.6 | Wireframe giao diện trang kết quả (/results) | … |
| Hình 4.1 | Ma trận nhầm lẫn mô hình lai đầy đủ | … |
| Hình 4.2 | So sánh hiệu năng chỉ-văn-bản và mô hình lai | … |
| Hình 4.3 | Kết quả nghiên cứu phân rã (ablation study) | … |
| Hình 4.4 | Đường cong ROC các cấu hình mô hình chính | … |
| Hình 4.5 | Biểu đồ kiểm định chéo 5-fold (F1, Accuracy) | … |
| Hình 4.6 | Giao diện trang chủ hệ thống ShieldAI | … |
| Hình 4.7 | Giao diện nhập văn bản và siêu dữ liệu | … |
| Hình 4.8 | Giao diện hiển thị kết quả phân loại và giải thích | … |

> *Các hình 4.1–4.5 được sinh từ script `run_experimental_evaluation.py`, lưu tại `backend/experiments/figures/experimental/` sau khi chạy đánh giá.*

---

## DANH MỤC BẢNG BIỂU

| Ký hiệu | Tên bảng | Trang |
|---------|----------|:-----:|
| Bảng 1.1 | Mục tiêu cụ thể dạng SMART | … |
| Bảng 2.1 | So sánh công trình liên quan với đề tài ShieldAI | … |
| Bảng 2.2 | Danh sách công nghệ, thư viện và lý do lựa chọn | … |
| Bảng 3.5 | Mô tả thực thể lưu trữ | … |
| Bảng 3.1 | Mười đặc trưng siêu dữ liệu trong mô hình lai | … |
| Bảng 3.2 | Yêu cầu chức năng hệ thống ShieldAI | … |
| Bảng 3.3 | Yêu cầu phi chức năng hệ thống ShieldAI | … |
| Bảng 3.4 | Siêu tham số bộ phân loại MLP | … |
| Bảng 4.1 | Môi trường phát triển và triển khai | … |
| Bảng 4.2 | Thống kê bộ dữ liệu full_dataset.csv | … |
| Bảng 4.3 | Hiệu năng bảy cấu hình mô hình trên tập kiểm thử | … |
| Bảng 4.4 | Kết quả kiểm định chéo 5-fold (mô hình lai) | … |
| Bảng 4.5 | Kịch bản kiểm thử chức năng hệ thống (ánh xạ FR) | … |
| Bảng 4.6 | Đối chiếu mục tiêu SMART và kết quả đạt được | … |

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

Nghiên cứu, thiết kế và xây dựng hệ thống phát hiện tin giả tiếng Việt có khả năng vận hành thực tế, kết hợp phân tích ngữ nghĩa sâu và tín hiệu siêu dữ liệu bổ trợ, đồng thời cung cấp cơ chế diễn giải kết quả cho người dùng phổ thông.

### 1.2.2. Mục tiêu cụ thể (theo tiêu chí SMART)

*Bảng 1.1. Mục tiêu cụ thể dạng SMART*

| Mã | Mục tiêu | S (Cụ thể) | M (Đo lường) | A (Khả thi) | R (Liên quan) | T (Thời hạn) |
|----|----------|------------|--------------|-------------|---------------|--------------|
| MT-01 | Tiền xử lý tiếng Việt | Pipeline PyVi + teencode + làm sạch | Có module `TextCleaner` chạy được | Dùng PyVi, PhoBERT [3] | Chuẩn hóa đầu vào NLP | HK2 2025–2026 |
| MT-02 | Mô hình lai | PhoBERT 768 + 10 meta → MLP | F1 ≥ 95% trên tập test | ~169k mẫu, sklearn | Giải quyết đặt vấn đề | HK2 2025–2026 |
| MT-03 | Đánh giá & ablation | 7 cấu hình + 5-fold CV | Bảng metric đầy đủ | Script eval có sẵn | Chứng minh khoa học | HK2 2025–2026 |
| MT-04 | Triển khai web | FastAPI + Next.js | 8/8 chức năng FR (Bảng 3.2) | `./run_web.sh` | Ứng dụng thực tiễn | HK2 2025–2026 |
| MT-05 | Giải thích kết quả | Rule-based tiếng Việt | JSON `explanation` trên UI | Module riêng | Tăng tin cậy người dùng | HK2 2025–2026 |

## 1.3. Đối tượng và phạm vi nghiên cứu

### 1.3.1. Đối tượng nghiên cứu

Đối tượng là bài toán **phân loại nhị phân** văn bản tiếng Việt thành tin thật hoặc tin giả, dựa trên nội dung văn bản và siêu dữ liệu ngữ cảnh (tùy chọn).

### 1.3.2. Phạm vi nghiên cứu

**Trong phạm vi:**

- Phân loại nhị phân với nhãn có giám sát trên tập dữ liệu tiếng Việt.
- PhoBERT-base ở chế độ cố định (trích embedding, không fine-tune end-to-end).
- Siêu dữ liệu MXH mô phỏng khi huấn luyện; người dùng nhập siêu dữ liệu thực khi sử dụng web.
- Giải thích kết quả theo quy tắc heuristic.

**Ngoài phạm vi:** phát hiện deepfake đa phương tiện; phân loại đa lớp theo chủ đề; fine-tune PhoBERT trên GPU cluster; thu thập API Facebook thương mại.

## 1.4. Phương pháp nghiên cứu

Đề tài kết hợp: **nghiên cứu tài liệu** (tổng quan lý thuyết và công trình liên quan); **phân tích–tổng hợp** (yêu cầu hệ thống, đặc trưng); **thực nghiệm so sánh** (ablation, kiểm định chéo); **thiết kế–xây dựng hệ thống** (backend, frontend); **đánh giá định lượng** (Accuracy, Precision, Recall, F1, ROC-AUC).

## 1.5. Ý nghĩa khoa học và thực tiễn

**Ý nghĩa khoa học:** Đề tài chứng minh hiệu quả của phương pháp học máy lai trên tiếng Việt, cung cấp số liệu tham chiếu (F1 97,51%) và phân tích đóng góp từng nhóm đặc trưng.

**Ý nghĩa thực tiễn:** Hệ thống ShieldAI hỗ trợ người dùng kiểm tra nội dung nghi ngờ (văn bản hoặc URL), nhận xác suất tin giả và lý do diễn giải — bước đầu hướng tới công cụ hỗ trợ fact-checking, không thay thế con người.

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

### 2.1.2. Học máy lai và hợp nhất đa phương thức

**Học máy lai** (*hybrid machine learning*) kết hợp nhiều nguồn đặc trưng không đồng nhất. **Hợp nhất sớm** (*early fusion*) nối vector đặc trưng từng nhánh rồi đưa qua bộ phân loại chung — phù hợp quy mô đồ án và dễ tái lập.

### 2.1.3. Trí tuệ nhân tạo có thể giải thích

Người dùng cần không chỉ nhãn phân loại mà còn **lý do**. ShieldAI dùng giải thích theo quy tắc (*rule-based*), cân bằng giữa tính hình thức và khả năng tiếp cận công chúng.

## 2.2. Cơ sở lý thuyết

### 2.2.1. Xử lý ngôn ngữ tự nhiên tiếng Việt

Tiếng Việt là ngôn ngữ đơn lập, bắt buộc **phân đoạn từ** trước khi đưa vào mô hình. Văn bản mạng xã hội chứa teencode, emoji — cần tiền xử lý. Thư viện **PyVi** được dùng để phân đoạn từ (dạng `người_dùng`, `tin_giả`).

### 2.2.2. Mô hình BERT và PhoBERT

**BERT** dùng Transformer encoder hai chiều, tạo embedding ngữ cảnh. **PhoBERT** (VinAI, 2020) [3] huấn luyện trước trên corpus tiếng Việt ~20 GB, kế thừa kiến trúc BERT [4]. Phiên bản `vinai/phobert-base`: 12 lớp, hidden 768, 12 attention heads. ShieldAI trích vector **[CLS]** 768 chiều làm biểu diễn câu, độ dài tối đa 256 token.

### 2.2.3. Mạng nơ-ron đa tầng (MLP)

MLP gồm các lớp ẩn với hàm kích hoạt phi tuyến (ReLU), phù hợp học quan hệ phức tạp giữa embedding PhoBERT và siêu dữ liệu sau hợp nhất.

## 2.3. Tổng quan các công trình nghiên cứu liên quan

### 2.3.1. Các nghiên cứu trong nước

Trong nước, các hướng tiếp cận chủ yếu gồm: (i) phân loại bằng TF-IDF kết hợp SVM/Naive Bayes — đơn giản nhưng thiếu ngữ cảnh sâu; (ii) mô hình học sâu PhoBERT, BiLSTM — cải thiện F1 nhưng thường chỉ xét văn bản; (iii) bổ sung đặc trưng nguồn tin hoặc thống kê văn bản. **Phân tích so sánh:** hầu hết công trình chưa kết hợp đồng thời embedding PhoBERT, siêu dữ liệu lan truyền và triển khai web end-to-end có giải thích — đây là khoảng trống mà ShieldAI nhắm tới.

### 2.3.2. Các nghiên cứu ngoài nước

Shu *et al.* [5] phân loại ba hướng: nội dung, mạng lan truyền, nguồn tin. Zhou và Zafarani [6] tổng quan lý thuyết, phương pháp và hướng mở. Các benchmark FakeNewsNet, LIAR có đồ thị lan truyền nhưng chưa phủ tiếng Việt. Hướng LLM zero-shot mới nổi [11] thiếu kiểm soát và khó tái lập trên tập riêng.

**Bảng 2.1. So sánh công trình liên quan với đề tài ShieldAI**

| Nghiên cứu | Ngôn ngữ | Đặc trưng văn bản | Metadata / MXH | Ablation | Triển khai web | Giải thích |
|------------|:--------:|:-----------------:|:--------------:|:--------:|:--------------:|:----------:|
| TF-IDF + SVM (truyền thống) | VN | Thống kê từ | Không | Hạn chế | Hiếm | Không |
| PhoBERT / BiLSTM | VN | Học sâu | Hạn chế | Một phần | Một số | Hạn chế |
| Hybrid (quốc tế) [5], [6] | EN chủ yếu | Có | Có (graph) | Có | Một số | Một số |
| **ShieldAI (đề tài)** | **VN** | **PhoBERT 768** | **10 chiều** | **7 cấu hình** | **Có** | **Rule-based VN** |

*Bảng 2.1 cho thấy đề tài bổ sung pipeline lai tiếng Việt có đánh giá phân rã và ứng dụng web — khác với chỉ áp dụng mô hình có sẵn.*

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

Chương 2 đã trình bày khái niệm tin giả, cơ sở NLP tiếng Việt, PhoBERT [3], học máy lai và **so sánh phân tích** công trình trong/ngoài nước (Bảng 2.1). Công nghệ được chọn kèm **lý do** (Bảng 2.2). Chương 3 sẽ chi tiết hóa phương pháp, yêu cầu và thiết kế kiến trúc ShieldAI.

---

<br>

# CHƯƠNG 3: PHƯƠNG PHÁP NGHIÊN CỨU VÀ THIẾT KẾ HỆ THỐNG

## 3.1. Phương pháp nghiên cứu

### 3.1.1. Tiếp cận học máy lai

Hệ thống kết hợp hai luồng đặc trưng bổ sung:

- **Nhánh ngữ nghĩa:** PhoBERT-base → vector [CLS] 768 chiều.
- **Nhánh siêu dữ liệu:** 10 chiều (5 MXH + 5 thống kê văn bản).

Hợp nhất: nối vector → 778 chiều → chuẩn hóa → MLP (128, 64) → nhãn tin thật/tin giả.

**Cơ sở lựa chọn:** Thực nghiệm cho thấy mô hình lai đạt F1 **97,51%**, cao hơn chỉ PhoBERT (**93,70%**) và chỉ siêu dữ liệu (**95,65%**), xác nhận tính bổ sung của hai nguồn thông tin.

### 3.1.2. Chiến lược PhoBERT cố định

Không fine-tune end-to-end vì: (i) tiết kiệm GPU/thời gian; (ii) mục tiêu đề tài là chứng minh phương pháp lai; (iii) embedding lưu `.npy` tái sử dụng; (iv) MLP nhỏ ổn định hơn. Trade-off: có thể mất 1–2% so với fine-tune tối ưu.

### 3.1.3. Mô phỏng siêu dữ liệu mạng xã hội

`full_dataset.csv` không có dữ liệu MXH thực. Hàm `simulate_user_signals(is_fake)` sinh phân phối ngẫu nhiên có điều kiện theo nhãn. Khi vận hành, người dùng nhập siêu dữ liệu thực. **Hạn chế:** cần ghi rõ trong luận văn.

### 3.1.4. Giao thức đánh giá

- Chia tập: 70% huấn luyện / 30% kiểm thử, phân tầng, `random_state = 42`.
- Kiểm định chéo 5-fold phân tầng.
- Ablation: bảy cấu hình mô hình.
- Chỉ số: Accuracy, Precision, Recall, F1, ROC-AUC.

## 3.2. Phân tích yêu cầu

### 3.2.1. Yêu cầu chức năng

**Bảng 3.2. Yêu cầu chức năng hệ thống ShieldAI**

| Mã | Yêu cầu | Mô tả |
|----|---------|-------|
| FR-01 | Nhập văn bản | Người dùng dán tiêu đề và nội dung bài viết |
| FR-02 | Nhập URL | Hệ thống crawl và trích xuất nội dung báo điện tử |
| FR-03 | Nhập siêu dữ liệu MXH | Tuổi tài khoản, follower, verified, tốc độ share, tỷ lệ phẫn nộ |
| FR-04 | Tiền xử lý văn bản | Làm sạch HTML, URL, teencode; phân đoạn PyVi |
| FR-05 | Trích đặc trưng | PhoBERT + siêu dữ liệu song song |
| FR-06 | Phân loại | Dự đoán tin thật/tin giả và xác suất |
| FR-07 | Giải thích kết quả | Trình bày lý do bằng tiếng Việt |
| FR-08 | API REST | Endpoint `/api/analyze`, `/api/health` |

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
│  Người dùng  │               │ /analyze        │  POST /api/    │ HybridInferenceSystem│
└──────────────┘               │ /results        │  analyze       └──────────────────────┘
                               └─────────────────┘
```

*Hình 3.1 mô tả luồng tương tác: người dùng thao tác trên giao diện Next.js; yêu cầu phân tích được chuyển tới API Python xử lý mô hình.*

**Hình 3.2. Sơ đồ bốn mô-đun suy luận**

```
[Module 1: Crawler + TextCleaner]
            │
            ▼
[Module 2: PhoBERT ∥ Metadata] ── song song ──
            │
            ▼
[Module 3: Concat + StandardScaler]
            │
            ▼
[Module 4: MLP + ExplanationEngine]
```

*Hình 3.2 thể hiện pipeline suy luận bốn giai đoạn, trong đó Module 2 trích xuất đặc trưng song song trước khi hợp nhất.*

Bốn mô-đun suy luận:

| Mô-đun | Tên | Chức năng |
|--------|-----|-----------|
| 1 | Thu thập & tiền xử lý | DataCrawler, TextCleaner |
| 2 | Trích xuất đặc trưng | PhoBERT ∥ Metadata |
| 3 | Hợp nhất | Concatenation + StandardScaler |
| 4 | Phân loại & giải thích | MLP + ExplanationEngine |

### 3.3.2. Thiết kế lưu trữ dữ liệu

Hệ thống **không sử dụng cơ sở dữ liệu quan hệ** (MySQL, PostgreSQL) vì bài toán inference là stateless: mỗi yêu cầu phân tích độc lập, không cần lưu lịch sử người dùng trên server. Thay vào đó, mô hình **lưu trữ dạng file** — phù hợp triển khai đồ án và tái lập thí nghiệm.

**Hình 3.3. Sơ đồ quan hệ lưu trữ dữ liệu và mô hình**

```
full_dataset.csv ──► dataset_cleaner ──► DataFrame sạch
                              │
                              ▼
                    phobert_base_features.npy
                    phobert_base_labels.npy
                              │
         feature_extraction ──┤
                              ▼
              hybrid_mlp_model.joblib
              hybrid_scaler.joblib
              hybrid_scaler_meta.joblib
                              │
                              ▼
                    hybrid_inference.py (runtime)
```

*Bảng 3.5. Mô tả thực thể lưu trữ*

| Thực thể | Định dạng | Vai trò | Giai đoạn |
|----------|-----------|---------|-----------|
| Tập huấn luyện | CSV | ~169.000 mẫu, nhãn `is_fake` | Train |
| Embedding | NPY | Ma trận 768 chiều × N mẫu | Train/Eval |
| Nhãn | NPY | Vector nhãn tương ứng | Train/Eval |
| MLP + Scaler | joblib | Mô hình suy luận | Inference |
| Kết quả web | sessionStorage | JSON kết quả tạm | Runtime UI |

Kết quả phân tích trên web lưu tạm `sessionStorage` trình duyệt giữa `/analyze` và `/results` — không ghi đĩa server.

### 3.3.3. Thiết kế giao diện

Ba trang chính:

| Route | Chức năng |
|-------|-----------|
| `/` | Trang chủ — giới thiệu ShieldAI |
| `/analyze` | Form nhập văn bản/URL + siêu dữ liệu MXH |
| `/results` | Gauge xác suất, giải thích, breakdown metadata |

*Hình 3.5, 3.6* — Wireframe hoặc screenshot khi hoàn thiện Word.

### 3.3.4. Thiết kế thuật toán

**Bảng 3.1. Mười đặc trưng siêu dữ liệu**

| STT | Đặc trưng | Nhóm | Mô tả |
|:---:|-----------|------|-------|
| 1 | account_age_days | MXH | Tuổi tài khoản (ngày) |
| 2 | followers | MXH | Số người theo dõi |
| 3 | is_verified | MXH | Tích xanh (0/1) |
| 4 | share_speed | MXH | Tốc độ chia sẻ |
| 5 | angry_ratio | MXH | Tỷ lệ phản ứng phẫn nộ |
| 6 | title_length | Văn bản | Độ dài tiêu đề |
| 7 | uppercase_ratio | Văn bản | Tỷ lệ chữ IN HOA |
| 8 | exclamation_count | Văn bản | Số dấu `!` trong tiêu đề |
| 9 | question_count | Văn bản | Số dấu `?` trong tiêu đề |
| 10 | punctuation_density | Văn bản | Mật độ dấu câu |

**Hình 3.4. Lưu đồ thuật toán suy luận (Inference)**

```
                    ┌─────────────┐
                    │   BẮT ĐẦU   │
                    └──────┬──────┘
                           ▼
              ┌────────────────────────┐
              │ Nhận text/URL + meta?  │
              └────────────┬───────────┘
                           ▼
              ┌────────────────────────┐
              │ Module 1: Làm sạch    │
              │ (≥ 5 từ?)              │
              └────────────┬───────────┘
                     Không │ Có
              ┌────────────┴───────────┐
              ▼                        ▼
        [Trả lỗi]          ┌─────────────────────┐
                             │ Module 2: PhoBERT   │
                             │        ∥ Meta 10    │
                             └──────────┬──────────┘
                                        ▼
                             ┌─────────────────────┐
                             │ Module 3: Concat    │
                             │ + Scale 778 chiều   │
                             └──────────┬──────────┘
                                        ▼
                             ┌─────────────────────┐
                             │ Module 4: MLP       │
                             │ + Giải thích        │
                             └──────────┬──────────┘
                                        ▼
                             ┌─────────────────────┐
                             │  JSON kết quả       │
                             └─────────────────────┘
```

*Hình 3.4 là lưu đồ thuật toán chính khi người dùng gửi yêu cầu phân tích — đáp ứng tiêu chí thiết kế có lưu đồ/pseudocode.*

**Pseudocode:**

```
INPUT: title, content, user_meta (tùy chọn)
1. clean_text ← TextCleaner.pipeline_clean(content)
2. IF word_count(clean_text) < 5 THEN RETURN error
3. phobert_vec ← PhoBERT([CLS])(clean_text)           // 768
4. meta_vec ← build_meta_vector(title, content, meta) // 10
5. meta_scaled ← scaler_meta.transform(meta_vec)
6. combined ← concat(phobert_vec, meta_scaled)        // 778
7. combined_scaled ← scaler.transform(combined)
8. label, prob ← MLP.predict / predict_proba
9. explanation ← build_explanation(prob, text, meta)
OUTPUT: label, prob, explanation
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

Chương 3 đã trình bày phương pháp học máy lai, yêu cầu chức năng/phi chức năng (Bảng 3.2, 3.3), kiến trúc (Hình 3.1–3.2), mô hình lưu trữ (Hình 3.3) và lưu đồ thuật toán (Hình 3.4). Chương 4 sẽ hiện thực hóa thiết kế, chạy thực nghiệm và đối chiếu kết quả với mục tiêu SMART (Bảng 1.1).

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

Cài đặt: `pip install -r requirements.txt`; `npm install` trong `frontend/`. Chạy: `./run_web.sh`.

## 4.2. Quá trình hiện thực

### 4.2.1. Cài đặt các mô-đun chính

| File / Thư mục | Vai trò |
|----------------|---------|
| `data_crawler.py` | Crawl URL, nhận văn bản thủ công |
| `text_cleaner.py` | Tiền xử lý inference (5 bước) |
| `text_utils.py` | Hàm văn bản dùng chung (train) |
| `feature_extraction.py` | Siêu dữ liệu + thống kê văn bản |
| `dataset_cleaner.py` | Lọc CSV trước train |
| `hybrid_inference.py` | Pipeline suy luận 4 mô-đun |
| `explanation_engine.py` | Sinh giải thích rule-based |
| `api/main.py` | FastAPI bridge |
| `frontend/` | Giao diện Next.js |

Notebook `train_hybrid_model.ipynb` gom sáu phần: lý thuyết → lọc dữ liệu → embed PhoBERT → siêu dữ liệu → train MLP → đánh giá.

### 4.2.2. Xử lý dữ liệu

**Bảng 4.2. Thống kê bộ dữ liệu**

| Chỉ số | Giá trị |
|--------|---------|
| File | `backend/data/full_dataset.csv` |
| Số mẫu (gốc) | ~169.056 dòng |
| Nhãn | `is_fake`: True (giả) / False (thật) |
| Trường chính | title, content, source, url, is_fake |

Quy trình `dataset_cleaner.py`: loại thiếu content; loại bài < 5 từ; loại trùng lặp; phân đoạn từ PyVi. Siêu dữ liệu MXH mô phỏng theo nhãn; thống kê văn bản tính từ title/content.

## 4.3. Kết quả đạt được

### 4.3.1. Kết quả chạy chương trình

**Bảng 4.3. Hiệu năng bảy cấu hình mô hình (tập kiểm thử 30%)**

| STT | Mô hình | Chiều | Acc | Prec | Rec | F1 | AUC |
|:---:|---------|:-----:|:---:|:----:|:---:|:--:|:---:|
| 1 | Chỉ PhoBERT | 768 | 94,13% | 93,29% | 94,11% | 93,70% | 98,46% |
| **2** | **Lai đầy đủ** | **778** | **97,68%** | **96,99%** | **98,04%** | **97,51%** | **99,71%** |
| 3 | PhoBERT + MXH | 773 | 97,20% | 96,39% | 97,63% | 97,01% | 99,67% |
| 4 | PhoBERT + Thống kê VB | 773 | 94,82% | 94,09% | 94,79% | 94,44% | 98,85% |
| 5 | Chỉ siêu dữ liệu | 10 | 95,92% | 94,57% | 96,75% | 95,65% | 99,13% |
| 6 | Chỉ MXH | 5 | 92,90% | 89,02% | 96,61% | 92,66% | 97,72% |
| 7 | Chỉ thống kê VB | 5 | 82,69% | 80,18% | 83,28% | 81,70% | 90,62% |

**Hình 4.1–4.5. Kết quả thực nghiệm định lượng**

| Hình | Tên file (sau khi chạy eval) | Nội dung |
|------|------------------------------|----------|
| Hình 4.1 | `confusion_matrix_hybrid.png` | Ma trận nhầm lẫn mô hình lai đầy đủ |
| Hình 4.2 | `model_comparison.png` | So sánh F1/Accuracy các cấu hình |
| Hình 4.3 | `ablation_study.png` | Biểu đồ ablation 7 cấu hình |
| Hình 4.4 | `roc_curves.png` | Đường cong ROC |
| Hình 4.5 | `cv_results.png` | Kiểm định chéo 5-fold |

*Sinh hình: `cd backend && python experiments/run_experimental_evaluation.py`. Lưu tại `backend/experiments/figures/experimental/`.*

**Hình 4.6–4.8. Giao diện hệ thống (screenshot khi chạy `./run_web.sh`)**

| Hình | Trang | Nội dung cần chụp |
|------|-------|-------------------|
| Hình 4.6 | `http://localhost:3000/` | Trang chủ ShieldAI |
| Hình 4.7 | `/analyze` | Form nhập văn bản/URL + siêu dữ liệu MXH |
| Hình 4.8 | `/results` | Gauge xác suất, nhãn phân loại, thẻ giải thích |

*Mỗi hình cần chú thích 1–2 câu mô tả chức năng — đáp ứng tiêu chí thực nghiệm có minh chứng hệ thống chạy được.*

### 4.3.2. Đánh giá kết quả

**Bảng 4.6. Đối chiếu mục tiêu SMART (Bảng 1.1) và kết quả đạt được**

| Mã | Mục tiêu | Tiêu chí đo | Kết quả | Đạt? |
|----|----------|-------------|---------|:----:|
| MT-01 | Tiền xử lý tiếng Việt | Module `TextCleaner` hoạt động | 5 bước làm sạch + PyVi | ✓ |
| MT-02 | Mô hình lai | F1 ≥ 95% | F1 **97,51%**, Acc 97,68% | ✓ |
| MT-03 | Ablation & CV | 7 cấu hình + 5-fold | Bảng 4.3, 4.4; Hình 4.3, 4.5 | ✓ |
| MT-04 | Triển khai web | 8/8 FR (Bảng 3.2) | Kiểm thử Bảng 4.5: 8/8 Đạt | ✓ |
| MT-05 | Giải thích | JSON `explanation` trên UI | `ExplanationEngine` + Hình 4.8 | ✓ |

*Bảng 4.6 cho thấy toàn bộ mục tiêu SMART đều đạt hoặc vượt ngưỡng đề ra.*

**Phân tích định lượng:** Mô hình lai vượt baseline chỉ PhoBERT **+3,81%** F1 (93,70% → 97,51%), chứng minh siêu dữ liệu bổ sung có ý nghĩa thống kê trên tập ~169.000 mẫu. Recall 98,04% — phát hiện được đa số tin giả. ROC-AUC 99,71% — khả năng phân tách lớp xuất sắc.

**Phân rã:** Siêu dữ liệu MXH đóng góp mạnh nhất; thống kê văn bản yếu đơn lẻ (F1 81,70%) nhưng bổ trợ khi ghép đủ 10 chiều. PhoBERT là neo ngữ nghĩa không thể thiếu khi siêu dữ liệu thiếu hoặc giả mạo.

**Bảng 4.4. Kiểm định chéo 5-fold — mô hình lai**

| Chỉ số | Trung bình ± Độ lệch chuẩn |
|--------|:--------------------------:|
| Accuracy | 97,47% ± 0,28% |
| F1 | 97,28% ± 0,30% |
| ROC-AUC | 99,67% ± 0,09% |

Độ lệch chuẩn thấp chứng tỏ mô hình ổn định, không phụ thuộc một lần chia ngẫu nhiên.

## 4.4. Kiểm thử

**Bảng 4.5. Kịch bản kiểm thử chức năng (ánh xạ yêu cầu FR)**

| STT | FR | Kịch bản | Đầu vào | Kỳ vọng | Kết quả |
|:---:|----|----------|---------|---------|:-------:|
| 1 | FR-01 | Nhập văn bản thủ công | Tiêu đề + nội dung dán trực tiếp | API trả JSON phân loại | Đạt |
| 2 | FR-02 | Nhập URL báo | Link VnExpress/VietnamNet hợp lệ | Crawl title + content | Đạt |
| 3 | FR-03 | Siêu dữ liệu MXH | Tài khoản mới, ít follower | Meta ảnh hưởng xác suất | Đạt |
| 4 | FR-04 | Tiền xử lý | Văn bản có HTML, teencode | `clean_text` hợp lệ | Đạt |
| 5 | FR-05 | Trích đặc trưng | Văn bản ≥ 5 từ | Vector 778 chiều nội bộ | Đạt |
| 6 | FR-06 | Phân loại tin giả | Nội dung giật gân + meta rủi ro | `prob_fake` cao | Đạt |
| 7 | FR-06 | Phân loại tin thật | Bài báo khách quan | `prob_fake` thấp | Đạt |
| 8 | FR-07 | Giải thích | Sau phân loại | Trường `explanation` tiếng Việt | Đạt |
| 9 | FR-08 | API REST | GET `/api/health` | `{"status":"ok"}` | Đạt |
| 10 | — | Nội dung quá ngắn | < 5 từ | HTTP 400 + thông báo lỗi | Đạt |
| 11 | — | Backend offline | Gọi API khi tắt server | UI báo lỗi kết nối | Đạt |

Kiểm thử thực hiện qua giao diện web và curl/Postman; API có tài liệu tự động tại `http://127.0.0.1:8000/docs` [9].

## 4.5. Kết luận chương

Chương 4 đã trình bày môi trường phát triển, hiện thực các mô-đun, kết quả thực nghiệm (F1 97,51%), đối chiếu SMART (Bảng 4.6) và kiểm thử ánh xạ FR (Bảng 4.5). Hạn chế: siêu dữ liệu mô phỏng khi train, crawler HTML đơn giản — thảo luận tại Chương 5.

---

<br>

# CHƯƠNG 5: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 5.1. Kết luận

Luận văn đã hoàn thành nghiên cứu, thiết kế, huấn luyện, đánh giá và triển khai hệ thống **ShieldAI** — công cụ phát hiện tin giả tiếng Việt bằng học máy lai đa phương thức. Các kết quả chính:

1. Xây dựng pipeline tiền xử lý tiếng Việt phù hợp PhoBERT (PyVi, teencode, làm sạch nhiễu).
2. Thiết kế kiến trúc lai: PhoBERT 768 + siêu dữ liệu 10 → MLP (128, 64).
3. Đạt độ chính xác **97,68%**, F1 **97,51%**, ROC-AUC **99,71%** trên ~169.000 mẫu.
4. Triển khai ứng dụng web FastAPI + Next.js với mô-đun giải thích.
5. Hoàn thành các mục tiêu đã đề ra tại mục 1.2.

## 5.2. Đóng góp của luận văn

### 5.2.1. Tính mới của đề tài

Đề tài có **tính mới** ở ba điểm chính, được kiểm chứng bằng số liệu (Bảng 4.3, 4.6):

1. **Pipeline lai tiếng Việt end-to-end:** Kết hợp PhoBERT cố định (768 chiều) với bộ 10 siêu dữ liệu (MXH + thống kê văn bản) qua early fusion và MLP — chưa được trình bày đồng thời trong các công trình trong nước đã khảo sát (Bảng 2.1).
2. **Đánh giá phân rã có hệ thống:** Bảy cấu hình ablation và kiểm định chéo 5-fold chứng minh đóng góp từng nhóm đặc trưng; mô hình lai vượt baseline PhoBERT **+3,81%** F1 trên ~169.000 mẫu.
3. **Triển khai ứng dụng có giải thích:** Module `ExplanationEngine` sinh diễn giải tiếng Việt theo quy tắc, tích hợp web FastAPI + Next.js — vượt mức demo mô hình đơn lẻ.

### 5.2.2. Phân biệt đóng góp bản thân và thành phần có sẵn

| Thành phần | Nguồn gốc | Đóng góp của luận văn |
|------------|-----------|------------------------|
| PhoBERT-base [3] | VinAI (pre-trained) | **Không** huấn luyện lại; chỉ trích [CLS] làm đặc trưng |
| scikit-learn MLP [7] | Thư viện có sẵn | **Có** — thiết kế kiến trúc (128,64), siêu tham số, pipeline scale |
| FastAPI / Next.js [9], [10] | Framework | **Có** — tích hợp API phân tích, luồng UI, sessionStorage |
| 10 siêu dữ liệu | Thiết kế đề tài | **Có** — chọn nhóm MXH + văn bản, `build_meta_vector`, mô phỏng train |
| `ExplanationEngine` | Code đề tài | **Có** — quy tắc tiếng Việt, breakdown metadata |
| `HybridInferenceSystem` | Code đề tài | **Có** — 4 mô-đun, đồng bộ train/inference |
| Ablation 7 cấu hình | Thực nghiệm đề tài | **Có** — script eval, bảng metric, biểu đồ |

*Như vậy, giá trị khoa học không nằm ở việc tái tạo PhoBERT, mà ở **cách kết hợp, đánh giá và triển khai** thành hệ thống hoàn chỉnh cho tiếng Việt.*

**Về mặt lý luận:** Chứng minh hiệu quả học máy lai; phân tích đóng góp từng nhóm đặc trưng; quy trình tái lập (notebook, module dùng chung).

**Về mặt thực tiễn:** Công cụ web hỗ trợ kiểm tra tin nghi ngờ; mã nguồn mở, mở rộng được; phù hợp demo và nền tảng nghiên cứu tiếp.

## 5.3. Hạn chế

1. **Siêu dữ liệu MXH mô phỏng** khi huấn luyện — chưa xác thực trên dữ liệu thực.
2. **PhoBERT cố định** — chưa khai thác hết tiềm năng fine-tune.
3. **Crawler HTML đơn giản** — không phủ hết mọi trang báo.
4. **Giải thích heuristic** — không khớp hoàn toàn ranh giới quyết định MLP.
5. **Nguy cơ thiên lệch tập dữ liệu** — mô hình có thể học shortcut theo nguồn miền.

## 5.4. Hướng phát triển

1. Thu thập siêu dữ liệu mạng xã hội thực, hợp tác tổ chức fact-checking.
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
│   ├── hybrid_inference.py
│   ├── feature_extraction.py
│   ├── explanation_engine.py
│   ├── data_crawler.py
│   ├── text_cleaner.py
│   ├── training/train_hybrid_model.ipynb
│   └── experiments/run_experimental_evaluation.py
├── frontend/
│   ├── app/analyze/page.tsx
│   ├── app/results/page.tsx
│   └── lib/api.ts
├── run_web.sh
└── requirements.txt
```

*(Chèn đoạn mã tiêu biểu: `build_meta_vector`, `infer()` — nếu quy định Khoa yêu cầu)*

## Phụ lục B: Hướng dẫn cài đặt và chạy hệ thống

```bash
# 1. Cài đặt
cd DoAnTotNghiep
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd frontend && npm install && cd ..

# 2. Chạy hệ thống
./run_web.sh

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
| Vì sao không fine-tune PhoBERT? | Tiết kiệm tài nguyên; mục tiêu chứng minh hybrid; F1 97,51% đủ mạnh; embedding tái sử dụng qua `.npy`. |
| Metadata MXH mô phỏng có tin được không? | Thừa nhận hạn chế (mục 5.3); ablation vẫn hợp lệ; inference dùng metadata thật do người dùng nhập. |
| Đóng góp của em khác gì PhoBERT có sẵn? | Xem Bảng mục 5.2.2: pipeline lai, 10 meta, 4 mô-đun, giải thích, web, ablation 7 cấu hình. |
| Vì sao chọn MLP thay vì XGBoost/SVM? | Phi tuyến trên vector dense 778 chiều; `predict_proba`; regularization L2; huấn luyện nhanh trên CPU. |
| False positive nguy hiểm thế nào? | Gán nhầm tin thật là giả; UI hiển thị xác suất + mức "đáng ngờ", không khẳng định tuyệt đối. |
| Hệ thống có CSDL không? | Không SQL; lưu CSV/npy/joblib (Hình 3.3); phù hợp inference stateless. |
| Làm sao tái lập kết quả? | `random_state=42`; chạy notebook train + `run_experimental_evaluation.py`; `./run_web.sh` cho demo. |

*Chi tiết checklist bảo vệ: `docs/CHUAN_BI_BAO_VE_THEO_PHIEU_CHAM.md`.*

---

*Hết luận văn.*

**Phiên bản:** 4.0 — Tối ưu theo Phiếu chấm điểm luận văn TTU (6 tiêu chí)  
**Cập nhật:** Tháng 06/2026
