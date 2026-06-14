from __future__ import annotations

from fastapi import Depends, Header
from sqlalchemy.orm import Session

from backend.database import User, get_db
from backend.auth.security import decode_access_token


def get_token_from_header(authorization: str | None) -> str | None:
    if not authorization:
        return None
    parts = authorization.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]
    return None


def get_current_user(
    db: Session = Depends(get_db),
    authorization: str | None = Header(default=None),
) -> User | None:
    token = get_token_from_header(authorization)
    if not token:
        return None
    user_id = decode_access_token(token)
    if user_id is None:
        return None
    return db.query(User).filter(User.id == user_id).first()

