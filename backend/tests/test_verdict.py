import pytest

from backend.verdict import result_label_from_verdict, verdict_from_prob


@pytest.mark.parametrize(
    ("prob", "expected_verdict", "expected_label"),
    [
        (80, "fake", "TIN GIẢ (FAKE)"),
        (60, "suspicious", "ĐÁNG NGỜ"),
        (45, "suspicious", "ĐÁNG NGỜ"),
        (30, "real", "TIN THẬT (REAL)"),
    ],
)
def test_verdict_thresholds(prob, expected_verdict, expected_label):
    assert verdict_from_prob(prob) == expected_verdict
    assert result_label_from_verdict(expected_verdict) == expected_label


def test_verdict_boundary_values():
    assert verdict_from_prob(75) == "fake"
    assert verdict_from_prob(74.9) == "suspicious"
    assert verdict_from_prob(35) == "suspicious"
    assert verdict_from_prob(34.9) == "real"
