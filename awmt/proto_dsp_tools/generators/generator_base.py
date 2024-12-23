from abc import ABC, abstractmethod

class GeneratorBase(ABC):
    @abstractmethod
    def generate(self, duration: float, sample_rate: int) -> list:
        """Generate a signal."""
        pass
