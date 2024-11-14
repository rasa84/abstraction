import re

from processor.TextProcessor import TextProcessor


class EmailFinder(TextProcessor):
    def find_pattern(self, text):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(pattern, text)