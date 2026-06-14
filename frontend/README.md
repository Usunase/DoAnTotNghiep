# ShieldAI — Next.js Frontend

Giao diện web chính của dự án (phân loại tin thật / tin giả).

## Stack

- React 18 + Next.js 14 (App Router)
- Tailwind CSS
- Framer Motion
- Backend: FastAPI (`backend/api/main.py`)

## Cấu trúc

```
frontend/
├── app/              # /, /analyze, /results
├── components/       # UI components
├── lib/              # API client, types
└── app/api/analyze/  # Proxy → Python API
```

## Chạy nhanh (1 lệnh — khuyến nghị)

```bash
cd /home/haminhchien/Documents/DoAnTotNghiep
source venv/bin/activate
./run_web.sh
```

Mở **http://localhost:3000** (API: http://127.0.0.1:8000)

## Chạy tách riêng (2 terminal)

**Terminal 1 — API:**
```bash
./run_api.sh
```

**Terminal 2 — Next.js:**
```bash
./run_nextjs.sh
```

## Trang

| Route | Mô tả |
|-------|--------|
| `/` | Welcome + banner |
| `/analyze` | Nhập văn bản / link |
| `/results` | Kết quả phân tích |
