"""Kiểm thử API xác thực người dùng."""
import uuid


def test_register_and_login_flow(client):
    suffix = uuid.uuid4().hex[:8]
    email = f"auth_{suffix}@example.com"
    password = "SecurePass1"

    register = client.post(
        "/api/auth/register",
        json={"email": email, "username": f"authuser_{suffix}", "password": password},
    )
    assert register.status_code == 200
    reg_data = register.json()
    assert "token" in reg_data
    assert reg_data["user"]["email"] == email

    login = client.post("/api/auth/login", json={"email": email, "password": password})
    assert login.status_code == 200
    assert "token" in login.json()

    me = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {login.json()['token']}"},
    )
    assert me.status_code == 200
    assert me.json()["status"] == "success"
    assert me.json()["user"]["email"] == email


def test_register_duplicate_email(client):
    suffix = uuid.uuid4().hex[:8]
    email = f"dup_{suffix}@example.com"
    payload = {"email": email, "username": f"user1_{suffix}", "password": "Pass1234"}

    first = client.post("/api/auth/register", json=payload)
    assert first.status_code == 200

    second = client.post(
        "/api/auth/register",
        json={"email": email, "username": f"user2_{suffix}", "password": "Pass1234"},
    )
    assert second.status_code == 200
    assert second.json()["status"] == "error"
    assert "Email" in second.json()["message"]


def test_login_wrong_password(client):
    suffix = uuid.uuid4().hex[:8]
    email = f"wrong_{suffix}@example.com"
    client.post(
        "/api/auth/register",
        json={"email": email, "username": f"wrong_{suffix}", "password": "CorrectPass"},
    )

    response = client.post(
        "/api/auth/login",
        json={"email": email, "password": "WrongPass"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "error"


def test_me_requires_auth(client):
    response = client.get("/api/auth/me")
    assert response.status_code == 200
    assert response.json()["status"] == "error"
