import pytest
from fastapi.testclient import TestClient
from backend.api.main import app

client = TestClient(app)

def test_health_check():
    """Kiểm tra xem server FastAPI có sống (Health Check) hay không."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "model_loaded" in data

def test_analyze_unauthorized():
    """Kiểm tra bảo mật API: Đảm bảo không cho phép phân tích nếu chưa đăng nhập."""
    payload = {
        "mode": "text",
        "text": "Bệnh ung thư có thể chữa khỏi bằng lá lốt!!!",
        "title": "Tin giật gân",
        "meta": {
            "account_age_days": 10,
            "followers": 5,
            "is_verified": 0,
            "share_speed": 100,
            "angry_ratio": 0.8
        }
    }
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "Vui lòng đăng nhập" in data["message"]

def test_analyze_missing_text():
    """Kiểm tra bắt lỗi: Báo lỗi nếu text rỗng."""
    payload = {
        "mode": "text",
        "text": "",
    }
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "Vui lòng đăng nhập" in data["message"] # Authentication runs first
