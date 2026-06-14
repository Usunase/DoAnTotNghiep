from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.auth.deps import get_current_user
from backend.database import get_db, User
from backend.database.feedback_service import submit_feedback

router = APIRouter(prefix="/api/history", tags=["feedback"])

class FeedbackPayload(BaseModel):
    is_correct: bool
    comment: str | None = None

@router.post("/{history_id}/feedback")
def create_or_update_feedback(
    history_id: int,
    payload: FeedbackPayload,
    db: Session = Depends(get_db),
    user: User | None = Depends(get_current_user),
):
    if user is None:
        return {"status": "error", "message": "Vui lòng đăng nhập."}

    # You might want to check if the history_id belongs to the user first.
    # Assuming get_user_history does this or submit_feedback will fail if FK constraint.
    # For now, submit_feedback will just link to the user.

    result = submit_feedback(
        db,
        user_id=user.id,
        history_id=history_id,
        is_correct=payload.is_correct,
        comment=payload.comment,
    )
    return result
