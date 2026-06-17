<h1 align="center">🛡️ ShieldAI - Hệ thống Nhận diện Tin giả Tiếng Việt</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-14-black.svg" alt="Next.js">
  <img src="https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/PhoBERT-Base-yellow.svg" alt="PhoBERT">
</p>

<p align="center">
  <b>Đồ án Tốt nghiệp: Nghiên cứu và xây dựng hệ thống phát hiện tin giả tiếng Việt dựa trên PhoBERT và mạng nơ-ron MLP.</b>
</p>

---

## 📖 Giới thiệu
**ShieldAI** là một hệ thống Trí tuệ Nhân tạo chuyên biệt dùng để rà soát, phân tích và phát hiện các bài báo, bài viết giả mạo trên không gian mạng Việt Nam. 

Thay vì các mô hình học máy truyền thống, ShieldAI sử dụng **PhoBERT** (embedding 768 chiều) kết hợp **MLP** để phân loại tin thật / tin giả. Hệ thống đạt F1-Score khoảng **94%** trên tập đánh giá hold-out, kèm lớp giải thích rule-based (XAI) dựa trên phân tích văn bản.

## ✨ Tính năng nổi bật
- **Phân tích Đa phương thức:** Hỗ trợ nhập trực tiếp Văn bản (Text) hoặc dán Đường dẫn bài báo (URL) từ các trang tin tức chính thống.
- **XAI (Explainable AI):** Không chỉ đưa ra kết luận 3 mức (Tin thật / Đáng ngờ / Tin giả), hệ thống còn giải thích các dấu hiệu rủi ro trong văn bản.
- **Giao diện hiện đại (Web App):** Xây dựng bằng Next.js mang lại trải nghiệm người dùng mượt mà, phản hồi tức thời.
- **Tiền xử lý thống nhất:** Cùng pipeline `preprocess_text` cho train và inference (lowercase, xóa URL, PyVi tokenize).

## 📂 Cấu trúc Dự án
Dự án được tổ chức theo mô hình Client-Server chuyên nghiệp:

```text
DoAnTotNghiep/
├── backend/            # Chứa mã nguồn AI và API Server
│   ├── api/            # Các Endpoint của FastAPI
│   ├── tests/          # Bộ kiểm thử tự động (Unit Test & Integration Test)
│   ├── text_utils.py   # Tiền xử lý văn bản (train + inference)
│   ├── phobert_inference.py  # Pipeline suy luận PhoBERT + MLP
│   └── run_tests.sh    # Script chạy Test tự động
├── frontend/           # Giao diện người dùng (Next.js, React, TailwindCSS)
├── docs/               # Tài liệu tham khảo và Log quá trình
├── image/              # Các hình ảnh minh chứng kiểm thử
└── Mau_Luan_Van...md   # Bản thảo Luận văn Tốt nghiệp
```

## ⚙️ Yêu cầu Hệ thống
- Hệ điều hành: Linux/Windows/macOS
- Python: >= 3.10
- Node.js: >= 18.0

## 📦 Mô hình inference (`backend/models/`)

Sau khi clone, thư mục này **phải có** các file sau để API chạy được (đã được commit trong repo):

| File | Vai trò |
|------|---------|
| `phobert_mlp_model.joblib` | MLP đã huấn luyện (768-d → 2 lớp) |
| `phobert_scaler.joblib` | StandardScaler fit trên embedding train |
| `phobert_base_features.npy` | Embedding PhoBERT cache (train) — ~32MB |
| `phobert_base_labels.npy` | Nhãn tương ứng embedding cache |

**Không còn** file `hybrid_*.joblib` (pipeline cũ PhoBERT + metadata đã bỏ).

Nếu thiếu file hoặc muốn train lại từ đầu:

1. Chuẩn bị dữ liệu CSV (xem `docs/HUONG_DAN_THUC_HIEN_DU_AN.md`).
2. Mở và chạy tuần tự `backend/training/train_phobert_model.ipynb` (Phần 1 → 5).
3. Notebook ghi đè các file `.joblib` và `.npy` vào `backend/models/`.

Kiểm tra nhanh sau khi có model:

```bash
source venv/bin/activate
python -m backend.phobert_inference
```

## 🚀 Hướng dẫn Cài đặt & Khởi chạy

### Bước 1: Khởi động Backend (FastAPI & AI Model)
Mở Terminal, di chuyển vào thư mục gốc của dự án và chạy script:
```bash
# Script tự động kích hoạt môi trường ảo và chạy uvicorn
./run_api.sh
```
*Lưu ý: API sẽ chạy ở địa chỉ `http://localhost:8000`. Lần đầu tiên chạy có thể mất chút thời gian để load mô hình PhoBERT vào RAM.*

### Bước 2: Khởi động Frontend (Next.js Web App)
Mở một tab Terminal thứ 2 và chạy script:
```bash
# Script tự động vào thư mục frontend và chạy npm run dev
./run_web.sh
```
Truy cập giao diện hệ thống tại: `http://localhost:3000`

## 🧪 Hệ thống Kiểm thử Tự động (Automated Testing)
Dự án được trang bị bộ Test Suite sử dụng `pytest`. Hệ thống kiểm thử:
1. Tiền xử lý văn bản thống nhất (`preprocess_text`).
2. Phân loại 3 mức (`verdict`).
3. Đảm bảo bảo mật truy cập API.

**Cách chạy Test:**
```bash
cd backend
./run_tests.sh
```
Nếu màn hình Terminal trả về dòng chữ xanh lá `✅ TOÀN BỘ TEST CASES ĐỀU ĐÃ VƯỢT QUA (PASSED)!`, hệ thống của bạn đang hoạt động cực kỳ ổn định!

---
**Tác giả:** Hà Minh Chiến  
**Bản quyền:** Mã nguồn phục vụ mục đích nghiên cứu học thuật và báo cáo Đồ án Tốt nghiệp.
