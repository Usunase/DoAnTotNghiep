"""
FastAPI — bridge giữa Next.js frontend và HybridInferenceSystem.
Chạy: uvicorn backend.api.main:app --reload --host 0.0.0.0 --port 8000
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal, Optional

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.api.auth_routes import router as auth_router
from backend.api.feedback_routes import router as feedback_router
from backend.api.history_routes import router as history_router
from backend.auth.deps import get_current_user
from backend.database import User, get_db, init_db, save_analysis
from backend.hybrid_inference import HybridInferenceSystem

app = FastAPI(title="ShieldAI API", version="1.2.0")

app.include_router(auth_router)
app.include_router(history_router)
app.include_router(feedback_router)


@app.on_event("startup")
def on_startup():
    init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_system: HybridInferenceSystem | None = None


def get_system() -> HybridInferenceSystem:
    global _system
    if _system is None:
        _system = HybridInferenceSystem(verbose=False)
    return _system


class MetaPayload(BaseModel):
    account_age_days: float = 0
    followers: float = 0
    is_verified: float = 0
    share_speed: float = 0
    angry_ratio: float = 0


class AnalyzePayload(BaseModel):
    mode: Literal["text", "url"]
    text: Optional[str] = None
    title: Optional[str] = ""
    url: Optional[str] = None
    meta: MetaPayload = Field(default_factory=MetaPayload)


@app.get("/api/health")
def health():
    sys_obj = get_system()
    return {
        "status": "ok",
        "model_loaded": sys_obj.model_loaded,
    }


@app.post("/api/analyze")
def analyze(
    payload: AnalyzePayload,
    db: Session = Depends(get_db),
    user: User | None = Depends(get_current_user),
):
    if user is None:
        return {"status": "error", "message": "Vui lòng đăng nhập để phân tích."}
    system = get_system()
    meta = payload.meta.model_dump()

    if payload.mode == "text":
        if not payload.text or not payload.text.strip():
            return {"status": "error", "message": "Nội dung trống."}
        result = system.infer(
            article_text=payload.text.strip(),
            article_title=payload.title or "",
            facebook_meta=meta,
        )
    else:
        if not payload.url or not payload.url.strip():
            return {"status": "error", "message": "URL trống."}
        result = system.infer(url=payload.url.strip(), facebook_meta=meta)

    if not result:
        return {"status": "error", "message": "Lỗi không xác định."}
    if result.get("status") == "error":
        return result

    history_id = save_analysis(
        db,
        user.id,
        payload.mode,
        meta,
        result,
        input_title=payload.title or "",
        input_url=payload.url.strip() if payload.url else None,
    )
    result["history_id"] = history_id
    return result
