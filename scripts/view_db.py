#!/usr/bin/env python3
"""Xem nhanh nội dung SQLite ShieldAI trong terminal."""
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.database import DB_PATH


def main() -> None:
    if not DB_PATH.exists():
        print(f"Chưa có database: {DB_PATH}")
        print("Chạy ./run_web.sh và đăng ký tài khoản trước.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print(f"Database: {DB_PATH}\n")

    print("=== BẢNG ===")
    for row in cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    ):
        count = cur.execute(f"SELECT COUNT(*) FROM {row[0]}").fetchone()[0]
        print(f"  {row[0]:20} ({count} dòng)")

    print("\n=== TÀI KHOẢN (users) ===")
    users = cur.execute(
        "SELECT id, email, username, created_at FROM users ORDER BY id"
    ).fetchall()
    if not users:
        print("  (trống)")
    for u in users:
        print(f"  [{u['id']}] {u['username']} <{u['email']}> — {u['created_at']}")

    print("\n=== LỊCH SỬ PHÂN TÍCH (analysis_history) ===")
    rows = cur.execute(
        """
        SELECT id, user_id, input_mode, title, result_label,
               ROUND(fake_prob, 2) AS fake_prob, created_at
        FROM analysis_history
        ORDER BY id DESC
        LIMIT 20
        """
    ).fetchall()
    if not rows:
        print("  (trống)")
    for r in rows:
        title = (r["title"] or "—")[:50]
        print(
            f"  #{r['id']} user={r['user_id']} [{r['input_mode']}] "
            f"{r['fake_prob']}% — {title} — {r['created_at']}"
        )

    conn.close()
    print("\nGợi ý: cài DB Browser for SQLite hoặc extension 'SQLite Viewer' trong Cursor.")


if __name__ == "__main__":
    main()
