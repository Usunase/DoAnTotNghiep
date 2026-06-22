import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

class DataCrawler:
    """
    Hệ thống Crawler Đa Dụng (Scraping) thu thập dữ liệu báo điện tử từ URL.
    """
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

    def crawl_news_article(self, url):
        """
        Nhận vào 1 URL, dùng BeautifulSoup tải và bóc tách nội dung HTML.
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            h1_tag = soup.find('h1')
            title = h1_tag.get_text().strip() if h1_tag else soup.title.string.strip() if soup.title else ""
            
            paragraphs = soup.find_all('p')
            content = " ".join([p.get_text().strip() for p in paragraphs])
            
            parsed_uri = urlparse(url)
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            
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

    def get_article_from_text(self, raw_text, title=""):
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
        }

    def get_facebook_post(self, raw_text):
        """Giữ tương thích code cũ — alias cho nhập văn bản thủ công."""
        return self.get_article_from_text(raw_text, title="Bài đăng mạng xã hội")

if __name__ == "__main__":
    crawler = DataCrawler()
    test_url = "https://vnexpress.net/the-gioi"
    print(f"Thử nghiệm quét dữ liệu: {test_url}")
    result = crawler.crawl_news_article(test_url)
    
    if result["status"] == "success":
        print(f"Domain: {result['source_domain']}")
        print(f"Title: {result['title']}")
        print(f"Content length: {len(result['content'])} kí tự")
    else:
        print(f"Lỗi: {result['message']}")
