"""
Sinh giải thích "tại sao" sau khi phân loại tin thật / tin giả.
Dựa trên đặc trưng văn bản, metadata và xác suất mô hình (rule-based + heuristic).
"""
from __future__ import annotations

import re
from typing import Any

from backend.feature_extraction import META_LABELS_VI as META_LABELS

SENSATIONAL_PATTERNS = [
    (r"cảnh báo|khẩn cấp|tin nóng|tin cực|sốc|kinh hoàng|chấn động", "Ngôn ngữ giật gân, kích động"),
    (r"chia sẻ ngay|share ngay|đừng bỏ lỡ|gấp", "Kêu gọi lan truyền gấp"),
    (r"!\s*!|!!!", "Lạm dụng dấu chấm than"),
    (r"không thể tin|tin đồn|đồn thất", "Cụm từ gợi tin đồn, chưa kiểm chứng"),
    (r"100%|chắc chắn|tuyệt đối|không nghi ngờ", "Khẳng định tuyệt đối thiếu căn cứ"),
]

POSITIVE_PATTERNS = [
    (r"bác sĩ|theo.*(bệnh viện|bộ y tế|chính phủ)|nguồn tin", "Có dấu hiệu trích nguồn / chuyên gia"),
    (r"theo (vnexpress|tuoitre|thanh niên|reuters|afp)", "Trích dẫn nguồn báo chí"),
]


def _verdict_label(fake_prob: float) -> str:
    if fake_prob >= 75:
        return "fake"
    if fake_prob >= 35:
        return "suspicious"
    return "real"


def _scan_text_signals(content: str, title: str) -> list[dict[str, Any]]:
    text = f"{title} {content}".lower()
    signals = []

    for pattern, desc in SENSATIONAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            signals.append({"type": "text_risk", "text": desc, "weight": 2})

    for pattern, desc in POSITIVE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            signals.append({"type": "text_trust", "text": desc, "weight": 2})

    excl = title.count("!") + content.count("!")
    if excl >= 3:
        signals.append({
            "type": "text_risk",
            "text": f"Nhiều dấu chấm than ({excl} lần) — thường gặp ở tin giật tít",
            "weight": 1,
        })
    elif excl == 0:
        signals.append({
            "type": "text_trust",
            "text": "Không lạm dụng dấu chấm than trong tiêu đề/nội dung",
            "weight": 1,
        })

    upper = sum(1 for c in content if c.isupper())
    if upper > 30:
        signals.append({
            "type": "text_risk",
            "text": f"Nhiều chữ IN HOA ({upper} ký tự) — dấu hiệu thao túng cảm xúc",
            "weight": 1,
        })

    word_count = len(content.split())
    if word_count >= 80:
        signals.append({
            "type": "text_trust",
            "text": f"Nội dung đủ dài ({word_count} từ) — có khả năng là bài báo hoàn chỉnh",
            "weight": 1,
        })
    elif word_count < 30:
        signals.append({
            "type": "text_risk",
            "text": f"Nội dung ngắn ({word_count} từ) — khó kiểm chứng, hay gặp ở tin đồn",
            "weight": 1,
        })

    return signals


def _meta_fields_provided(meta: dict) -> bool:
    """True khi người dùng đã nhập ít nhất một trường metadata (khác mặc định 0)."""
    return (
        meta.get("account_age_days", 0) > 0
        or meta.get("followers", 0) > 0
        or meta.get("share_speed", 0) > 0
        or meta.get("angry_ratio", 0) > 0
        or bool(meta.get("is_verified"))
    )


def _scan_meta_signals(meta: dict, meta_vector: list[float]) -> list[dict[str, Any]]:
    signals = []
    mv = meta_vector

    angry = meta.get("angry_ratio", 0)
    if angry > 0:
        if angry >= 0.4:
            signals.append({
                "type": "meta_risk",
                "text": f"Tỷ lệ phẫn nộ cao ({angry*100:.0f}%) — phản ứng tiêu cực mạnh",
                "weight": 2,
            })
        elif angry < 0.2:
            signals.append({
                "type": "meta_trust",
                "text": "Tỷ lệ phẫn nộ thấp — ít dấu hiệu kích động từ cộng đồng",
                "weight": 1,
            })

    share = meta.get("share_speed", 0)
    if share > 0 and share >= 30:
        signals.append({
            "type": "meta_risk",
            "text": f"Tốc độ share cao ({share:.0f}/phút) — lan truyền bất thường",
            "weight": 2,
        })

    age = meta.get("account_age_days", 0)
    if age > 0:
        if age < 60:
            signals.append({
                "type": "meta_risk",
                "text": f"Tài khoản mới ({age:.0f} ngày) — độ tin cậy nguồn thấp",
                "weight": 2,
            })
        elif age >= 180:
            signals.append({
                "type": "meta_trust",
                "text": f"Tài khoản tồn tại lâu ({age:.0f} ngày)",
                "weight": 1,
            })

    if _meta_fields_provided(meta):
        if meta.get("is_verified"):
            signals.append({
                "type": "meta_trust",
                "text": "Nguồn có tích xanh (verified)",
                "weight": 2,
            })
        else:
            signals.append({
                "type": "meta_risk",
                "text": "Không có tích xanh xác thực — nguồn chưa được xác minh",
                "weight": 1,
            })

    followers = meta.get("followers", 0)
    if followers > 0 and followers < 200:
        signals.append({
            "type": "meta_risk",
            "text": f"Số follower thấp ({followers:.0f})",
            "weight": 1,
        })

  # Thống kê từ meta_vector
    if len(mv) >= 10 and mv[8] + mv[7] >= 3:  # ! + ?
        signals.append({
            "type": "text_risk",
            "text": "Tiêu đề có nhiều dấu câu cảm xúc (!/?)",
            "weight": 1,
        })

    return signals


def _phobert_summary(fake_prob: float) -> dict[str, str]:
    """Mô tả định tính nhánh ngữ nghĩa PhoBERT (không giải thích từng chiều 768)."""
    if fake_prob >= 60:
        return {
            "type": "model",
            "text": (
                "PhoBERT phát hiện ngữ nghĩa gần với các mẫu tin giả trong tập huấn luyện "
                "(giọng điệu kích động, mơ hồ, thiếu căn cứ)."
            ),
        }
    if fake_prob <= 40:
        return {
            "type": "model",
            "text": (
                "PhoBERT đánh giá văn phong và ngữ cảnh tương đồng tin thật "
                "(khách quan, mạch lạc, ít dấu hiệu thao túng)."
            ),
        }
    return {
        "type": "model",
        "text": (
            "PhoBERT thấy ngữ nghĩa có cả dấu hiệu tin thật lẫn đáng ngờ — "
            "cần đối chiếu metadata và nguồn."
        ),
    }


def build_explanation(
    fake_prob: float,
    raw_data: dict,
    meta: dict,
    meta_vector: list[float],
) -> dict[str, Any]:
    """
    Trả về cấu trúc giải thích cho UI.
    """
    verdict = _verdict_label(fake_prob)
    content = str(raw_data.get("content", ""))
    title = str(raw_data.get("title", ""))

    text_signals = _scan_text_signals(content, title)
    meta_signals = _scan_meta_signals(meta, meta_vector)
    model_note = _phobert_summary(fake_prob)

    risk_points = [s for s in text_signals + meta_signals if s["type"].endswith("_risk")]
    trust_points = [s for s in text_signals + meta_signals if s["type"].endswith("_trust")]

    risk_points.sort(key=lambda x: -x.get("weight", 0))
    trust_points.sort(key=lambda x: -x.get("weight", 0))

    if verdict == "fake":
        headline = "Vì sao hệ thống cho rằng đây là TIN GIẢ?"
        summary = (
            f"Mô hình hybrid (PhoBERT + metadata) gán {fake_prob:.1f}% xác suất tin giả. "
            "Các yếu tố dưới đây là tín hiệu chính hỗ trợ kết luận này."
        )
        primary = [s["text"] for s in risk_points[:5]]
        secondary = [s["text"] for s in trust_points[:2]]
        counter = "Một số điểm ủng hộ tin thật (nếu có)" if trust_points else None
    elif verdict == "suspicious":
        headline = "Vì sao tin này ĐÁNG NGỜ?"
        summary = (
            f"Xác suất tin giả {fake_prob:.1f}% — chưa đủ mạnh để khẳng định hoàn toàn, "
            "nhưng có nhiều tín hiệu cần kiểm chứng thêm."
        )
        primary = [s["text"] for s in risk_points[:4]]
        secondary = [s["text"] for s in trust_points[:3]]
        counter = "Điểm ủng hộ độ tin cậy"
    else:
        headline = "Vì sao hệ thống cho rằng đây là TIN THẬT?"
        summary = (
            f"Mô hình đánh giá xác suất tin giả chỉ {fake_prob:.1f}%. "
            "Nội dung và nguồn phát thể hiện các đặc điểm tương đối đáng tin."
        )
        primary = [s["text"] for s in trust_points[:5]]
        secondary = [s["text"] for s in risk_points[:2]]
        counter = "Một số điểm cần lưu ý (nếu có)" if risk_points else None

    if not primary:
        primary = [model_note["text"]]
    else:
        primary = [model_note["text"]] + primary

    return {
        "verdict": verdict,
        "headline": headline,
        "summary": summary,
        "primary_reasons": primary,
        "counter_points": secondary,
        "counter_label": counter,
        "model_confidence": fake_prob,
        "meta_breakdown": [
            {"label": META_LABELS[i], "value": meta_vector[i]}
            for i in range(min(len(META_LABELS), len(meta_vector)))
        ],
    }
