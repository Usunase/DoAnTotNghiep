<h1 align="center">🛡️ ShieldAI — Phát hiện Tin giả Tiếng Việt</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-14-black.svg" alt="Next.js">
  <img src="https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/PhoBERT-Base-yellow.svg" alt="PhoBERT">
</p>

<p align="center">
  <b>Đồ án Tốt nghiệp — Hệ thống phát hiện tin giả tiếng Việt dựa trên PhoBERT và MLP, kèm giải thích rule-based (XAI).</b>
</p>

---

## Giới thiệu

**ShieldAI** là ứng dụng web phân tích và phát hiện tin giả tiếng Việt trong lĩnh vực y tế / sức khỏe. Hệ thống dùng **PhoBERT-base** (embedding 768 chiều, cố định) kết hợp **MLP (128, 64)** để ước lượng xác suất tin giả, sau đó phân loại **3 mức**: tin thật / đáng ngờ / tin giả.

**Kết quả thực nghiệm** (tập 10.609 mẫu, hold-out 30%):

| Chỉ số | Giá trị |
|--------|---------|
| Accuracy | 94,13% |
| F1-Score | **93,71%** |
| ROC-AUC | 98,50% |
| CV F1 (5-fold) | 93,17% ± 1,33% |

Stack triển khai: **FastAPI** (backend + AI) và **Next.js** (giao diện), SQLite lưu lịch sử phân tích.

---

## Tính năng

- **Nhập liệu linh hoạt:** dán văn bản hoặc URL bài báo (crawl tự động bằng BeautifulSoup).
- **Verdict 3 mức:** ngưỡng thống nhất backend ↔ frontend (≥75% tin giả, 35–74% đáng ngờ, &lt;35% tin thật).
- **Giải thích (XAI):** rule-based — phân tích dấu hiệu văn bản + tóm tắt từ mô hình.
- **Tài khoản & lịch sử:** đăng ký / đăng nhập JWT, xem lại kết quả phân tích.
- **Tiền xử lý thống nhất:** `preprocess_text` dùng chung cho train và inference (lowercase → xóa URL → PyVi).

---

## Kiến trúc tóm tắt

```
Người dùng (Next.js)
    → API proxy (/api/*)
    → FastAPI
        → preprocess_text
        → PhoBERT [CLS] 768-d
        → StandardScaler + MLP
        → verdict + explanation
    → SQLite (users, history)
```

Sơ đồ chi tiết: thư mục `image/` (`mermaid_1.mmd`, `mermaid_3.mmd`).

---

## Cấu trúc dự án

```text
DoAnTotNghiep/
├── setup.sh / run.sh       # Cài đặt & chạy nhanh (wrapper)
├── scripts/
│   ├── setup.sh            # Tạo venv, pip, npm, kiểm tra model
│   └── run.sh              # all | api | web | test
├── backend/
│   ├── api/                # FastAPI routes
│   ├── auth/               # JWT
│   ├── database/           # SQLite + models ORM
│   ├── data/               # full_dataset.csv
│   ├── models/             # .joblib, .npy (artifact inference)
│   ├── experiments/        # Đánh giá thực nghiệm + biểu đồ
│   ├── training/           # train_phobert_model.ipynb
│   ├── phobert_inference.py
│   ├── verdict.py
│   ├── explanation_engine.py
│   ├── text_utils.py
│   ├── dataset_cleaner.py
│   └── tests/
├── frontend/               # Next.js 14 + TailwindCSS
├── docs/
│   ├── TIEU_LUAN_SHIELDAI.md      # Luận văn chính thức (v5.0)
│   ├── HUONG_DAN_THUC_HIEN_DU_AN.md
│   ├── LY_DO_CHON_PHUONG_AN.md
│   └── CHUAN_BI_BAO_VE_THEO_PHIEU_CHAM.md
└── image/                  # Sơ đồ Mermaid
```

---

## Bộ dữ liệu

| Mục | Giá trị |
|-----|---------|
| File | `backend/data/full_dataset.csv` |
| Số bản ghi | **10.617** bài |
| Sau lọc (train) | **10.609** mẫu |
| Nhãn | `is_fake`: True = giả, False = thật |
| Cân bằng lớp | ~53,6% thật / ~46,4% giả |
| Lĩnh vực | Y tế, sức khỏe, COVID (tiếng Việt) |
| Nguồn chính | VnExpress, daikynguyen, covid19_dataset, … |

Quy trình lọc (`dataset_cleaner.py`): bỏ thiếu `content` → bỏ &lt; 5 từ → bỏ trùng → `preprocess_text`.

---

## Mô hình inference (`backend/models/`)

Các file sau **đã được commit** — clone repo có thể chạy inference ngay:

| File | Vai trò |
|------|---------|
| `phobert_mlp_model.joblib` | MLP đã huấn luyện |
| `phobert_scaler.joblib` | StandardScaler |
| `phobert_base_features.npy` | Cache embedding (~32 MB) |
| `phobert_base_labels.npy` | Nhãn tương ứng |

Train lại: mở `backend/training/train_phobert_model.ipynb` (Phần 1 → 5).

---

## Yêu cầu hệ thống

| Thành phần | Phiên bản |
|------------|-----------|
| Python | ≥ 3.10 |
| Node.js | ≥ 18 |
| RAM | ≥ 8 GB (khuyến nghị 16 GB cho PhoBERT) |
| GPU | Tùy chọn (chỉ tăng tốc embedding khi train) |

---

## Cài đặt & chạy

### 1. Clone và cài đặt (lần đầu)

```bash
git clone https://github.com/Usunase/DoAnTotNghiep.git
cd DoAnTotNghiep
chmod +x setup.sh run.sh scripts/*.sh
./setup.sh
```

`setup.sh` thực hiện: tạo `venv`, `pip install -r requirements.txt`, `npm install`, tạo `frontend/.env.local`, kiểm tra artifact model.

### 2. Chạy hệ thống

```bash
./run.sh
```

| Lệnh | Mô tả |
|------|--------|
| `./run.sh` | Backend `:8000` + Frontend `:3000` |
| `./run.sh api` | Chỉ FastAPI |
| `./run.sh web` | Chỉ Next.js (API chạy terminal khác) |
| `./run.sh test` | Chạy pytest |
| `./run.sh setup` | Cài đặt lại môi trường |

**URL:**

| Dịch vụ | Địa chỉ |
|---------|---------|
| Giao diện web | http://localhost:3000 |
| API | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |

> Lần đầu khởi động API có thể mất 1–2 phút để tải PhoBERT vào RAM.

### 3. Chạy thủ công (tùy chọn)

```bash
source venv/bin/activate

# Terminal 1
uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2
cd frontend && npm run dev
```

### 4. Kiểm tra inference (CLI)

```bash
source venv/bin/activate
python -m backend.phobert_inference
```

### 5. Làm sạch dữ liệu

```bash
source venv/bin/activate
python -m backend.dataset_cleaner
```

---

### API

Các endpoint FastAPI trả JSON envelope `status` + `message`; lỗi nghiệp vụ (auth, input trống) thường dùng HTTP **200** + `status: "error"` — frontend kiểm tra trường `status`, không mã 401/403.

## Kiểm thử

```bash
./run.sh test
# hoặc
cd backend && ./run_tests.sh
```

Bộ test (`pytest`) gồm: tiền xử lý văn bản, verdict 3 mức, explanation, API cơ bản.

---

## Tài liệu

| File | Nội dung |
|------|----------|
| [`Mau_Luan_Van_Tot_Nghiep.md`](Mau_Luan_Van_Tot_Nghiep.md) | Bản luận văn HTML (~1.580 dòng, export Word) — đồng bộ với kiến trúc PhoBERT Text-only + MLP |
| [`docs/TIEU_LUAN_SHIELDAI.md`](docs/TIEU_LUAN_SHIELDAI.md) | Luận văn markdown — dùng để nộp / bảo vệ |
| [`docs/HUONG_DAN_THUC_HIEN_DU_AN.md`](docs/HUONG_DAN_THUC_HIEN_DU_AN.md) | Hướng dẫn từng bước thực hiện |
| [`docs/LY_DO_CHON_PHUONG_AN.md`](docs/LY_DO_CHON_PHUONG_AN.md) | Lý do chọn PhoBERT text-only |
| [`docs/CHUAN_BI_BAO_VE_THEO_PHIEU_CHAM.md`](docs/CHUAN_BI_BAO_VE_THEO_PHIEU_CHAM.md) | Gợi ý trả lời hội đồng |
| [`backend/training/README.md`](backend/training/README.md) | Notebook huấn luyện |

Hai bản luận văn (`Mau_Luan_Van_Tot_Nghiep.md` và `docs/TIEU_LUAN_SHIELDAI.md`) mô tả cùng kiến trúc hiện tại; ưu tiên `TIEU_LUAN_SHIELDAI.md` khi chỉnh sửa nội dung học thuật.

---

## Công nghệ sử dụng

| Lớp | Công nghệ |
|-----|-----------|
| NLP / ML | PyTorch, Transformers (PhoBERT), scikit-learn, PyVi |
| Backend | FastAPI, Uvicorn, SQLAlchemy, JWT |
| Frontend | Next.js 14, React, TailwindCSS, Framer Motion |
| Dữ liệu | pandas, BeautifulSoup, joblib |

---

## Tác giả

**Hà Minh Chiến** — Đồ án Tốt nghiệp, Trường Đại học Tân Tạo, 2026.

Mã nguồn phục vụ mục đích nghiên cứu học thuật và báo cáo đồ án tốt nghiệp.
