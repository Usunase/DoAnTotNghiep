import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

class DataCrawler:
    """
    Hệ thống Crawler Đa Dụng (Scraping) thu thập dữ liệu báo điện tử từ URL.
    """
    def __init__(self):
        # Fake User-Agent để tránh bị block bởi trình tường lửa chống bot
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def crawl_news_article(self, url):
        """
        Nhận vào 1 URL, dùng BeautifulSoup tải và bóc tách nội dung HTML.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status() # Bắn lỗi nếu status code là báo 4xx, 5xx
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Trích xuất Tiêu đề (Title) thường nằm trong thẻ <h1>
            h1_tag = soup.find('h1')
            title = h1_tag.get_text().strip() if h1_tag else soup.title.string.strip() if soup.title else ""
            
            # Trích xuất Nội dung: Gộp toàn bộ văn bản trong các thẻ <p>
            paragraphs = soup.find_all('p')
            content = " ".join([p.get_text().strip() for p in paragraphs])
            
            # Trích xuất Tên miền Nguồn gốc (Domain Source)
            parsed_uri = urlparse(url)
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            
            # Mô phỏng ngày lấy dữ liệu (crawled_at)
            crawled_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            return {
                "status": "success",
                "title": title,
                "content": content,
                "source_domain": domain,
                "crawled_at": crawled_at,
                "original_url": url
            }
            
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    def get_article_from_text(self, raw_text, title="", author_metadata=None):
        """Nhận nội dung bài báo do người dùng dán trực tiếp."""
        if not raw_text or not str(raw_text).strip():
            return {"status": "error", "message": "Nội dung bài báo trống."}

        crawled_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "status": "success",
            "title": (title or "Bài viết người dùng nhập").strip(),
            "content": raw_text.strip(),
            "source_domain": "user_input",
            "crawled_at": crawled_at,
            "metadata": author_metadata or {},
        }

    def get_facebook_post(self, raw_text, author_metadata=None):
        """Giữ tương thích code cũ — alias cho nhập văn bản thủ công."""
        return self.get_article_from_text(raw_text, title="Bài đăng mạng xã hội", author_metadata=author_metadata)

# Script Test nếu file được chạy độc lập
if __name__ == "__main__":
    crawler = DataCrawler()
    # Ví dụ một URL tin tức VN
    test_url = "https://vnexpress.net/the-gioi"
    print(f"Thử nghiệm quét dữ liệu: {test_url}")
    result = crawler.crawl_news_article(test_url)
    
    if result["status"] == "success":
        print(f"Domain: {result['source_domain']}")
        print(f"Title: {result['title']}")
        print(f"Content length: {len(result['content'])} kí tự")
    else:
        print(f"Lỗi: {result['message']}")
