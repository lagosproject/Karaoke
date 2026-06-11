"""
Run this script once to generate the demo WAV audio files.
  python create_demo_audio.py
"""
import numpy as np
import soundfile as sf
import os

SAMPLE_RATE = 44100
DURATION = 32  # seconds — covers all lyrics timestamps
CHANNELS = 2

out_dir = os.path.join(os.path.dirname(__file__), 'songs')

def tone(freq, duration, sample_rate=SAMPLE_RATE, amplitude=0.3):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return np.column_stack([wave, wave]).astype(np.float32)

# Song track: melody (440 Hz A4)
song_audio = tone(440, DURATION)
sf.write(os.path.join(out_dir, 'demo_song.wav'), song_audio, SAMPLE_RATE)
print('Created demo_song.wav')

# Karaoke track: same tone slightly lower (330 Hz E4) to simulate instrumental
karaoke_audio = tone(330, DURATION, amplitude=0.2)
sf.write(os.path.join(out_dir, 'demo_karaoke.wav'), karaoke_audio, SAMPLE_RATE)
print('Created demo_karaoke.wav')

print('\nDone. Set DATA_PATH=./songs in your .env and run the app.')
