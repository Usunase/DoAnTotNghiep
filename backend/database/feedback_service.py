from __future__ import annotations

from typing import Any

from sqlalchemy.orm import Session

from backend.database.models import Feedback


def submit_feedback(
    db: Session,
    user_id: int,
    history_id: int,
    is_correct: bool,
    comment: str | None = None,
) -> dict[str, Any]:
    # Check if feedback already exists for this history_id
    existing_feedback = (
        db.query(Feedback)
        .filter(Feedback.history_id == history_id, Feedback.user_id == user_id)
        .first()
    )

    if existing_feedback:
        existing_feedback.is_correct = is_correct
        existing_feedback.comment = comment
        action = "updated"
    else:
        new_feedback = Feedback(
            history_id=history_id,
            user_id=user_id,
            is_correct=is_correct,
            comment=comment,
        )
        db.add(new_feedback)
        action = "created"

    db.commit()
    return {"status": "success", "action": action}
