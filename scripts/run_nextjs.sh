#!/bin/bash
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR/frontend"
if [ ! -d "node_modules" ]; then
  echo "Cài dependencies lần đầu..."
  npm install
fi
echo "ShieldAI Web: http://localhost:3000"
npm run dev
