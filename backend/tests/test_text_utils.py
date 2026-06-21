import pytest

from backend.text_cleaner import TextCleaner
from backend.text_utils import preprocess_text, segment_for_training


def test_preprocess_text_basic():
    text = "Tin nóng tại https://example.com cần kiểm chứng gấp!"
    out = preprocess_text(text)
    assert "http" not in out
    assert "example.com" not in out
    assert "_" in out  # PyVi tokenization


def test_segment_for_training_matches_preprocess_text():
    sample = "Người bệnh cúm nên uống đủ nước mỗi ngày."
    assert segment_for_training(sample) == preprocess_text(sample)


def test_text_cleaner_pipeline_matches_preprocess_text():
    cleaner = TextCleaner()
    sample = "CẢNH BÁO!!! Chia sẻ ngay http://fake.vn tin cực hot"
    assert cleaner.pipeline_clean(sample) == preprocess_text(sample)


def test_preprocess_text_empty():
    assert preprocess_text("") == ""
    assert preprocess_text(None) == ""
