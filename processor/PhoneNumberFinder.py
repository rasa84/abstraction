import re

from processor.TextProcessor import TextProcessor


class PhoneNumberFinder(TextProcessor):
    def find_pattern(self, text):
        pattern = r'\+370\(\d{3}\)\d{5}'
        return re.findall(pattern, text)