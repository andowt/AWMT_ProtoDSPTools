from abc import ABC, abstractmethod

class GeneratorBase(ABC):
    @abstractmethod
    def generate(self, duration_ms: float, sample_rate_hz: int) -> list:
        """Generate a signal."""
        pass
