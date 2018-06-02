from abc import ABC, abstractmethod

class DataFetcher(ABC):
    @abstractmethod
    def fetch(self, path):
        pass
