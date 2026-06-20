"""Fixtures dùng chung cho bộ kiểm thử ShieldAI."""
from __future__ import annotations

import uuid
from typing import Any
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.api.main import app
from backend.database import models  # noqa: F401 — đăng ký ORM
from backend.database.connection import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

_test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_test_engine)


def _sample_infer_result(fake_prob: float = 55.0) -> dict[str, Any]:
    verdict = "suspicious"
    if fake_prob >= 75:
        verdict = "fake"
    elif fake_prob < 35:
        verdict = "real"
    labels = {
        "fake": "TIN GIẢ (FAKE)",
        "suspicious": "ĐÁNG NGỜ",
        "real": "TIN THẬT (REAL)",
    }
    return {
        "status": "success",
        "result": labels[verdict],
        "verdict": verdict,
        "fake_prob": fake_prob,
        "raw_data": {
            "title": "Tiêu đề kiểm thử",
            "content": "Nội dung bài viết đủ dài để phân tích hệ thống ShieldAI một cách hợp lệ.",
            "source_domain": "user_input",
        },
        "cleaned_text": "nội_dung bài_viết",
        "phobert_shape": (768,),
        "explanation": {
            "verdict": verdict,
            "headline": "Kiểm thử",
            "summary": "Tóm tắt kiểm thử",
            "primary_reasons": ["Lý do mẫu"],
            "counter_points": [],
            "model_confidence": fake_prob,
        },
    }


@pytest.fixture()
def db_session():
    Base.metadata.create_all(bind=_test_engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=_test_engine)


@pytest.fixture()
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture()
def auth_headers(client):
    suffix = uuid.uuid4().hex[:8]
    response = client.post(
        "/api/auth/register",
        json={
            "email": f"test_{suffix}@example.com",
            "username": f"user_{suffix}",
            "password": "TestPass123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    return {"Authorization": f"Bearer {data['token']}"}


@pytest.fixture()
def mock_inference_system(monkeypatch):
    mock_system = MagicMock()
    mock_system.model_loaded = True
    mock_system.infer.side_effect = lambda **kwargs: _sample_infer_result()
    monkeypatch.setattr("backend.api.main.get_system", lambda: mock_system)
    return mock_system
