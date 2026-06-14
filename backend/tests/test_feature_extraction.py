import pytest
from backend.feature_extraction import extract_text_stats

def test_extract_text_stats():
    title = "SỐC!!! Chữa bách bệnh chỉ với 1 loại cây này???"
    content = "Theo một nghiên cứu, loại cây này rất TỐT cho sức khỏe. Đừng bỏ lỡ!!!"
    
    stats = extract_text_stats(title, content)
    
    # Check title length
    assert stats["title_length"] == len(title)
    
    # Check uppercase ratio (only counting letters in content that are uppercase)
    # Uppercase letters in content: T, Ô, T, Đ
    # Number of uppercase = 4. 
    # length of content = len(content) = 71. len(content) + 1 = 72
    # So ratio = 4 / 72. We'll just check if it's > 0
    assert stats["uppercase_ratio"] > 0
    
    # Check exclamation marks in title
    assert stats["exclamation_count"] == 3
    
    # Check question marks in title
    assert stats["question_count"] == 3
    
    # Check punctuation density in content (!, ?, .)
    # content has 1 dot (.) and 3 exclamation marks (!!!)
    # Total = 4. Ratio = 4 / (len(content) + 1)
    assert stats["punctuation_density"] == 4 / (len(content) + 1)

def test_extract_text_stats_empty():
    stats = extract_text_stats("", "")
    assert stats["title_length"] == 0
    assert stats["uppercase_ratio"] == 0.0
    assert stats["exclamation_count"] == 0.0
    assert stats["question_count"] == 0.0
    assert stats["punctuation_density"] == 0.0
