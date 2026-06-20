"""Kiểm thử lớp lưu trữ lịch sử phân tích."""
from backend.database.history_service import list_user_history, save_analysis
from backend.database.models import User


def test_save_and_list_analysis(db_session):
    user = User(
        email="history@example.com",
        username="history_user",
        hashed_password="hashed",
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    result = {
        "result": "ĐÁNG NGỜ",
        "fake_prob": 42.5,
        "raw_data": {
            "title": "Tin thử",
            "content": "Nội dung đủ dài",
            "source_domain": "user_input",
        },
        "explanation": {
            "verdict": "suspicious",
            "headline": "Đáng ngờ",
            "summary": "Tóm tắt",
            "primary_reasons": ["Lý do"],
        },
    }
    history_id = save_analysis(db_session, user.id, "text", result, input_title="Tin thử")

    items, total = list_user_history(db_session, user.id)
    assert total == 1
    assert items[0]["id"] == history_id
    assert items[0]["verdict"] == "suspicious"
    assert items[0]["fake_prob"] == 42.5
