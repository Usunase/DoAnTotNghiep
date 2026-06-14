from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.auth.deps import get_current_user
from backend.database import (
    User,
    delete_user_history,
    get_db,
    get_user_history,
    list_user_history,
)

router = APIRouter(prefix="/api/history", tags=["history"])


@router.get("")
def list_history(
    db: Session = Depends(get_db),
    user: User | None = Depends(get_current_user),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    if user is None:
        return {"status": "error", "message": "Vui lòng đăng nhập."}
    items, total = list_user_history(db, user.id, limit=limit, offset=offset)
    return {"status": "success", "items": items, "total": total}


@router.get("/{history_id}")
def get_history(
    history_id: int,
    db: Session = Depends(get_db),
    user: User | None = Depends(get_current_user),
):
    if user is None:
        return {"status": "error", "message": "Vui lòng đăng nhập."}
    detail = get_user_history(db, user.id, history_id)
    if detail is None:
        return {"status": "error", "message": "Không tìm thấy bản ghi lịch sử."}
    return detail


@router.delete("/{history_id}")
def remove_history(
    history_id: int,
    db: Session = Depends(get_db),
    user: User | None = Depends(get_current_user),
):
    if user is None:
        return {"status": "error", "message": "Vui lòng đăng nhập."}
    if not delete_user_history(db, user.id, history_id):
        return {"status": "error", "message": "Không tìm thấy bản ghi lịch sử."}
    return {"status": "success", "message": "Đã xóa bản ghi."}
