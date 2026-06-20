"""Kiểm tra ngưỡng giải thích khớp verdict.py."""
from backend.explanation_engine import _phobert_summary, _scan_text_signals, build_explanation
from backend.verdict import FAKE_THRESHOLD, SUSPICIOUS_THRESHOLD, verdict_from_prob


def test_phobert_summary_aligns_with_verdict_thresholds():
    fake_text = _phobert_summary(80)["text"]
    suspicious_text = _phobert_summary(50)["text"]
    real_text = _phobert_summary(20)["text"]

    assert verdict_from_prob(80) == "fake"
    assert "tin giả" in fake_text.lower()

    assert verdict_from_prob(50) == "suspicious"
    assert "đối chiếu" in suspicious_text.lower()

    assert verdict_from_prob(20) == "real"
    assert "chính thống" in real_text.lower()


def test_phobert_summary_boundary_at_fake_threshold():
    at_fake = _phobert_summary(FAKE_THRESHOLD)["text"]
    below_fake = _phobert_summary(FAKE_THRESHOLD - 0.1)["text"]
    assert "tin giả" in at_fake.lower()
    assert "đối chiếu" in below_fake.lower()


def test_phobert_summary_boundary_at_suspicious_threshold():
    at_suspicious = _phobert_summary(SUSPICIOUS_THRESHOLD)["text"]
    below_suspicious = _phobert_summary(SUSPICIOUS_THRESHOLD - 0.1)["text"]
    assert "đối chiếu" in at_suspicious.lower()
    assert "chính thống" in below_suspicious.lower()


def test_scan_text_signals_detects_sensational_language():
    signals = _scan_text_signals(
        "CẢNH BÁO KHẨN CẤP!!! CHIA SẺ NGAY!!!",
        "Tin nóng",
    )
    types = {s["type"] for s in signals}
    assert "text_risk" in types


def test_build_explanation_matches_verdict_for_fake():
    explanation = build_explanation(
        fake_prob=85.0,
        raw_data={
            "title": "SỐC!!!",
            "content": "CẢNH BÁO KHẨN CẤP!!! CHIA SẺ NGAY!!! Tin đồn lan truyền.",
        },
    )
    assert explanation["verdict"] == "fake"
    assert "TIN GIẢ" in explanation["headline"].upper()
    assert explanation["model_confidence"] == 85.0
    assert len(explanation["primary_reasons"]) >= 1


def test_build_explanation_real_news_tone():
    explanation = build_explanation(
        fake_prob=10.0,
        raw_data={
            "title": "Theo Bộ Y tế",
            "content": (
                "Theo vnexpress bác sĩ tại bệnh viện cho biết tình hình dịch bệnh "
                "đang được kiểm soát tốt với nhiều biện pháp phòng ngừa hợp lý."
            ),
        },
    )
    assert explanation["verdict"] == "real"
    assert "TIN THẬT" in explanation["headline"].upper()
