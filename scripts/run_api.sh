#!/bin/bash
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"
source venv/bin/activate
echo "ShieldAI API: http://127.0.0.1:8000"
echo "Docs: http://127.0.0.1:8000/docs"
uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
