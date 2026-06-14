# Lý do lựa chọn phương án — Dự án ShieldAI

Tài liệu này giải thích **chi tiết từng quyết định thiết kế** trong đồ án phát hiện tin giả tiếng Việt: chọn gì, bỏ gì, và **tại sao** — phù hợp để đưa vào Chương phương pháp / thiết kế hệ thống trong luận văn.

---

## Mục lục

1. [Bài toán và hướng tiếp cận tổng thể](#1-bài-toán-và-hướng-tiếp-cận-tổng-thể)
2. [Vì sao chọn mô hình lai (Hybrid)?](#2-vì-sao-chọn-mô-hình-lai-hybrid)
3. [Vì sao chọn PhoBERT?](#3-vì-sao-chọn-phobert)
4. [Vì sao dùng PhoBERT frozen thay vì fine-tune?](#4-vì-sao-dùng-phobert-frozen-thay-vì-fine-tune)
5. [Vì sao thêm metadata phi văn bản?](#5-vì-sao-thêm-metadata-phi-văn-bản)
6. [Vì sao mô phỏng metadata MXH?](#6-vì-sao-mô-phỏng-metadata-mxh)
7. [Vì sao chọn MLP làm bộ phân loại?](#7-vì-sao-chọn-mlp-làm-bộ-phân-loại)
8. [Vì sao ghép vector bằng Concatenation?](#8-vì-sao-ghép-vector-bằng-concatenation)
9. [Vì sao dùng StandardScaler?](#9-vì-sao-dùng-standardscaler)
10. [Vì sao tiền xử lý văn bản như vậy?](#10-vì-sao-tiền-xử-lý-văn-bản-như-vậy)
11. [Vì sao kiến trúc hệ thống 4 module?](#11-vì-sao-kiến-trúc-hệ-thống-4-module)
12. [Vì sao FastAPI + Next.js?](#12-vì-sao-fastapi--nextjs)
13. [Vì sao giải thích rule-based thay vì SHAP/LIME?](#13-vì-sao-giải-thích-rule-based-thay-vì-shaplime)
14. [Vì sao thiết kế thí nghiệm như vậy?](#14-vì-sao-thiết-kế-thí-nghiệm-như-vậy)
15. [Kết luận — phương án cuối cùng](#15-kết-luận--phương-án-cuối-cùng)

---

## 1. Bài toán và hướng tiếp cận tổng thể

### Bài toán

Phân loại nhị phân một bài viết tiếng Việt thành **tin thật** hoặc **tin giả**, dựa trên:

- Nội dung văn bản (tiêu đề + thân bài)
- Ngữ cảnh lan truyền trên mạng xã hội (tài khoản, tốc độ share, phản ứng cộng đồng…)

### Thách thức riêng của tiếng Việt

| Thách thức | Hệ quả |
|------------|--------|
| Không tách từ bằng khoảng trắng | Cần tokenizer/tách từ chuyên biệt (PyVi) |
| Teencode, viết tắt, emoji | Cần bước chuẩn hóa trước khi đưa vào mô hình |
| Thiếu mô hình NLP lớn pre-train sẵn như tiếng Anh | PhoBERT là lựa chọn phù hợp nhất hiện có |
| Tin giả thường lan truyền trên MXH | Chỉ phân tích văn bản là chưa đủ |

### Hướng tiếp cận được chọn

**Mô hình lai đa phương thức (Multimodal Hybrid):**

```
Nội dung văn bản ──► PhoBERT ──► Vector 768 chiều
                                        │
Metadata + thống kê ──► 10 đặc trưng ───┤
                                        ▼
                              Concatenation (778 chiều)
                                        │
                                        ▼
                              MLP (128, 64) ──► Tin thật / Tin giả
```

Đây là phương án cân bằng giữa **độ chính xác**, **khả năng triển khai** và **phạm vi đồ án tốt nghiệp**.

---

## 2. Vì sao chọn mô hình lai (Hybrid)?

### Lý thuyết

Tin giả không chỉ khác ở **nội dung ngữ nghĩa** mà còn khác ở **cách lan truyền**:

- Tài khoản mới, ít follower, không verified
- Tiêu đề giật gân, nhiều dấu chấm than
- Lan truyền nhanh, phản ứng tiêu cực cao

Một mô hình **chỉ đọc văn bản** có thể bỏ sót các tín hiệu này. Ngược lại, mô hình **chỉ dùng metadata** không hiểu được ngữ nghĩa sâu (ví dụ: tin giả viết khéo, giọng văn khách quan).

### Bằng chứng từ thí nghiệm (trên tập test)

| Mô hình | Accuracy | F1 | ROC-AUC |
|---------|----------|-----|---------|
| Chỉ PhoBERT (768 chiều) | 94.13% | 93.70% | 98.46% |
| **Hybrid đầy đủ (778 chiều)** | **97.68%** | **97.51%** | **99.71%** |
| Chỉ metadata (10 chiều) | 95.92% | 95.65% | 99.13% |

**Kết luận:** Hybrid vượt trội so với chỉ-văn-bản (+3.5% accuracy, +3.8% F1). Điều này chứng minh hai nguồn thông tin **bổ sung cho nhau**, không thay thế hoàn toàn.

### Vì sao không chọn phương án khác?

| Phương án bị loại | Lý do |
|-------------------|-------|
| Chỉ TF-IDF / Bag-of-Words | Không nắm được ngữ cảnh, đồng nghĩa, cấu trúc câu tiếng Việt |
| Chỉ metadata | Không đọc được nội dung thực sự của bài viết |
| End-to-end deep learning phức tạp (Transformer + GNN…) | Vượt phạm vi đồ án, khó giải thích, cần GPU mạnh |
| Ensemble nhiều mô hình lớn | Chi phí inference cao, khó triển khai web realtime |

---

## 3. Vì sao chọn PhoBERT?

### PhoBERT là gì?

`vinai/phobert-base` là mô hình BERT được **pre-train trên corpus tiếng Việt lớn** (khoảng 20GB văn bản), do VinAI Research phát triển. Kiến trúc:

- 12 lớp Transformer
- Hidden size: 768
- 12 attention heads
- Vocab size: ~64.000 token

### So sánh với các lựa chọn khác

| Mô hình | Ưu điểm | Nhược điểm | Quyết định |
|---------|---------|------------|------------|
| **PhoBERT-base** | Pre-train tiếng Việt, miễn phí, cộng đồng lớn | Cần GPU/RAM khi inference | **Chọn** |
| mBERT (multilingual) | Hỗ trợ nhiều ngôn ngữ | Tiếng Việt không phải trọng tâm, kém hơn PhoBERT trên task VN | Loại |
| BERT tiếng Anh | Mạnh trên tiếng Anh | Không phù hợp tiếng Việt | Loại |
| PhoBERT-large | Embedding 1024 chiều, mạnh hơn | Gấp đôi thời gian inference, cần RAM lớn hơn | Loại (đồ án) |
| LLM (GPT, Gemini…) | Rất mạnh ngôn ngữ | Quá nặng, chi phí cao, khó kiểm soát, không phù hợp phân loại có giám sát | Loại |

### Cách dùng PhoBERT trong dự án

Lấy vector **[CLS]** từ lớp cuối (`last_hidden_state[:, 0, :]`) — vector 768 chiều đại diện cho **toàn bộ ngữ cảnh câu/đoạn văn**.

**Tại sao [CLS] mà không pooling trung bình?**

- [CLS] được BERT/PhoBERT thiết kế sẵn để đại diện câu trong các task phân loại
- Phổ biến trong literature fake news detection
- Đơn giản, ổn định, dễ tái lập

---

## 4. Vì sao dùng PhoBERT frozen thay vì fine-tune?

### Hai phương án

| | **Frozen (đã chọn)** | Fine-tune end-to-end |
|--|---------------------|----------------------|
| Cách làm | Trích embedding 1 lần → train MLP riêng | Cập nhật trọng số PhoBERT + classifier |
| Thời gian train | Embedding ~1 giờ (CPU), MLP vài phút | Nhiều giờ–ngày, cần GPU |
| RAM/GPU | Inference cần load PhoBERT (~500MB) | Train cần GPU 8GB+ |
| Overfitting | Ít hơn (MLP nhỏ trên embedding cố định) | Dễ overfit nếu dataset không đủ lớn |
| Tái sử dụng | Embedding lưu `.npy`, train lại MLP nhanh | Phải train lại toàn bộ |

### Lý do chọn frozen

1. **Dataset ~169k mẫu** — đủ lớn để MLP học trên embedding cố định, nhưng fine-tune PhoBERT vẫn tốn kém và cần tuning hyperparameter phức tạp hơn.

2. **Mục tiêu đồ án** là chứng minh **phương pháp hybrid**, không phải đua SOTA fine-tuning. Kết quả 97.7% accuracy đã đủ mạnh.

3. **Triển khai thực tế:** Embedding có thể pre-compute offline; lúc inference chỉ cần 1 forward pass PhoBERT + MLP nhẹ.

4. **Notebook vẫn minh họa** cấu hình fine-tune (LR=2e-5, batch=16, epochs=5, AdamW) ở Phần 0 để tham khảo lý thuyết — nhưng pipeline thực tế dùng frozen.

---

## 5. Vì sao thêm metadata phi văn bản?

### Phân loại 10 đặc trưng

**Nhóm A — Metadata người dùng / lan truyền (5 chiều):**

| Đặc trưng | Ý nghĩa | Liên hệ tin giả |
|-----------|---------|-----------------|
| `account_age_days` | Tuổi tài khoản | Tài khoản mới thường spam tin giả |
| `followers` | Số người theo dõi | Follower thấp → độ tin cậy thấp |
| `is_verified` | Tích xanh | Nguồn chưa xác minh |
| `share_speed` | Tốc độ lan truyền | Tin giả thường viral nhanh |
| `angry_ratio` | Tỷ lệ phản ứng phẫn nộ | Kích động cảm xúc tiêu cực |

**Nhóm B — Thống kê văn bản (5 chiều):**

| Đặc trưng | Ý nghĩa | Liên hệ tin giả |
|-----------|---------|-----------------|
| `title_length` | Độ dài tiêu đề | Tiêu đề giật gân thường ngắn/cụt |
| `uppercase_ratio` | Tỷ lệ chữ IN HOA | Thao túng cảm xúc |
| `exclamation_count` | Số dấu `!` trong tiêu đề | Giật tít, cảnh báo giả |
| `question_count` | Số dấu `?` | Câu hỏi kích thích tò mò |
| `punctuation_density` | Mật độ dấu câu | Văn phong kích động |

### Ablation study — đóng góp từng nhóm

| Cấu hình | F1 (test) |
|----------|-----------|
| PhoBERT + 10 meta (đầy đủ) | **97.51%** |
| PhoBERT + 5 meta MXH | 97.01% |
| PhoBERT + 5 thống kê văn bản | 94.44% |
| Chỉ thống kê văn bản (5) | 81.70% |

**Nhận xét:**

- **Metadata MXH** đóng góp mạnh nhất (+~3% F1 so với chỉ thống kê văn bản khi kết hợp PhoBERT)
- **Thống kê văn bản** một mình yếu (81.7% F1) nhưng **bổ trợ tốt** khi ghép với PhoBERT
- Hai nhóm **bổ sung lẫn nhau** — đúng với giả thuyết hybrid

---

## 6. Vì sao mô phỏng metadata MXH?

### Thực tế dữ liệu

File `full_dataset.csv` chỉ có: `title`, `content`, `is_fake`, `source`, `url`… — **không có** dữ liệu Facebook thật (tuổi tài khoản, share speed, v.v.).

### Phương án xử lý

Mô phỏng 5 đặc trưng MXH bằng phân phối ngẫu nhiên **có điều kiện theo nhãn** `is_fake`:

```python
# Tin giả: tài khoản mới, ít follower, ít verified, share nhanh, angry cao
# Tin thật: tài khoản lâu năm, nhiều follower, verified cao hơn, angry thấp hơn
```

(Xem `backend/feature_extraction.py` — hàm `simulate_user_signals`)

### Vì sao chấp nhận mô phỏng?

| Lý do | Giải thích |
|-------|------------|
| Không có API MXH công khai | Facebook/ TikTok không cung cấp metadata bài đăng cho nghiên cứu |
| Giữ được kiến trúc hybrid | MLP học được **mối quan hệ** giữa metadata và nhãn |
| Phù hợp inference | Lúc dùng web, người dùng **nhập metadata thật** → mô hình áp dụng được |
| Có tiền lệ nghiên cứu | Nhiều paper fake news dùng synthetic social features khi thiếu dữ liệu thật |

### Hạn chế cần ghi trong luận văn

> Metadata MXH trong giai đoạn train là **mô phỏng**, không phải dữ liệu thực. Kết quả thí nghiệm phản ánh khả năng mô hình **học tín hiệu bổ sung** khi có metadata, chứ chưa validate trên dữ liệu MXH production.

---

## 7. Vì sao chọn MLP làm bộ phân loại?

### Cấu hình đã chọn

```python
MLPClassifier(
    hidden_layer_sizes=(128, 64),
    activation='relu',
    solver='adam',
    max_iter=500,
    alpha=0.1,           # L2 regularization
    early_stopping=True,
    random_state=42,
)
```

### So sánh với các classifier khác

| Classifier | Ưu | Nhược | Quyết định |
|------------|-----|-------|------------|
| **MLP (128, 64)** | Học phi tuyến, nhanh trên vector 778 chiều, `predict_proba` cho xác suất | Cần scale feature | **Chọn** |
| Logistic Regression | Đơn giản, giải thích được hệ số | Chỉ mô hình tuyến tính, kém trên embedding 768 chiều | Loại |
| Random Forest / XGBoost | Mạnh trên tabular | Chậm hơn với 778 chiều dense, overfit dễ trên high-dim | Không chọn |
| SVM | Mạnh lý thuyết | Chậm với ~169k mẫu × 778 chiều | Loại |
| Fine-tune PhoBERT + linear head | End-to-end | Xem mục 4 | Loại |

### Vì sao (128, 64)?

- **778 input → 128 → 64 → 2 output:** đủ sâu để học tương tác phi tuyến giữa PhoBERT và metadata, nhưng không quá lớn → tránh overfit
- **ReLU:** activation phổ biến, hội tụ nhanh
- **alpha=0.1:** regularization L2 mạnh — embedding 768 chiều dễ overfit nếu không regularize
- **early_stopping=True:** dừng sớm khi validation loss không cải thiện

### Kết quả 5-fold CV (Hybrid)

| Metric | Mean ± Std |
|--------|------------|
| Accuracy | 97.47% ± 0.28% |
| F1 | 97.28% ± 0.30% |
| ROC-AUC | 99.67% ± 0.09% |

Độ lệch chuẩn thấp → mô hình **ổn định**, không phụ thuộc vào một split ngẫu nhiên.

---

## 8. Vì sao ghép vector bằng Concatenation?

### Các phương án fusion

| Phương án | Mô tả | Ưu / Nhược |
|-----------|-------|------------|
| **Concatenation** | `[PhoBERT_768 ; Meta_10]` → 778 chiều | Đơn giản, MLP tự học trọng số từng nhánh |
| Attention fusion | Meta làm query, PhoBERT làm key/value | Phức tạp, cần train end-to-end |
| Gating / Weighted sum | Học trọng số động giữa 2 nhánh | Thêm hyperparameter, khó debug |
| Cross-modal Transformer | Transformer trên 2 modality | Quá nặng cho đồ án |

### Lý do chọn Concatenation

1. **Early fusion đơn giản** — phù hợp khi 2 nhánh đã được extract sẵn
2. MLP `(128, 64)` đủ capacity để học **tương tác chéo** giữa chiều ngữ nghĩa và chiều metadata
3. Dễ **tái lập inference:** scale meta riêng → nối → scale toàn bộ → predict
4. Ablation study chứng minh fusion này **hiệu quả** (97.7% vs 94.1% text-only)

---

## 9. Vì sao dùng StandardScaler?

### Hai scaler trong pipeline

| Scaler | Áp dụng lên | File lưu |
|--------|-------------|----------|
| `scaler_meta` | 10 chiều metadata | `hybrid_scaler_meta.joblib` |
| `scaler_combined` | 778 chiều sau concat | `hybrid_scaler.joblib` |

### Lý do

- **PhoBERT embedding** có phân phối khác **metadata** (tuổi tài khoản: 1–3650, angry_ratio: 0–1, embedding: giá trị âm/dương nhỏ)
- Không scale → MLP ưu tiên chiều có magnitude lớn, bỏ qua chiều quan trọng nhưng nhỏ
- **StandardScaler** (z-score: mean=0, std=1) là chuẩn cho MLP và neural network
- Scale metadata **trước** concat, rồi scale **toàn bộ** sau — khớp giữa train và inference

---

## 10. Vì sao tiền xử lý văn bản như vậy?

### Pipeline inference (`text_cleaner.py`)

```
Văn bản thô
  → Xóa HTML, URL
  → Chuẩn hóa teencode (ko→không, wa→quá…)
  → Lowercase
  → Xóa emoji, ký tự đặc biệt
  → Tách từ PyVi (người_dùng)
```

### Pipeline train (`text_utils.py`)

```
Lowercase → Xóa URL → Tách từ PyVi
```

(Huấn luyện ít bước hơn vì dataset báo chí đã tương đối sạch)

### Lý do từng bước

| Bước | Tại sao |
|------|---------|
| **PyVi tokenization** | PhoBERT vocab được xây trên văn bản đã tách từ (`word_segment`). Không tách từ → tokenization sai → embedding kém |
| **Xóa URL/HTML** | URL không mang thông tin phân loại, HTML làm nhiễu |
| **Teencode** | Tin giả MXH thường dùng ngôn ngữ trẻ (`wa`, `ko`, `share ngay`) — chuẩn hóa giúp PhoBERT hiểu |
| **Lowercase** | PhoBERT và PyVi hoạt động tốt hơn với chữ thường |
| **Xóa emoji** | Emoji không có trong vocab PhoBERT, gây `<unk>` token |

### Vì sao không dùng underthesea / VnCoreNLP?

PyVi đủ nhẹ, cài đặt đơn giản (`pip install pyvi`), tốc độ chấp nhận được cho inference realtime. Các toolkit nặng hơn (VnCoreNLP cần Java) tăng độ phức tạp triển khai mà cải thiện không đáng kể cho task này.

---

## 11. Vì sao kiến trúc hệ thống 4 module?

Thiết kế trong `hybrid_inference.py` theo luận văn mục 3.3:

```
Module 1: Thu thập & tiền xử lý  (DataCrawler + TextCleaner)
Module 2: Trích xuất đặc trưng  (PhoBERT ∥ Metadata) — song song
Module 3: Hợp nhất (Fusion)     (Concatenation + Scaler)
Module 4: Phân loại & giải thích (MLP + ExplanationEngine)
```

### Lý do chia module

| Lý do | Chi tiết |
|-------|----------|
| **Separation of concerns** | Mỗi module một nhiệm vụ — dễ test, debug, mở rộng |
| **Khớp luận văn** | Mô tả kiến trúc rõ ràng trong Chương thiết kế |
| **Song song Module 2** | PhoBERT và metadata độc lập → có thể tối ưu/cache riêng |
| **Tái sử dụng** | `feature_extraction.py`, `text_utils.py` dùng chung train/eval/inference |

---

## 12. Vì sao FastAPI + Next.js?

### Kiến trúc tách frontend / backend

```
Next.js (port 3000)  ←→  FastAPI (port 8000)  ←→  HybridInferenceSystem
```

### Vì sao không Streamlit?

Streamlit phù hợp prototype nhanh nhưng:

- UI hạn chế, khó tùy biến giao diện chuyên nghiệp
- Không tách biệt frontend/backend rõ ràng
- Khó scale và deploy production

→ Dự án đã **loại bỏ Streamlit**, chỉ dùng Next.js.

### Vì sao FastAPI (backend)?

| Ưu điểm | Ứng dụng |
|---------|----------|
| Async, nhanh | Phục vụ API phân loại |
| Pydantic validation | Kiểm tra payload `mode`, `text`, `meta` |
| Auto OpenAPI docs | `/docs` để test API |
| Python native | Gọi trực tiếp PyTorch, PhoBERT, sklearn |

### Vì sao Next.js (frontend)?

| Ưu điểm | Ứng dụng |
|---------|----------|
| React + TypeScript | UI type-safe, component tái sử dụng |
| App Router | Trang `/`, `/analyze`, `/results` |
| Tailwind + Framer Motion | Giao diện hiện đại, animation mượt |
| Tách biệt API | Frontend gọi backend qua REST, dễ deploy riêng |

---

## 13. Vì sao giải thích rule-based thay vì SHAP/LIME?

### Phương án đã chọn

`explanation_engine.py` — quy tắc heuristic:

- Quét pattern văn bản (`CẢNH BÁO`, `chia sẻ ngay`, nhiều `!!!`)
- Đánh giá metadata (tài khoản mới, share speed cao, không verified)
- Tóm tắt định tính nhánh PhoBERT (không giải thích từng chiều 768)

### So sánh

| Phương án | Ưu | Nhược |
|-----------|-----|-------|
| **Rule-based (đã chọn)** | Dễ hiểu với người dùng phổ thông, nhanh, không cần GPU thêm | Không phản ánh chính xác trọng số MLP |
| SHAP trên MLP | Giải thích mathematically | 778 chiều → khó diễn giải cho user |
| LIME | Local explanation | Không ổn định, chậm mỗi request |
| Attention visualization | Trực quan PhoBERT | Chỉ giải thích nhánh text, bỏ metadata |

### Lý do chọn rule-based

1. **Đối tượng người dùng** là công dân đọc tin — cần câu tiếng Việt dễ hiểu, không phải biểu đồ SHAP
2. **Tin giả có pattern rõ** (giật gân, kêu gọi share, tài khoản lạ) — rule bắt được các pattern này tốt
3. **PhoBERT 768 chiều** gần như black box — rule-based bổ sung lớp giải thích **ở mức ứng dụng**
4. Phù hợp phạm vi đồ án — không cần triển khai XAI phức tạp

---

## 14. Vì sao thiết kế thí nghiệm như vậy?

### 7 cấu hình mô hình (ablation)

| # | Cấu hình | Mục đích |
|---|----------|----------|
| 1 | Chỉ PhoBERT | Baseline ngữ nghĩa |
| 2 | Hybrid đầy đủ | **Mô hình đề xuất** |
| 3 | PhoBERT + MXH | Đo đóng góp metadata người dùng |
| 4 | PhoBERT + thống kê VB | Đo đóng góp đặc trưng văn bản |
| 5 | Chỉ metadata 10 | Trần trên của metadata |
| 6 | Chỉ MXH 5 | Riêng nhóm MXH |
| 7 | Chỉ thống kê VB 5 | Riêng nhóm văn bản |

### Các metric

| Metric | Vì sao dùng |
|--------|-------------|
| **Accuracy** | Tổng quan, dễ trình bày |
| **Precision** | Quan trọng — gán nhầm tin thật là giả gây hại uy tín |
| **Recall** | Bắt được nhiều tin giả nhất có thể |
| **F1** | Cân bằng Precision/Recall |
| **ROC-AUC** | Đánh giá khả năng phân tách ở mọi ngưỡng |
| **5-fold CV** | Kiểm tra ổn định, tránh may rủi do 1 lần split |

### Train/test split

- **70/30**, `random_state=42`, stratified — giữ tỷ lệ tin giả/thật
- Confusion matrix trên tập test — nhìn loại lỗi False Positive / False Negative

---

## 15. Kết luận — phương án cuối cùng

### Tóm tắt quyết định thiết kế

| Thành phần | Lựa chọn | Lý do chính |
|------------|----------|-------------|
| NLP backbone | PhoBERT-base frozen | Pre-train tiếng Việt, cân bằng hiệu năng/tài nguyên |
| Phân loại | MLP (128, 64) | Phi tuyến, nhanh, regularization tốt |
| Fusion | Concatenation | Đơn giản, hiệu quả đã chứng minh |
| Metadata | 10 chiều (5 MXH + 5 VB) | Bổ sung tín hiệu ngoài ngữ nghĩa |
| Tiền xử lý | PyVi + teencode + làm sạch | Phù hợp tiếng Việt và PhoBERT vocab |
| Backend | FastAPI | Python ML stack, API chuẩn |
| Frontend | Next.js 14 | UI chuyên nghiệp, tách biệt backend |
| Giải thích | Rule-based heuristic | Dễ hiểu cho người dùng cuối |
| Đánh giá | 7 ablation + 5-fold CV | Chứng minh có cơ sở khoa học |

### Số liệu cốt lõi (Hybrid vs Text-only)

```
                    Text-only    Hybrid      Cải thiện
Accuracy            94.13%       97.68%      +3.55%
F1                  93.70%       97.51%      +3.81%
ROC-AUC             98.46%       99.71%      +1.25%
CV F1 (mean±std)    93.27±0.32%  97.28±0.30% +4.01%
```

### Hạn chế cần thừa nhận

1. Metadata MXH **mô phỏng** khi train — chưa validate trên dữ liệu MXH thực
2. PhoBERT **không fine-tune** — có thể cải thiện thêm nếu có GPU
3. Crawler HTML **đơn giản** — không phủ hết mọi trang báo
4. Giải thích **heuristic** — không phải XAI formal

---

*Tài liệu bổ sung cho `HUONG_DAN_THUC_HIEN_DU_AN.md` — cập nhật: tháng 6/2026.*
