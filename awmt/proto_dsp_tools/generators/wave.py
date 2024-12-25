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

        if frequency_hz < 0:
            raise ValueError(f"Negative frequency requested {frequency_hz}")
        if not 0 <= phase_deg <= 360:
            raise ValueError(f"Invalid phase requested: {phase_deg}")
        if not 0 <= amplitude_normal <= 1:
            raise ValueError(f"Invalid amplitude requested: {amplitude_normal}")

class WaveGenerator(GeneratorBase):
    def __init__(self, wave_list: list[Wave]):
        self.wave_list = wave_list

    def generate(self, duration_ms: float, sample_rate_hz: int) -> list:

        duration_s = duration_ms / 1000.0
        t = np.linspace(0, duration_s, int(sample_rate_hz * duration_s), endpoint=False)
        signal = np.zeros_like(t)
                # Generate and mix each wave
        for wave in self.wave_list:
            base_sine = np.sin(2 * np.pi * wave.frequency_hz * t + wave.phase_rad)
            if wave.wave_type == WaveType.sine:
                wave_signal = wave.amplitude_normal * base_sine
            elif wave.wave_type == WaveType.triangle:
                # arcsin is used to generate a triangle wave as it linearises the waveform
                # 0:1 is mapped to 0:pi/2
                # 1:0 is mapped to pi/2:0
                # -1:0 is mapped to -pi/2:0
                # 0:-1 is mapped to 0:-pi/2
                wave_signal = wave.amplitude_normal * (2 / np.pi) * np.arcsin(base_sine)
            elif wave.wave_type == WaveType.square:
                # np.sign used to generate square wave mapping positive values to 1 and negative to -1
                wave_signal = wave.amplitude_normal * np.sign(base_sine)
            else:
                raise ValueError(f"Unsupported wave type: {wave.wave_type}")
            
            signal += wave_signal

        return signal.tolist()