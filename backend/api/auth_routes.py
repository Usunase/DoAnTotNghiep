from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.auth.deps import get_current_user
from backend.database import User, get_db
from backend.auth.schemas import AuthSuccess, LoginRequest, RegisterRequest, UserPublic
from backend.auth.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _auth_response(user: User) -> dict:
    token = create_access_token(user.id)
    return AuthSuccess(
        token=token,
        user=UserPublic.model_validate(user),
    ).model_dump()


@router.post("/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    username = payload.username.strip()

    if db.query(User).filter(User.email == email).first():
        return {"status": "error", "message": "Email đã được sử dụng."}
    if db.query(User).filter(User.username == username).first():
        return {"status": "error", "message": "Tên đăng nhập đã tồn tại."}

    user = User(
        email=email,
        username=username,
        hashed_password=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return _auth_response(user)


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        return {"status": "error", "message": "Email hoặc mật khẩu không đúng."}
    return _auth_response(user)


@router.post("/logout")
def logout():
    return {"status": "success", "message": "Đã đăng xuất."}


@router.get("/me")
def me(user: User | None = Depends(get_current_user)):
    if user is None:
        return {"status": "error", "message": "Chưa đăng nhập."}
    return {
        "status": "success",
        "user": UserPublic.model_validate(user).model_dump(),
    }
