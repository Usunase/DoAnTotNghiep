"""
Sinh giải thích "tại sao" sau khi phân loại tin thật / tin giả.
Dựa trên phân tích văn bản và xác suất mô hình (rule-based).
"""
from __future__ import annotations

import re
from typing import Any

from backend.verdict import FAKE_THRESHOLD, SUSPICIOUS_THRESHOLD, verdict_from_prob

SENSATIONAL_PATTERNS = [
    (r"cảnh báo|khẩn cấp|tin nóng|tin cực|sốc|kinh hoàng|chấn động", "Ngôn ngữ giật gân, kích động"),
    (r"chia sẻ ngay|share ngay|đừng bỏ lỡ|gấp", "Kêu gọi lan truyền gấp"),
    (r"không thể tin|tin đồn|đồn thất", "Cụm từ gợi tin đồn, chưa kiểm chứng"),
    (r"100%|chắc chắn|tuyệt đối|không nghi ngờ", "Khẳng định tuyệt đối thiếu căn cứ"),
]

POSITIVE_PATTERNS = [
    (r"bác sĩ|theo.*(bệnh viện|bộ y tế|chính phủ)|nguồn tin", "Có dấu hiệu trích nguồn / chuyên gia"),
    (r"theo (vnexpress|tuoitre|thanh niên|reuters|afp)", "Trích dẫn nguồn báo chí"),
]


def _scan_text_signals(content: str, title: str, source: str = "") -> list[dict[str, Any]]:
    text = f"{title} {content}"
    text_lower = text.lower()
    signals = []

    for pattern, desc in SENSATIONAL_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            signals.append({"type": "text_risk", "text": desc, "weight": 2})

    for pattern, desc in POSITIVE_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            signals.append({"type": "text_trust", "text": desc, "weight": 2})

    if "njj.de.com" in text_lower or (source and "njj.de.com" in source.lower()):
        signals.append({
            "type": "text_risk",
            "text": "Nguồn tin hoặc đường dẫn chứa URL độc hại (njj.de.com), mang tính thao túng người dùng, tỉ lệ tin giả rất cao (80-100%).",
            "weight": 10,
        })

    low_credibility_sources = [
        "blogspot", "wordpress", "tinnhanh", "tinhoatoc", "tin24h", "giaitri", 
        "showbiz", "tamlinh", "bí mật", "bimat", "tinrao", "hóng", "bocphot"
    ]
    if source and any(lc in source.lower() for lc in low_credibility_sources):
        signals.append({
            "type": "text_risk",
            "text": "Nguồn phát có độ tin cậy thấp (Blog cá nhân, báo lá cải hoặc ẩn danh)",
            "weight": 3,
        })
        
    social_media_sources = ["facebook", "fb", "tiktok", "zalo", "youtube", "mạng xã hội", "instagram", "twitter", "x.com"]
    if source and any(sm in source.lower() for sm in social_media_sources):
        signals.append({
            "type": "text_risk",
            "text": "Nguồn phát từ mạng xã hội (thiếu kiểm duyệt, độ tin cậy thấp)",
            "weight": 3,
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
            "text": f"Nội dung quá ngắn ({word_count} từ) — khó kiểm chứng, hay gặp ở tin đồn",
            "weight": 1,
        })

    t_len = len(text) + 1
    uppercase_ratio = sum(1 for c in text if c.isupper()) / t_len
    exclamations = text.count("!")
    questions = text.count("?")
    url_count = len(re.findall(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        text,
    ))
    repeated_chars = sum(1 for _ in re.finditer(r"(.)\1{2,}", text)) / t_len

    if uppercase_ratio > 0.15:
        signals.append({
            "type": "text_risk",
            "text": f"Tỷ lệ in hoa bất thường ({uppercase_ratio * 100:.0f}%) — dấu hiệu thao túng cảm xúc",
            "weight": 2,
        })

    if exclamations >= 3:
        signals.append({
            "type": "text_risk",
            "text": f"Lạm dụng dấu chấm than ({exclamations} lần) — thường gặp ở tin giật tít",
            "weight": 2,
        })
    elif exclamations == 0:
        signals.append({
            "type": "text_trust",
            "text": "Không lạm dụng dấu chấm than — văn phong điềm tĩnh",
            "weight": 1,
        })

    if questions >= 3:
        signals.append({
            "type": "text_risk",
            "text": f"Nhiều câu hỏi ({questions} lần) — thủ pháp gieo rắc hoang mang",
            "weight": 1,
        })

    if url_count >= 3:
        signals.append({
            "type": "text_risk",
            "text": "Chứa nhiều liên kết URL đáng ngờ (đặc điểm của tin rác/spam)",
            "weight": 2,
        })

    if repeated_chars > 0.05:
        signals.append({
            "type": "text_risk",
            "text": "Cố tình kéo dài ký tự (ví dụ: 'quáaaa') — ngôn ngữ thiếu chuyên nghiệp",
            "weight": 1,
        })

    return signals


def _phobert_summary(fake_prob: float) -> dict[str, str]:
    """Dùng cùng ngưỡng với verdict.py (75% / 35%)."""
    if fake_prob >= FAKE_THRESHOLD:
        return {
            "type": "model",
            "text": (
                "Mạng học sâu đánh giá văn bản có ngữ nghĩa tương đồng với tin giả "
                "(văn phong kích động, phi logic hoặc chứa thông tin sai lệch)."
            ),
        }
    if fake_prob >= SUSPICIOUS_THRESHOLD:
        return {
            "type": "model",
            "text": (
                "Mạng học sâu nhận thấy thông tin có cả đặc điểm thật và giả — "
                "cần đối chiếu thêm với nguồn tin chính thống."
            ),
        }
    return {
        "type": "model",
        "text": (
            "Mạng học sâu đánh giá ngữ cảnh phù hợp với tin tức chính thống "
            "(khách quan, mạch lạc, ít dấu hiệu thao túng)."
        ),
    }


def build_explanation(
    fake_prob: float,
    raw_data: dict,
) -> dict[str, Any]:
    """Trả về cấu trúc giải thích cho UI."""
    verdict = verdict_from_prob(fake_prob)
    content = str(raw_data.get("content", ""))
    title = str(raw_data.get("title", ""))
    source = str(raw_data.get("source", raw_data.get("source_domain", "")))

    text_signals = _scan_text_signals(content, title, source)
    model_note = _phobert_summary(fake_prob)

    risk_points = [s for s in text_signals if s["type"].endswith("_risk")]
    trust_points = [s for s in text_signals if s["type"].endswith("_trust")]

    risk_points.sort(key=lambda x: -x.get("weight", 0))
    trust_points.sort(key=lambda x: -x.get("weight", 0))

    if verdict == "fake":
        headline = "Vì sao hệ thống cho rằng đây là TIN GIẢ?"
        summary = (
            f"Mô hình PhoBERT gán {fake_prob:.1f}% xác suất tin giả. "
            "Các yếu tố dưới đây là cơ sở cho quyết định phân loại này."
        )
        primary = [s["text"] for s in risk_points[:5]]
        secondary = [s["text"] for s in trust_points[:2]]
        counter = "Một số điểm ủng hộ tin thật (nếu có)" if trust_points else None
    elif verdict == "suspicious":
        headline = "Vì sao tin này ĐÁNG NGỜ?"
        summary = (
            f"Xác suất tin giả là {fake_prob:.1f}% — chưa đủ dữ kiện để khẳng định hoàn toàn, "
            "nhưng văn bản có nhiều dấu hiệu đáng ngờ."
        )
        primary = [s["text"] for s in risk_points[:4]]
        secondary = [s["text"] for s in trust_points[:3]]
        counter = "Điểm ủng hộ độ tin cậy"
    else:
        headline = "Vì sao hệ thống cho rằng đây là TIN THẬT?"
        summary = (
            f"Xác suất tin giả ở mức an toàn ({fake_prob:.1f}%). "
            "Phân tích ngữ nghĩa phản ánh tính chuyên nghiệp của bài báo."
        )
        primary = [s["text"] for s in trust_points[:5]]
        secondary = [s["text"] for s in risk_points[:2]]
        counter = "Một số điểm rủi ro cần lưu ý (nếu có)" if risk_points else None

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
    }
