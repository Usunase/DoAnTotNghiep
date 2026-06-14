"""Hàm tiền xử lý văn bản tiếng Việt dùng chung (train + inference)."""
from __future__ import annotations

import re

from pyvi import ViTokenizer

URL_PATTERN = re.compile(r"http[s]?://\S+", re.IGNORECASE)
HTML_PATTERN = re.compile(r"<.*?>")


def remove_html(text: str) -> str:
    return HTML_PATTERN.sub(" ", text)


def remove_urls(text: str) -> str:
    return URL_PATTERN.sub("", text)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def segment_for_training(text: str) -> str:
    """Pipeline gọn cho train/embed: lower → xóa URL → tách từ PyVi."""
    if not isinstance(text, str) or not text:
        return ""
    text = text.lower()
    text = remove_urls(text)
    text = normalize_whitespace(text)
    if not text:
        return ""
    return ViTokenizer.tokenize(text)
