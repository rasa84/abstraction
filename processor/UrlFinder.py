import re

from processor.TextProcessor import TextProcessor


class UrlFinder(TextProcessor):
    def find_pattern(self, text):
        pattern = r'https?://(?:www\.)?\S+\.\S+'
        return re.findall(pattern, text)