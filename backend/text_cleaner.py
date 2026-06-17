import re

from pyvi import ViTokenizer

from backend.text_utils import preprocess_text, remove_html, remove_urls, normalize_whitespace

class TextCleaner:
    """
    Quy trình Tiền Xử Lý tiêu chuẩn cho hệ thống NLP Tiếng Việt.
    1. Xóa HTML, URL, Icon
    2. Chuyển hóa ngôn ngữ mạng (Teencode)
    3. Tách từ bằng PyVi
    """
    def __init__(self):
        # Bộ từ điển TEENCODE tiếng Việt cơ bản (Do giới trẻ hay chế từ)
        self.teencode_dict = {
            'j': 'gì', 'wa': 'quá', 'wá': 'quá', 'ko': 'không', 
            'k': 'không', 'khong': 'không', 'dc': 'được', 'đk': 'được',
            'đc': 'được', 'ng': 'người', 'cx': 'cũng', 'hj': 'hì',
            'vs': 'với', 'zậy': 'vậy', 'zay': 'vậy', 'ms': 'mới',
            'thik': 'thích', 'thuog': 'thương', 'ak': 'à', 'ah': 'à',
            'ui': 'ơi', 'tg': 'thời gian', 'r': 'rồi', 'rồi': 'rồi'
        }
        
    def remove_html_and_urls(self, text):
        text = remove_html(text)
        text = remove_urls(text)
        return text

    def remove_special_characters_and_emojis(self, text):
        """ Chỉ giữ lại chữ cái, số tiếng Việt và các dấu câu cơ bản. Xóa Emoji. """
        # Xóa emojis/icon - giữ chữ cái, số, các dấu câu ,.!? và _
        # Patern này match chữ Việt Nam (bao gồm các dấu thanh)
        vietnamese_chars = r"a-zA-Z0-9ÀÁÂÃÈÉÊẾÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêếìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỮỰỲỴÝỶỸửữựỳỵỷỹ\s\.,!\?"
        text = re.sub(f'[^{vietnamese_chars}]', ' ', text)
        
        # Biến đống khoảng trắng dư thừa thành 1 khoảng trắng duy nhất
        return normalize_whitespace(text)

    def normalize_teencode(self, text):
        """ Thay thế chữ teencode về chuẩn thuần Việt """
        words = text.split()
        normalized_words = []
        for word in words:
            # Xử lý lowercase để tìm trong dictionary
            lower_word = word.lower()
            # Bỏ mảng dấu câu ra ngoài để đối soát chữ cho chuẩn
            clean_word = re.sub(r'[^\w\s]', '', lower_word)
            
            if clean_word in self.teencode_dict:
                # Nếu từ sau khi lột dấu câu nằm trong từ điển, thay thế!
                new_word = self.teencode_dict[clean_word]
                # Thêm lại dấu câu nếu có (rất thô sơ, nhưng hiệu quả)
                if word[-1] in ['.', ',', '!', '?']:
                    new_word += word[-1]
                normalized_words.append(new_word)
            else:
                normalized_words.append(word)
                
        return " ".join(normalized_words)

    def pyvi_segmentation(self, text):
        """ Tách từ bằng PyVi (Tạo các dấu gạch dưới _, vd: người_dùng) """
        return ViTokenizer.tokenize(text)

    def pipeline_clean(self, text):
        """Cùng pipeline với train/embed — gọi `preprocess_text` trong text_utils."""
        return preprocess_text(text)

# Script Test
if __name__ == "__main__":
    cleaner = TextCleaner()
    test_text = "Hôm nay tôi thấy bài báo đó viết sai sự thật wa j luôn á mọi ng ơi!!! Vào web xem nè http://fake.vn <br> Quá bức xúc!"
    print(f"Original Text: {test_text}")
    print(f"Cleaned Text: {cleaner.pipeline_clean(test_text)}")
