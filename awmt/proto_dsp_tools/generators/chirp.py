import numpy as np
from generator_base import GeneratorBase

class ChirpGenerator(GeneratorBase):
    def __init__(self, start_freq_hz: float, end_freq_hz: float):
        self.start_freq_hz = start_freq_hz
        self.end_freq_hz = end_freq_hz

    def generate(self, duration_ms: float, sample_rate_hz: int) -> list:
        t = np.linspace(0, duration_ms, int(sample_rate_hz * duration_ms))
        freqs = np.linspace(self.start_freq, self.end_freq, len(t))
        signal = np.sin(2 * np.pi * freqs * t)
        return signal.tolist()