from __future__ import annotations

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    analyses: Mapped[list[AnalysisHistory]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
    feedbacks: Mapped[list[Feedback]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


class AnalysisHistory(Base):
    """Lịch sử phân tích bài báo của từng tài khoản."""

    __tablename__ = "analysis_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    input_mode: Mapped[str] = mapped_column(String(10))  # text | url
    title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    source_domain: Mapped[str | None] = mapped_column(String(255), nullable=True)
    result_label: Mapped[str] = mapped_column(String(64))
    fake_prob: Mapped[float] = mapped_column(Float)
    verdict: Mapped[str | None] = mapped_column(String(32), nullable=True)
    explanation_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    meta_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        index=True,
    )

    user: Mapped[User] = relationship(back_populates="analyses")
    feedback: Mapped[Feedback | None] = relationship(
        back_populates="analysis",
        cascade="all, delete-orphan",
        uselist=False,
    )

class Feedback(Base):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    history_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("analysis_history.id", ondelete="CASCADE"),
        unique=True,
        index=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    is_correct: Mapped[bool] = mapped_column(Boolean, nullable=False)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[object] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    analysis: Mapped[AnalysisHistory] = relationship(back_populates="feedback")
    user: Mapped[User] = relationship(back_populates="feedbacks")
