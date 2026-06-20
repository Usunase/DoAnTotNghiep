#!/usr/bin/env bash
# Cài đặt một lần: venv, Python deps, Node deps, kiểm tra model.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "══════════════════════════════════════════"
echo "  ShieldAI — Cài đặt môi trường"
echo "  Thư mục: $ROOT_DIR"
echo "══════════════════════════════════════════"

# --- Python ---
if ! command -v python3 &>/dev/null; then
  echo "❌ Cần Python 3.10+. Cài python3 rồi chạy lại."
  exit 1
fi

PY_VER="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
echo "▶ Python $PY_VER"

if [ ! -d "venv" ]; then
  echo "▶ Tạo virtualenv..."
  python3 -m venv venv
fi

# shellcheck disable=SC1091
source venv/bin/activate

echo "▶ pip install -r requirements.txt ..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
pip install -q pytest

# --- Node ---
if ! command -v node &>/dev/null; then
  echo "❌ Cần Node.js >= 18. Cài node rồi chạy lại."
  exit 1
fi
echo "▶ Node $(node -v)"

if [ ! -d "frontend/node_modules" ]; then
  echo "▶ npm install (frontend)..."
  (cd frontend && npm install)
else
  echo "▶ frontend/node_modules đã có — bỏ qua npm install"
fi

# --- Env frontend ---
if [ ! -f "frontend/.env.local" ] && [ -f "frontend/.env.local.example" ]; then
  cp frontend/.env.local.example frontend/.env.local
  echo "▶ Đã tạo frontend/.env.local từ .env.local.example"
fi

# --- Model artifacts ---
MODEL_DIR="$ROOT_DIR/backend/models"
MISSING=0
for f in phobert_mlp_model.joblib phobert_scaler.joblib phobert_base_features.npy phobert_base_labels.npy; do
  if [ ! -f "$MODEL_DIR/$f" ]; then
    echo "⚠️  Thiếu: backend/models/$f"
    MISSING=1
  fi
done

if [ "$MISSING" -eq 1 ]; then
  echo ""
  echo "⚠️  Chưa đủ file model. Chạy notebook train:"
  echo "    backend/training/train_phobert_model.ipynb (Phần 1 → 5)"
  echo "    hoặc clone repo đã có model trong backend/models/"
else
  echo "▶ Model inference: OK"
fi

# --- Quick sanity ---
echo "▶ Kiểm tra import backend..."
python -c "from backend.phobert_inference import PhoBERTInferenceSystem; print('   PhoBERTInferenceSystem OK')"

echo ""
echo "✅ Cài đặt xong. Chạy hệ thống:"
echo "   ./run.sh          # Backend + Frontend"
echo "   ./run.sh api      # Chỉ API"
echo "   ./run.sh test     # Chạy pytest"
