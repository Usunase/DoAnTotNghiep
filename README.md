<h1 align="center">🛡️ ShieldAI — Phát hiện Tin giả Tiếng Việt</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-14-black.svg" alt="Next.js">
  <img src="https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/PhoBERT-Base-yellow.svg" alt="PhoBERT">
</p>

<p align="center">
  <b>Tiểu luận Tốt nghiệp — Hệ thống phát hiện tin giả tiếng Việt dựa trên mô hình PhoBERT Fine-tuned Sequence Classification, tích hợp Động cơ giải thích (Rule-based Heuristic Explanation).</b>
</p>

---

## Giới thiệu

**ShieldAI** là ứng dụng web phân tích và phát hiện tin giả tiếng Việt toàn diện. Hệ thống ứng dụng kiến trúc **Phân tách Ngữ nghĩa - Kinh nghiệm (Decoupled Semantic-Heuristic Architecture)**. Phân loại lõi sử dụng mô hình học sâu **PhoBERT Fine-tuned**, kết hợp với luồng phân tích luật độc lập (Rule-based) để giải thích tính hợp lý của kết quả theo thời gian thực mà không làm tăng độ trễ suy luận.

**Kết quả thực nghiệm** (Siêu tập 22.633 mẫu, hold-out 12%):

| Chỉ số | Giá trị |
|--------|---------|
| Accuracy | **96,32%** |
| F1-Score | **93,42%** |
| Precision| 92,45% |
| Recall   | 94,41% |

Hệ thống được phát triển theo mô hình 3 tầng: **FastAPI** (Backend/AI), **Next.js** (Frontend) và **SQLite** (Cơ sở dữ liệu).

---

## Tính năng nổi bật

- **Nhập liệu đa dạng:** Phân tích trực tiếp từ đoạn văn bản hoặc trích xuất tự động nội dung từ URL tin tức (bằng BeautifulSoup).
- **Phân loại 3 mức độ:** Hệ thống diễn giải xác suất rủi ro thành 3 mức trực quan (Tin giả, Đáng ngờ, Tin thật).
- **Minh bạch hóa (XAI):** Động cơ giải thích độc lập, tự động quét dấu hiệu thao túng tâm lý (Teencode, viết hoa in đậm, dấu câu kích động, phân tích cảm xúc).
- **Quản lý lịch sử:** Hệ thống tài khoản người dùng JWT an toàn, lưu trữ toàn bộ lịch sử phân tích và phản hồi.

---

## Kiến trúc Hệ thống

```text
Client (Next.js 14)
    ├── Giao diện Phân tích / Lịch sử / Xác thực
    └── Gọi API thông qua các Route Handler nội bộ
          ↓ (HTTP/JSON)
Backend API (FastAPI)
    ├── Tiền xử lý (TextCleaner)
    ├── PhoBERT Inference Engine (Sequence Classification)
    ├── Động cơ Giải thích Heuristics
    └── Trả về Kết quả (Verdict + Explanation)
          ↓ (SQLAlchemy)
Cơ sở dữ liệu (SQLite)
    └── Lưu trữ thông tin Users, AnalysisHistory, Feedbacks
```

*(Các sơ đồ chi tiết định dạng hình ảnh và Draw.io có sẵn trong thư mục `image/` và `export/`)*

---

## Cấu trúc Dự án

```text
DoAnTotNghiep/
├── setup.sh / run.sh       # Script tự động hóa cài đặt & khởi chạy
├── scripts/                # Các script hệ thống phụ trợ
├── backend/
│   ├── api/                # FastAPI Routers (auth, history, feedback)
│   ├── auth/               # Hệ thống bảo mật JWT
│   ├── database/           # SQLite + SQLAlchemy Models
│   ├── data/               # vietnamese_fake_news_dataset.csv
│   ├── models/             # Chứa mô hình PhoBERT-fakenews-final sau khi train
│   ├── experiments/        # Thư mục chứa biểu đồ/số liệu thực nghiệm
│   ├── training/           # Notebook & Script huấn luyện mô hình
│   ├── phobert_inference.py
│   ├── explanation_engine.py
│   ├── text_cleaner.py
│   └── tests/              # Mã kiểm thử tự động (Pytest)
├── frontend/               # Next.js 14 Web App + TailwindCSS
├── image/ / export/        # Sơ đồ và hình ảnh minh họa
└── mau_luan_van_...tex     # Mã nguồn tài liệu báo cáo Tiểu luận (LaTeX)
```

---

## Bộ dữ liệu (Vietnamese Fake News Dataset)

Siêu tập dữ liệu được gộp từ 4 bộ ngữ liệu uy tín trên nền tảng Kaggle, tập trung vào tin tức tổng hợp, tin tức mạng xã hội và y tế.

| Thuộc tính | Giá trị |
|-----|---------|
| File | `backend/data/vietnamese_fake_news_dataset.csv` |
| Tổng số mẫu | **22.633** bài báo/bài đăng |
| Tỷ lệ phân lớp | Rất cân bằng (Xấp xỉ 53,6% Tin thật / 46,4% Tin giả) |
| Tỷ lệ phân chia | Train (76%) - Val (12%) - Test (12%) |

---

## Cài đặt & Vận hành Hệ thống

### 1. Cài đặt môi trường (Lần đầu tiên)

Yêu cầu hệ thống:
- Python ≥ 3.10
- Node.js ≥ 18
- RAM tối thiểu 16GB để tải mô hình PhoBERT vào bộ nhớ chính.

```bash
git clone https://github.com/Usunase/DoAnTotNghiep.git
cd DoAnTotNghiep
chmod +x setup.sh run.sh scripts/*.sh
./setup.sh
```

### 2. Khởi chạy Ứng dụng

Bạn có thể chạy toàn bộ hệ thống bằng một dòng lệnh duy nhất:

```bash
./run.sh
```

Các tùy chọn lệnh khác:
- `./run.sh api`: Chỉ khởi chạy Backend (Cổng 8000)
- `./run.sh web`: Chỉ khởi chạy Frontend (Cổng 3000)
- `./run.sh test`: Chạy bộ Test tự động (Pytest)

### 3. Thông tin Truy cập

| Dịch vụ | Địa chỉ Local |
|---------|---------|
| Web App (Next.js) | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger UI (API Docs)| http://localhost:8000/docs |

---

## Huấn luyện Mô hình (Training)

Mô hình đã được Fine-tune được lưu tại `backend/models/phobert-fakenews-final`. Nếu muốn chạy lại quá trình huấn luyện:

1. Đọc hướng dẫn chi tiết tại: `backend/training/TRAINING_GUIDE.md`
2. Mở sổ tay Jupyter: `backend/training/train_phobert_model.ipynb`

---

## Bản quyền & Tác giả

**Hà Minh Chiến** — Tiểu luận Tốt nghiệp, Trường Đại học Tân Tạo, 2026.
Mã nguồn được phát triển phục vụ mục đích nghiên cứu học thuật.
