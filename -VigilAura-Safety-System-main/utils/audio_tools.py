# utils/audio_tools.py

import sounddevice as sd
import numpy as np

def detect_scream(threshold_db=45, duration=2, scream_energy_threshold=35):
    fs = 44100  # Sampling frequency
    print("🎙️ Listening for scream...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    energy = np.sum(recording ** 2) / len(recording)
    energy_db = 10 * np.log10(energy + 1e-6)

    print(f"Energy (dB): {energy_db:.2f}")

    if energy_db > threshold_db:
        print("🚨 Scream detected!")
    else:
        print("✅ No scream detected.")
