from abc import ABC, abstractmethod

class DataParser(ABC):
    @abstractmethod
    def parse(self, data):
        pass

    @abstractmethod
    def fields(self):
        pass
