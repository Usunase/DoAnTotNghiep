#!/bin/bash
# Khởi động ShieldAI: FastAPI backend + Next.js frontend
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

source venv/bin/activate

cleanup() {
  if [ -n "$API_PID" ] && kill -0 "$API_PID" 2>/dev/null; then
    kill "$API_PID" 2>/dev/null
    wait "$API_PID" 2>/dev/null
  fi
}
trap cleanup EXIT INT TERM

echo "▶ Backend API: http://127.0.0.1:8000"
uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000 &
API_PID=$!

sleep 2

echo "▶ Frontend Next.js: http://localhost:3000"
cd "$ROOT_DIR/frontend"
if [ ! -d "node_modules" ]; then
  echo "Cài npm dependencies lần đầu..."
  npm install
fi
npm run dev
