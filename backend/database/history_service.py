from __future__ import annotations

import json
from typing import Any

from sqlalchemy.orm import Session

from backend.database.models import AnalysisHistory

PREVIEW_LEN = 200


def save_analysis(
    db: Session,
    user_id: int,
    input_mode: str,
    result: dict[str, Any],
    *,
    input_title: str = "",
    input_url: str | None = None,
) -> int:
    raw = result.get("raw_data") or {}
    explanation = result.get("explanation") or {}

    record = AnalysisHistory(
        user_id=user_id,
        input_mode=input_mode,
        title=(raw.get("title") or input_title or "")[:500],
        content=raw.get("content") or "",
        source_url=raw.get("original_url") or input_url,
        source_domain=raw.get("source_domain"),
        result_label=result.get("result", ""),
        fake_prob=float(result.get("fake_prob", 0)),
        verdict=explanation.get("verdict"),
        explanation_json=json.dumps(explanation, ensure_ascii=False),
        meta_json="{}",
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record.id


def list_user_history(
    db: Session,
    user_id: int,
    *,
    limit: int = 50,
    offset: int = 0,
) -> tuple[list[dict[str, Any]], int]:
    query = (
        db.query(AnalysisHistory)
        .filter(AnalysisHistory.user_id == user_id)
        .order_by(AnalysisHistory.created_at.desc())
    )
    total = query.count()
    rows = query.offset(offset).limit(limit).all()
    items = [_to_summary(row) for row in rows]
    return items, total


def get_user_history(
    db: Session,
    user_id: int,
    history_id: int,
) -> dict[str, Any] | None:
    row = (
        db.query(AnalysisHistory)
        .filter(
            AnalysisHistory.id == history_id,
            AnalysisHistory.user_id == user_id,
        )
        .first()
    )
    if row is None:
        return None
    return _to_detail(row)


def delete_user_history(db: Session, user_id: int, history_id: int) -> bool:
    row = (
        db.query(AnalysisHistory)
        .filter(
            AnalysisHistory.id == history_id,
            AnalysisHistory.user_id == user_id,
        )
        .first()
    )
    if row is None:
        return False
    db.delete(row)
    db.commit()
    return True


def _preview(text: str | None) -> str:
    if not text:
        return ""
    text = text.strip()
    if len(text) <= PREVIEW_LEN:
        return text
    return text[:PREVIEW_LEN] + "…"


def _to_summary(row: AnalysisHistory) -> dict[str, Any]:
    created = row.created_at
    return {
        "id": row.id,
        "input_mode": row.input_mode,
        "title": row.title or "—",
        "preview": _preview(row.content),
        "source_url": row.source_url,
        "source_domain": row.source_domain,
        "result_label": row.result_label,
        "fake_prob": row.fake_prob,
        "verdict": row.verdict,
        "created_at": created.isoformat() if created else None,
    }


def _to_detail(row: AnalysisHistory) -> dict[str, Any]:
    explanation = {}
    if row.explanation_json:
        try:
            explanation = json.loads(row.explanation_json)
        except json.JSONDecodeError:
            explanation = {}

    return {
        "status": "success",
        "history_id": row.id,
        "result": row.result_label,
        "verdict": row.verdict or explanation.get("verdict"),
        "fake_prob": row.fake_prob,
        "raw_data": {
            "title": row.title,
            "content": row.content,
            "source_domain": row.source_domain,
            "original_url": row.source_url,
        },
        "explanation": explanation,
        "feedback": {
            "is_correct": row.feedback.is_correct,
            "comment": row.feedback.comment,
        } if row.feedback else None,
        "created_at": row.created_at.isoformat() if row.created_at else None,
    }

