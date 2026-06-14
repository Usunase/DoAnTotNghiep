"""Lớp truy cập cơ sở dữ liệu ShieldAI (SQLite + SQLAlchemy)."""

from backend.database.connection import DB_PATH, get_db, init_db
from backend.database.history_service import (
    delete_user_history,
    get_user_history,
    list_user_history,
    save_analysis,
)
from backend.database.models import AnalysisHistory, User

__all__ = [
    "DB_PATH",
    "User",
    "AnalysisHistory",
    "get_db",
    "init_db",
    "save_analysis",
    "list_user_history",
    "get_user_history",
    "delete_user_history",
]
