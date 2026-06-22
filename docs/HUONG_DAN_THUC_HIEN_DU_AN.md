# Hướng dẫn thực hiện dự án ShieldAI

**Phát hiện tin giả tiếng Việt bằng PhoBERT + MLP (text-only)**

Tài liệu này mô tả **toàn bộ quy trình** từ thu thập dữ liệu → huấn luyện → đánh giá → triển khai web, phù hợp cho tiểu luận tốt nghiệp.

---

## Mục lục

1. [Tổng quan dự án](#1-tổng-quan-dự-án)
2. [Cấu trúc thư mục](#2-cấu-trúc-thư-mục)
3. [Chuẩn bị môi trường](#3-chuẩn-bị-môi-trường)
4. [Thu thập và chuẩn bị dữ liệu](#4-thu-thập-và-chuẩn-bị-dữ-liệu)
5. [Huấn luyện mô hình](#5-huấn-luyện-mô-hình)
6. [Đánh giá thực nghiệm](#6-đánh-giá-thực-nghiệm)
7. [Xây dựng backend suy luận](#7-xây-dựng-backend-suy-luận)
8. [Xây dựng giao diện web](#8-xây-dựng-giao-diện-web)
9. [Chạy hệ thống hoàn chỉnh](#9-chạy-hệ-thống-hoàn-chỉnh)
10. [Kiểm thử thủ công](#10-kiểm-thử-thủ-công)
11. [Lưu ý quan trọng cho luận văn](#11-lưu-ý-quan-trọng-cho-luận-văn)
12. [Xử lý sự cố thường gặp](#12-xử-lý-sự-cố-thường-gặp)

---

## 1. Tổng quan dự án

### 1.1. Mục tiêu

Xây dựng công cụ **phân tích và phát hiện tin giả tiếng Việt**, kết hợp:

| Thành phần | Mô tả |
|------------|-------|
| **PhoBERT-base** | Trích xuất embedding ngữ cảnh 768 chiều từ nội dung bài viết |
| **MLP `(128, 64)`** | Phân loại nhị phân: tin thật / tin giả |
| **Verdict 3 mức** | Tin thật / Đáng ngờ / Tin giả (ngưỡng 35% / 75%) |
| **Giải thích rule-based** | Trình bày lý do phân loại cho người dùng |

### 1.2. Kiến trúc hệ thống

```
Người dùng (Web)
      │
      ▼
Next.js Frontend  ──POST /api/analyze──►  FastAPI Backend
      │                                        │
      │                                        ▼
      │                              PhoBERTInferenceSystem
      │                              ┌─────────────────────┐
      │                              │ Module 1: Crawler   │
      │                              │ + preprocess_text   │
      │                              │ Module 2: PhoBERT   │
      │                              │ Module 3: MLP + XAI │
      │                              └─────────────────────┘
      ▼
Trang kết quả (xác suất + giải thích)
```

### 1.3. Công nghệ sử dụng

| Lớp | Công nghệ |
|-----|-----------|
| Backend | Python 3, FastAPI, PyTorch, Transformers, scikit-learn |
| Mô hình NLP | `vinai/phobert-base` |
| Frontend | Next.js 14, TypeScript, Tailwind CSS, Framer Motion |
| Huấn luyện | Jupyter Notebook |

---

## 2. Cấu trúc thư mục

```
DoAnTotNghiep/
├── backend/
│   ├── api/main.py                 # FastAPI — API phân tích
│   ├── data_crawler.py             # Crawl URL / nhận văn bản thủ công
│   ├── text_utils.py               # preprocess_text — train + inference
│   ├── text_cleaner.py             # Wrapper tương thích
│   ├── dataset_cleaner.py          # Làm sạch CSV trước train
│   ├── phobert_inference.py        # Pipeline suy luận
│   ├── verdict.py                  # Phân loại 3 mức
│   ├── explanation_engine.py       # Sinh giải thích kết quả
│   ├── data/
│   │   └── full_dataset.csv        # Bộ dữ liệu gốc (10.617 bản ghi → 10.609 sau lọc)
│   ├── models/                     # Mô hình đã train (.joblib, .npy)
│   ├── training/
│   │   └── train_phobert_model.ipynb  # Notebook train duy nhất
│   └── experiments/
│       └── run_experimental_evaluation.py  # Đánh giá thực nghiệm
├── frontend/                       # Giao diện Next.js
├── scripts/                        # Script chạy dự án
├── requirements.txt                # Thư viện Python
├── setup.sh / run.sh              # Cài đặt & chạy (all | api | web | test)
└── docs/                           # Tài liệu
```

---

## 3. Chuẩn bị môi trường

### Bước 3.1 — Cài Python và Node.js

Yêu cầu tối thiểu:

- **Python** ≥ 3.10
- **Node.js** ≥ 18
- **RAM** ≥ 8 GB (khuyến nghị 16 GB khi chạy PhoBERT)
- **GPU** (tùy chọn): tăng tốc embedding, không bắt buộc

### Bước 3.2 — Clone / mở dự án

```bash
cd /home/haminhchien/Documents/DoAnTotNghiep
```

### Bước 3.3 — Tạo môi trường ảo Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Bước 3.4 — Cài Jupyter (cho huấn luyện)

```bash
pip install jupyterlab
```

### Bước 3.5 — Cài dependencies frontend

```bash
cd frontend
npm install
cd ..
```

### Bước 3.6 — Kiểm tra cài đặt

```bash
source venv/bin/activate
python -c "import torch, transformers, sklearn; print('OK')"
node -v && npm -v
```

---

## 4. Thu thập và chuẩn bị dữ liệu

### Bước 4.1 — Hiểu bộ dữ liệu

File: `backend/data/full_dataset.csv`

| Chỉ số | Giá trị |
|--------|---------|
| Số bản ghi gốc | **10.617** bài |
| Sau lọc (`dataset_cleaner.py`) | **10.609** mẫu |
| Tập kiểm thử hold-out (30%) | **~3.183** mẫu |
| Lĩnh vực | Y tế, sức khỏe, COVID (tiếng Việt) |

| Cột quan trọng | Ý nghĩa |
|----------------|---------|
| `title` | Tiêu đề bài viết |
| `content` | Nội dung đầy đủ |
| `is_fake` | Nhãn: `True` = tin giả, `False` = tin thật |
| `source`, `url`, `published_at` | Thông tin nguồn (tham khảo) |

### Bước 4.2 — Làm sạch dữ liệu

Chạy script hoặc dùng trực tiếp trong notebook (Phần 1):

```bash
source venv/bin/activate
python -m backend.dataset_cleaner
```

Script thực hiện:

1. Bỏ dòng thiếu `content`
2. Bỏ bài quá ngắn (< 5 từ)
3. Bỏ trùng nội dung
4. Tách từ bằng PyVi → cột `content_segmented`

Kết quả lưu tại: `backend/data/full_dataset_cleaned.csv`

### Bước 4.3 — (Tùy chọn) Thu thập thêm dữ liệu

Nếu muốn mở rộng dataset:

1. Thu thập bài báo từ các nguồn uy tín (tin thật)
2. Thu thập tin giả từ các bộ dữ liệu công khai / fact-check
3. Gộp vào CSV với cùng schema: `title`, `content`, `is_fake`
4. Chạy lại `dataset_cleaner`

---

## 5. Huấn luyện mô hình

### Bước 5.1 — Mở notebook

```bash
source venv/bin/activate
./start_jupyter.sh
```

Mở file: `backend/training/train_phobert_model.ipynb`

### Bước 5.2 — Chạy lần lượt các phần trong notebook

| Phần | Nội dung | Đầu ra |
|------|----------|--------|
| **0** | Lý thuyết PhoBERT + MLP | Hiểu phương pháp |
| **1** | Nạp & lọc dữ liệu | DataFrame sạch |
| **2** | Nhúng PhoBERT-base | `phobert_base_features.npy`, `phobert_base_labels.npy` |
| **3** | (Bỏ qua metadata) | — |
| **4** | Train MLP trên embedding 768-d | `phobert_mlp_model.joblib`, `phobert_scaler.joblib` |
| **5** | Đánh giá thực nghiệm | Biểu đồ + bảng metrics |

### Bước 5.3 — Cấu hình quan trọng

Trong notebook, cell cấu hình:

```python
REGENERATE_EMBEDDINGS = False  # True = chạy lại embedding (~1 giờ trên CPU)
```

- **Lần đầu train:** đặt `REGENERATE_EMBEDDINGS = True`
- **Đã có file `.npy`:** giữ `False` để tiết kiệm thời gian

### Bước 5.4 — Quy trình train chi tiết

#### Phần 2 — Embedding PhoBERT

```
Văn bản đã tách từ
       │
       ▼
PhoBERT-base (frozen, không fine-tune)
       │
       ▼
Vector [CLS] 768 chiều  →  lưu .npy
```

#### Phần 4 — MLP text-only

```
Vector [CLS] 768 chiều
       │
       ▼
StandardScaler
       │
       ▼
MLP (128, 64) + ReLU + Adam
       │
       ▼
phobert_mlp_model.joblib
phobert_scaler.joblib
```

### Bước 5.5 — Kiểm tra file mô hình

Sau khi train xong, thư mục `backend/models/` phải có:

```
phobert_base_features.npy
phobert_base_labels.npy
phobert_mlp_model.joblib
phobert_scaler.joblib
```

---

## 6. Đánh giá thực nghiệm

### Bước 6.1 — Chạy script đánh giá

```bash
source venv/bin/activate
python3 -m backend.experiments.run_experimental_evaluation
```

Hoặc chạy **Phần 5** trong notebook.

### Bước 6.2 — Các thí nghiệm được thực hiện

| Thí nghiệm | Mục đích |
|------------|----------|
| Confusion matrix | Nhìn lỗi phân loại |
| ROC / AUC | Đánh giá khả năng phân tách lớp |
| 5-fold Cross-validation | Độ ổn định mô hình |

### Bước 6.3 — Kết quả lưu tại

```
backend/experiments/figures/experimental/
├── confusion_matrix_text_only.png
├── roc_curves.png
├── cv_summary.csv
├── cv_summary.json
├── metrics_summary.csv
└── metrics_summary.json
```

Dùng các biểu đồ và bảng số này cho **Chương kết quả thực nghiệm** trong luận văn.

---

## 7. Xây dựng backend suy luận

Backend đã được triển khai sẵn. Hiểu luồng xử lý:

### Module 1 — Thu thập & tiền xử lý

File: `backend/data_crawler.py`, `backend/text_utils.py`

- **Chế độ URL:** crawl HTML → trích tiêu đề + nội dung
- **Chế độ văn bản:** người dùng dán trực tiếp
- **Tiền xử lý:** `preprocess_text` (lowercase, xóa URL, PyVi)

### Module 2 — PhoBERT embedding

File: `backend/phobert_inference.py`

- PhoBERT → vector 768 chiều ([CLS])

### Module 3 — Phân loại & giải thích

- `phobert_scaler` + MLP → xác suất tin giả
- `verdict.py` → nhãn 3 mức
- `explanation_engine.py` → giải thích rule-based

### Test backend độc lập

```bash
source venv/bin/activate
python3 -m backend.phobert_inference
```

### Chạy API

```bash
./run.sh api
# Hoặc: source venv/bin/activate && uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
```

Kiểm tra: http://127.0.0.1:8000/api/health

---

## 8. Xây dựng giao diện web

Frontend Next.js tại thư mục `frontend/`.

### Các trang chính

| Route | Chức năng |
|-------|-----------|
| `/` | Trang chủ — giới thiệu ShieldAI |
| `/analyze` | Nhập văn bản hoặc URL (cần đăng nhập) |
| `/results` | Xác suất, verdict 3 mức, giải thích |
| `/history` | Lịch sử phân tích |

### Luồng frontend

```
/analyze  →  POST /api/analyze  →  lưu sessionStorage  →  /results
```

File quan trọng:

- `frontend/app/analyze/page.tsx` — form phân tích
- `frontend/app/results/page.tsx` — hiển thị kết quả
- `frontend/lib/api.ts` — gọi API backend
- `frontend/components/` — ResultGauge, ExplanationCard, ...

### Chạy frontend riêng

```bash
cd frontend
npm run dev
# http://localhost:3000
```

---

## 9. Chạy hệ thống hoàn chỉnh

### Cách nhanh nhất (khuyến nghị)

```bash
cd /home/haminhchien/Documents/DoAnTotNghiep
./run.sh
# hoặc: ./run.sh all
```

| Dịch vụ | URL |
|---------|-----|
| Giao diện web | http://localhost:3000 |
| API backend | http://127.0.0.1:8000 |
| Health check | http://127.0.0.1:8000/api/health |

### Chạy tách riêng (debug)

Terminal 1 — Backend:

```bash
./run.sh api
```

Terminal 2 — Frontend:

```bash
./run.sh web
```

---

## 10. Kiểm thử thủ công

### 10.1 — Test qua giao diện web

1. Mở http://localhost:3000/analyze
2. Chọn tab **Văn bản**
3. Dán mẫu tin giả hoặc tin thật
4. Nhấn **Phân tích ngay**
5. Xem kết quả tại `/results`

### 10.2 — Test API bằng curl

```bash
curl -X POST http://127.0.0.1:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "text",
    "title": "Tin test",
    "text": "CẢNH BÁO KHẨN CẤP!!! Tin cực hot chia sẻ gấp!!!!",
    "meta": {
      "account_age_days": 2,
      "followers": 10,
      "is_verified": 0,
      "share_speed": 65,
      "angry_ratio": 0.8
    }
  }'
```

### 10.3 — Test crawl URL

```bash
curl -X POST http://127.0.0.1:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"mode": "url", "url": "https://vnexpress.net/..."}'
```

---

## 11. Lưu ý quan trọng cho luận văn

### 11.1 — Pipeline thống nhất

Hàm `preprocess_text` trong `text_utils.py` phải được dùng cho **cả train và inference**. Ghi rõ trong luận văn để tránh lệch pipeline.

### 11.2 — PhoBERT frozen, không fine-tune

Đề tài dùng PhoBERT-base ở chế độ **frozen** (trích embedding), phân loại bằng MLP sklearn — không fine-tune end-to-end.

### 11.3 — Giải thích rule-based

Phần giải thích kết quả (`explanation_engine.py`) dựa trên **quy tắc heuristic**, không phải SHAP/LIME. Cần mô tả đúng trong phần thiết kế hệ thống.

### 11.4 — Giới hạn crawler

Crawler HTML đơn giản (BeautifulSoup), có thể **không trích xuất được** một số trang báo có cấu trúc phức tạp. Khuyến nghị người dùng dán văn bản thủ công khi URL không hoạt động.

---

## 12. Xử lý sự cố thường gặp

| Vấn đề | Nguyên nhân | Cách xử lý |
|--------|-------------|------------|
| `Chưa tìm thấy mô hình .joblib` | Chưa train | Chạy notebook Phần 4 |
| Lỗi `Số dòng không khớp` khi eval | CSV thay đổi sau khi embed | Đặt `REGENERATE_EMBEDDINGS = True` |
| Frontend báo không kết nối API | Backend chưa chạy | Chạy `./run.sh api` hoặc `./run.sh` (cả hai) |
| Embedding chạy quá lâu | CPU, dataset lớn | Dùng GPU hoặc giữ `REGENERATE_EMBEDDINGS = False` |
| Crawl URL trả về nội dung rỗng | Trang chặn bot / cấu trúc HTML khác | Dùng chế độ nhập văn bản |
| Lần đầu chạy web chậm | Tải PhoBERT từ HuggingFace | Chờ 1–3 phút, model được cache |

---

## Tóm tắt quy trình (checklist)

```
[ ] 1. Cài Python venv + pip install -r requirements.txt
[ ] 2. Cài npm install trong frontend/
[ ] 3. Kiểm tra backend/data/full_dataset.csv
[ ] 4. Chạy python -m backend.dataset_cleaner
[ ] 5. Mở train_phobert_model.ipynb — chạy Phần 1→5
[ ] 6. Kiểm tra 5 file trong backend/models/
[ ] 7. Chạy đánh giá thực nghiệm (Phần 5 / script)
[ ] 8. Chạy ./run.sh
[ ] 9. Test /analyze với mẫu tin giả và tin thật
[ ] 10. Chụp biểu đồ + ghi kết quả vào luận văn
```

---

*Tài liệu được tạo tự động từ cấu trúc dự án ShieldAI — cập nhật: tháng 6/2026.*
