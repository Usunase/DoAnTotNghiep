"""Trích xuất metadata & thống kê văn bản — dùng chung train / eval / inference."""
from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

USER_META_COLS = [
    "account_age_days",
    "followers",
    "is_verified",
    "share_speed",
    "angry_ratio",
]

TEXT_STAT_COLS = [
    "title_length",
    "uppercase_ratio",
    "exclamation_count",
    "question_count",
    "punctuation_density",
]

ALL_META_COLS = USER_META_COLS + TEXT_STAT_COLS

META_LABELS_VI = [
    "Tuổi tài khoản (ngày)",
    "Số follower",
    "Tích xanh (verified)",
    "Tốc độ share",
    "Tỷ lệ phẫn nộ",
    "Độ dài tiêu đề",
    "Tỷ lệ chữ IN HOA",
    "Số dấu ! trong tiêu đề",
    "Số dấu ? trong tiêu đề",
    "Mật độ dấu câu",
]


def simulate_user_signals(is_fake: bool) -> dict[str, float]:
    """Mô phỏng 5 metadata MXH theo nhãn tin giả / tin thật."""
    if is_fake:
        return {
            "account_age_days": float(np.random.randint(1, 1000)),
            "followers": float(np.random.randint(10, 50000)),
            "is_verified": float(np.random.choice([0, 1], p=[0.85, 0.15])),
            "share_speed": float(np.random.uniform(1.0, 50.0)),
            "angry_ratio": float(np.random.uniform(0.0, 0.9)),
        }
    return {
        "account_age_days": float(np.random.randint(100, 3650)),
        "followers": float(np.random.randint(500, 100000)),
        "is_verified": float(np.random.choice([0, 1], p=[0.60, 0.40])),
        "share_speed": float(np.random.uniform(0.1, 30.0)),
        "angry_ratio": float(np.random.uniform(0.0, 0.6)),
    }


def simulate_non_text_signals(row: pd.Series) -> pd.Series:
    return pd.Series(simulate_user_signals(bool(row["is_fake"])), index=USER_META_COLS)


def extract_text_stats(title: str, content: str) -> dict[str, float]:
    title = str(title or "")
    content = str(content or "")
    return {
        "title_length": float(len(title)),
        "uppercase_ratio": sum(1 for c in content if c.isupper()) / (len(content) + 1),
        "exclamation_count": float(title.count("!")),
        "question_count": float(title.count("?")),
        "punctuation_density": (
            content.count("!") + content.count("?") + content.count(".")
        ) / (len(content) + 1),
    }


def build_meta_vector(
    title: str,
    content: str,
    user_meta: dict[str, Any] | None = None,
) -> np.ndarray:
    """Vector 10 chiều cho inference (metadata người dùng + thống kê văn bản)."""
    meta = user_meta or {}
    user_vals = [float(meta.get(col, 0.0)) for col in USER_META_COLS]
    stats = extract_text_stats(title, content)
    stat_vals = [stats[col] for col in TEXT_STAT_COLS]
    return np.array(user_vals + stat_vals, dtype=np.float64)


def add_metadata_features(
    df: pd.DataFrame,
    random_state: int | None = 42,
    simulate_user: bool = True,
) -> pd.DataFrame:
    """Thêm cột metadata mô phỏng + thống kê văn bản vào DataFrame."""
    out = df.copy()
    if "title" in out.columns:
        out["title"] = out["title"].fillna("")
    out["content"] = out["content"].fillna("")

    if random_state is not None:
        np.random.seed(random_state)

    if simulate_user:
        out[USER_META_COLS] = out.apply(simulate_non_text_signals, axis=1)

    stats = out.apply(
        lambda row: pd.Series(extract_text_stats(row["title"], row["content"])),
        axis=1,
    )
    out[TEXT_STAT_COLS] = stats[TEXT_STAT_COLS]
    return out
