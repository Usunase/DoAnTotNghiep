#!/bin/bash

echo "======================================"
echo "🛡️  SHIELDAI AUTOMATED TESTING SUITE 🛡️"
echo "======================================"
echo "Khởi chạy môi trường Pytest cho Backend..."
echo ""

# Đặt PYTHONPATH để Python hiểu thư mục gốc
export PYTHONPATH=$(pwd)/..

# Chạy pytest với giao diện hiển thị chi tiết (verbose)
pytest tests/ -v --disable-warnings
TEST_EXIT_CODE=$?

echo ""
echo "======================================"
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ TOÀN BỘ TEST CASES ĐỀU ĐÃ VƯỢT QUA (PASSED)!"
else
    echo "❌ CÓ LỖI XẢY RA TRONG QUÁ TRÌNH KIỂM THỬ (FAILED)!"
    exit 1
fi
echo "======================================"
