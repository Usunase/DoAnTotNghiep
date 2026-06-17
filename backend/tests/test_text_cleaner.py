import pytest
from backend.text_cleaner import TextCleaner

@pytest.fixture
def cleaner():
    return TextCleaner()

def test_remove_html_and_urls(cleaner):
    text = "Truy cập <a href='http://fake.vn'>vào đây</a> để biết thêm chi tiết http://vnexpress.net"
    cleaned = cleaner.remove_html_and_urls(text)
    # Check if html tags and urls are removed
    assert "href" not in cleaned
    assert "http" not in cleaned
    assert "vào đây" in cleaned

def test_normalize_teencode(cleaner):
    text = "Hôm nay tôi thấy bài báo đó viết sai sự thật wa j luôn á mọi ng ơi"
    normalized = cleaner.normalize_teencode(text)
    assert "quá" in normalized
    assert "gì" in normalized
    assert "người" in normalized
    assert "wa" not in normalized
    assert "j" not in normalized

def test_pipeline_clean(cleaner):
    text = "Tin nóng tại https://example.com cần kiểm chứng gấp!!!"
    final_output = cleaner.pipeline_clean(text)

    assert "http" not in final_output
    assert "example.com" not in final_output
    assert final_output == final_output.lower()
    assert "_" in final_output
