#!/bin/bash
# Script khởi động JupyterLab cho dự án Phát hiện Tin giả Tiếng Việt

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

echo "🚀 Khởi động JupyterLab..."
echo "📁 Thư mục dự án: $PROJECT_DIR"

# Kích hoạt môi trường ảo
source "$VENV_DIR/bin/activate"

echo "✅ Python: $(python --version)"
echo "✅ JupyterLab: $(jupyter lab --version)"
echo ""
echo "🌐 Đang mở JupyterLab tại: http://localhost:8888"
echo "   (Nhấn Ctrl+C để dừng)"
echo ""

# Khởi động JupyterLab
jupyter lab --notebook-dir="$PROJECT_DIR" 
