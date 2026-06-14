<h1 align="center">🛡️ ShieldAI - Hệ thống Nhận diện Tin giả Tiếng Việt</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/Next.js-14-black.svg" alt="Next.js">
  <img src="https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/PhoBERT-Base-yellow.svg" alt="PhoBERT">
</p>

<p align="center">
  <b>Đồ án Tốt nghiệp: Nghiên cứu và Xây dựng hệ thống phát hiện tin giả dựa trên mô hình ngôn ngữ lớn và đặc trưng ngữ cảnh (Hybrid Architecture).</b>
</p>

---

## 📖 Giới thiệu
**ShieldAI** là một hệ thống Trí tuệ Nhân tạo chuyên biệt dùng để rà soát, phân tích và phát hiện các bài báo, bài viết giả mạo trên không gian mạng Việt Nam. 

Thay vì chỉ sử dụng các mô hình học máy truyền thống, ShieldAI tiên phong áp dụng **Kiến trúc Lai (Hybrid Architecture)**, kết hợp sức mạnh đọc hiểu ngữ nghĩa sâu của **PhoBERT** cùng với **10 luồng Đặc trưng Kinh nghiệm (Heuristics/Metadata)**. Giải pháp này giúp hệ thống đạt độ chính xác (F1-Score) lên tới **94.1%**, đồng thời triệt tiêu điểm mù của AI và giảm thiểu tối đa hiện tượng đánh oan tin thật (False Positives).

## ✨ Tính năng nổi bật
- **Phân tích Đa phương thức:** Hỗ trợ nhập trực tiếp Văn bản (Text) hoặc dán Đường dẫn bài báo (URL) từ các trang tin tức chính thống.
- **XAI (Explainable AI) - Trí tuệ nhân tạo có thể giải thích:** Không chỉ đưa ra kết luận (Tin thật/Tin giả), hệ thống còn vạch trần các thủ thuật lừa đảo (ví dụ: Lạm dụng viết hoa, lạm dụng dấu chấm than, giọng điệu kích động,...).
- **Giao diện hiện đại (Web App):** Xây dựng bằng Next.js mang lại trải nghiệm người dùng mượt mà, phản hồi tức thời.
- **Bộ chuẩn hóa Tiếng Việt (Text Cleaner):** Tự động làm sạch rác HTML, tự động dịch các từ lóng mạng (Teencode) như *ko, dc, wa, j* về chuẩn Tiếng Việt.

## 📂 Cấu trúc Dự án
Dự án được tổ chức theo mô hình Client-Server chuyên nghiệp:

```text
DoAnTotNghiep/
├── backend/            # Chứa mã nguồn AI và API Server
│   ├── api/            # Các Endpoint của FastAPI
│   ├── tests/          # Bộ kiểm thử tự động (Unit Test & Integration Test)
│   ├── text_cleaner.py # Module làm sạch văn bản & xử lý Teencode
│   ├── feature_...py   # Module trích xuất Heuristics (Tỷ lệ viết hoa, dấu câu)
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
Dự án được trang bị bộ Test Suite chuẩn doanh nghiệp sử dụng `pytest`. Hệ thống kiểm thử chặt chẽ 3 hạng mục:
1. Xử lý Teencode & Rác HTML.
2. Trích xuất đặc trưng hình thức (Heuristics).
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
