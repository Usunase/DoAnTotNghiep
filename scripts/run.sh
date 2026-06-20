#!/usr/bin/env bash
# Chạy ShieldAI: setup nếu cần, rồi khởi động API / Web / Test.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

MODE="${1:-all}"

usage() {
  cat <<'EOF'
ShieldAI — script chạy dự án

Cách dùng:
  ./run.sh [all|api|web|test|setup]

  all   — Backend (port 8000) + Frontend (port 3000)  [mặc định]
  api   — Chỉ FastAPI + mô hình PhoBERT
  web   — Chỉ Next.js (cần API đang chạy ở terminal khác)
  test  — Chạy pytest
  setup — Cài đặt môi trường (gọi scripts/setup.sh)

URL sau khi chạy:
  Web:     http://localhost:3000
  API:     http://127.0.0.1:8000
  API docs: http://127.0.0.1:8000/docs
EOF
}

require_venv() {
  if [ ! -d "venv" ]; then
    echo "Chưa có venv. Chạy: ./run.sh setup"
    exit 1
  fi
  # shellcheck disable=SC1091
  source venv/bin/activate
}

run_api() {
  require_venv
  echo "▶ Backend API: http://127.0.0.1:8000"
  echo "▶ Swagger:     http://127.0.0.1:8000/docs"
  exec uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
}

run_web_only() {
  cd "$ROOT_DIR/frontend"
  if [ ! -d "node_modules" ]; then
    echo "▶ npm install..."
    npm install
  fi
  echo "▶ Frontend: http://localhost:3000"
  exec npm run dev
}

run_all() {
  require_venv

  cleanup() {
    if [ -n "${API_PID:-}" ] && kill -0 "$API_PID" 2>/dev/null; then
      kill "$API_PID" 2>/dev/null || true
      wait "$API_PID" 2>/dev/null || true
    fi
  }
  trap cleanup EXIT INT TERM

  echo "▶ Khởi động Backend (nền)..."
  uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000 &
  API_PID=$!

  echo "▶ Đợi API sẵn sàng..."
  for _ in $(seq 1 30); do
    if curl -sf "http://127.0.0.1:8000/api/health" >/dev/null 2>&1; then
      echo "▶ API OK"
      break
    fi
    sleep 1
  done

  echo "▶ Khởi động Frontend..."
  cd "$ROOT_DIR/frontend"
  if [ ! -d "node_modules" ]; then
    npm install
  fi
  echo ""
  echo "══════════════════════════════════════════"
  echo "  Web:  http://localhost:3000"
  echo "  API:  http://127.0.0.1:8000"
  echo "  Docs: http://127.0.0.1:8000/docs"
  echo "  Ctrl+C để dừng cả hai"
  echo "══════════════════════════════════════════"
  npm run dev
}

run_test() {
  require_venv
  cd "$ROOT_DIR/backend"
  exec ./run_tests.sh
}

case "$MODE" in
  all)    run_all ;;
  api)    run_api ;;
  web)    run_web_only ;;
  test)   run_test ;;
  setup)  exec bash "$ROOT_DIR/scripts/setup.sh" ;;
  -h|--help|help) usage ;;
  *)
    echo "Lệnh không hợp lệ: $MODE"
    usage
    exit 1
    ;;
esac
