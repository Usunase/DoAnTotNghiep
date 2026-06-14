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
    text = "Hôm nay tôi thấy bài báo đó viết sai sự thật wa j luôn á mọi ng ơi!!! Vào web xem nè http://fake.vn <br> Quá bức xúc!"
    final_output = cleaner.pipeline_clean(text)
    
    # Should be lowercased, teencode fixed, urls removed, special characters removed, pyvi tokenized
    assert "http" not in final_output
    assert "br" not in final_output
    assert "!!!" not in final_output
    assert "quá" in final_output
    assert "_" in final_output # PyVi segmentation uses underscores
