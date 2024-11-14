from abc import ABC, abstractmethod


class TextProcessor(ABC):
    @abstractmethod
    def find_pattern(self, text):
        pass
