from abc import ABC, abstractmethod

class AnalyzerBase(ABC):
    @abstractmethod
    def analyze(self, signal: list, sample_rate: int, plot: bool) -> dict:
        """Analyze a signal."""
        pass
