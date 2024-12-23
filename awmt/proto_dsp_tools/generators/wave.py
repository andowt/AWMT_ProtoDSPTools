import numpy as np
from generator_base import GeneratorBase
from enum import Enum

class WaveType(Enum):
    sine = 0
    triangle = 1
    square = 2

class Wave():
    def __init__(self, wave_type: WaveType, frequency_hz: float, amplitude_normal: float, phase_deg: float=0.0):
        self.frequency_hz = frequency_hz
        self.amplitude_normal = amplitude_normal
        self.phase_deg = phase_deg
        self.phase_rad = (phase_deg * np.pi) / 360
        self.wave_type = wave_type

class WaveGenerator(GeneratorBase):
    def __init__(self, wave_list: list[Wave]):
        self.wave_list = wave_list
        
    def generate(self, duration_ms: float, sample_rate_hz: int) -> list:
        t = np.linspace(0, duration_ms, int(sample_rate_hz * duration_ms))
        freqs = np.linspace(self.start_freq, self.end_freq, len(t))
        signal = np.sin(2 * np.pi * freqs * t)
        return signal.tolist()