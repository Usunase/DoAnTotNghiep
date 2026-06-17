"""Phân loại 3 mức từ xác suất tin giả — dùng chung train UI, API, giải thích."""
from __future__ import annotations

from typing import Literal

Verdict = Literal["fake", "suspicious", "real"]

FAKE_THRESHOLD = 75.0
SUSPICIOUS_THRESHOLD = 35.0


def verdict_from_prob(fake_prob: float) -> Verdict:
    if fake_prob >= FAKE_THRESHOLD:
        return "fake"
    if fake_prob >= SUSPICIOUS_THRESHOLD:
        return "suspicious"
    return "real"


def result_label_from_verdict(verdict: Verdict) -> str:
    if verdict == "fake":
        return "TIN GIẢ (FAKE)"
    if verdict == "suspicious":
        return "ĐÁNG NGỜ"
    return "TIN THẬT (REAL)"
