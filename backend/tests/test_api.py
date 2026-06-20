"""Kiểm thử API phân tích và lịch sử."""
import uuid


def test_health_check(client, mock_inference_system):
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["model_loaded"] is True


def test_analyze_unauthorized(client, mock_inference_system):
    payload = {
        "mode": "text",
        "text": "Bệnh ung thư có thể chữa khỏi bằng lá lốt!!!",
        "title": "Tin giật gân",
    }
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "đăng nhập" in data["message"].lower()


def test_analyze_empty_text_when_authenticated(client, auth_headers, mock_inference_system):
    response = client.post(
        "/api/analyze",
        json={"mode": "text", "text": "", "title": ""},
        headers=auth_headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "trống" in data["message"].lower()


def test_analyze_text_success(client, auth_headers, mock_inference_system):
    response = client.post(
        "/api/analyze",
        json={
            "mode": "text",
            "title": "Kiểm thử",
            "text": (
                "CẢNH BÁO!!! Tin đồn lan truyền trên mạng xã hội cần được kiểm chứng "
                "kỹ lưỡng trước khi chia sẻ cho người thân."
            ),
        },
        headers=auth_headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "verdict" in data
    assert "fake_prob" in data
    assert "explanation" in data
    assert "history_id" in data
    mock_inference_system.infer.assert_called_once()


def test_analyze_url_mode(client, auth_headers, mock_inference_system):
    response = client.post(
        "/api/analyze",
        json={"mode": "url", "url": "https://vnexpress.net/bai-test"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    mock_inference_system.infer.assert_called_with(url="https://vnexpress.net/bai-test")


def test_history_list_after_analyze(client, auth_headers, mock_inference_system):
    client.post(
        "/api/analyze",
        json={
            "mode": "text",
            "text": "Nội dung bài viết đủ dài để lưu vào lịch sử phân tích của người dùng.",
        },
        headers=auth_headers,
    )

    history = client.get("/api/history", headers=auth_headers)
    assert history.status_code == 200
    body = history.json()
    assert body["status"] == "success"
    assert body["total"] >= 1
    assert len(body["items"]) >= 1


def test_history_detail_and_delete(client, auth_headers, mock_inference_system):
    analyze = client.post(
        "/api/analyze",
        json={
            "mode": "text",
            "text": "Bài viết kiểm thử chi tiết lịch sử với nội dung đủ dài cho hệ thống.",
        },
        headers=auth_headers,
    )
    history_id = analyze.json()["history_id"]

    detail = client.get(f"/api/history/{history_id}", headers=auth_headers)
    assert detail.status_code == 200
    assert detail.json()["status"] == "success"
    assert detail.json()["history_id"] == history_id

    deleted = client.delete(f"/api/history/{history_id}", headers=auth_headers)
    assert deleted.status_code == 200
    assert deleted.json()["status"] == "success"

    missing = client.get(f"/api/history/{history_id}", headers=auth_headers)
    assert missing.json()["status"] == "error"


def test_history_isolated_between_users(client, mock_inference_system):
    suffix = uuid.uuid4().hex[:8]

    user_a = client.post(
        "/api/auth/register",
        json={
            "email": f"a_{suffix}@example.com",
            "username": f"user_a_{suffix}",
            "password": "Pass1234",
        },
    ).json()["token"]
    user_b = client.post(
        "/api/auth/register",
        json={
            "email": f"b_{suffix}@example.com",
            "username": f"user_b_{suffix}",
            "password": "Pass1234",
        },
    ).json()["token"]

    created = client.post(
        "/api/analyze",
        json={"mode": "text", "text": "Nội dung riêng của user A đủ dài để phân tích."},
        headers={"Authorization": f"Bearer {user_a}"},
    )
    history_id = created.json()["history_id"]

    forbidden = client.get(
        f"/api/history/{history_id}",
        headers={"Authorization": f"Bearer {user_b}"},
    )
    assert forbidden.json()["status"] == "error"
