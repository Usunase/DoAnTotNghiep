"""Kiểm thử thu thập văn bản từ người dùng và crawl HTML."""
from unittest.mock import MagicMock, patch

from backend.data_crawler import DataCrawler


def test_get_article_from_text_success():
    crawler = DataCrawler()
    result = crawler.get_article_from_text(
        "Đây là nội dung bài viết đủ dài để kiểm thử hệ thống.",
        title="Tiêu đề thử",
    )
    assert result["status"] == "success"
    assert result["title"] == "Tiêu đề thử"
    assert "nội dung" in result["content"]
    assert result["source_domain"] == "user_input"


def test_get_article_from_text_empty():
    crawler = DataCrawler()
    result = crawler.get_article_from_text("   ")
    assert result["status"] == "error"


@patch("backend.data_crawler.requests.get")
def test_crawl_news_article_parses_html(mock_get):
    html = """
    <html><head><title>Fallback title</title></head>
    <body>
      <h1>Tin tức y tế</h1>
      <p>Đoạn văn đầu tiên của bài báo.</p>
      <p>Đoạn văn thứ hai cung cấp thêm ngữ cảnh.</p>
    </body></html>
  """
    mock_response = MagicMock()
    mock_response.content = html.encode("utf-8")
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    crawler = DataCrawler()
    result = crawler.crawl_news_article("https://vnexpress.net/bai-viet-test")

    assert result["status"] == "success"
    assert result["title"] == "Tin tức y tế"
    assert "Đoạn văn đầu tiên" in result["content"]
    assert result["source_domain"] == "vnexpress.net"
    assert result["original_url"].startswith("https://")
