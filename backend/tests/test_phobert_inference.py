"""Kiểm thử pipeline suy luận (mock PhoBERT — không tải model nặng)."""
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from backend.phobert_inference import PhoBERTInferenceSystem


def _make_system_without_init() -> PhoBERTInferenceSystem:
    return PhoBERTInferenceSystem.__new__(PhoBERTInferenceSystem)


def test_infer_fails_when_model_not_loaded():
    system = _make_system_without_init()
    system.model_loaded = False
    system.verbose = False

    result = system.infer(article_text="nội dung đủ dài để kiểm tra lỗi thiếu model")
    assert result["status"] == "error"
    assert "train" in result["message"].lower()


def test_module_1_rejects_short_content():
    system = _make_system_without_init()
    system.verbose = False
    system.crawler = MagicMock()
    system.crawler.get_article_from_text.return_value = {
        "status": "success",
        "title": "Ngắn",
        "content": "một hai ba",
    }

    clean, raw = system.module_1_data_acquisition_and_preprocessing(
        article_text="một hai ba",
    )
    assert clean is None
    assert raw["status"] == "error"


def test_module_3_classification_fake_verdict():
    system = _make_system_without_init()
    system.verbose = False
    system.scaler = MagicMock()
    system.scaler.transform.return_value = np.zeros((1, 768))
    system.classifier = MagicMock()
    system.classifier.classes_ = [False, True]
    system.classifier.predict_proba.return_value = np.array([[0.1, 0.82]])

    result, fake_prob, verdict = system.module_3_classification(np.zeros(768))

    assert verdict == "fake"
    assert fake_prob == pytest.approx(82.0)
    assert "FAKE" in result


@patch("backend.phobert_inference.build_explanation")
@patch.object(PhoBERTInferenceSystem, "module_3_classification")
@patch.object(PhoBERTInferenceSystem, "module_2_phobert_embedding")
@patch.object(PhoBERTInferenceSystem, "module_1_data_acquisition_and_preprocessing")
def test_infer_success_pipeline(
    mock_m1,
    mock_m2,
    mock_m3,
    mock_explain,
):
    mock_m1.return_value = ("clean_text", {"content": "raw", "title": "t"})
    mock_m2.return_value = np.zeros(768)
    mock_m3.return_value = ("ĐÁNG NGỜ", 50.0, "suspicious")
    mock_explain.return_value = {"verdict": "suspicious", "headline": "h"}

    system = _make_system_without_init()
    system.model_loaded = True
    system.verbose = False

    out = system.infer(article_text="nội dung bài viết đủ dài cho pipeline kiểm thử")

    assert out["status"] == "success"
    assert out["verdict"] == "suspicious"
    assert out["fake_prob"] == 50.0
    mock_m1.assert_called_once()
    mock_m2.assert_called_once_with("clean_text")
    mock_m3.assert_called_once()
    mock_explain.assert_called_once()
