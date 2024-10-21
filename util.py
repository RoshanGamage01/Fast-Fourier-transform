import wave
import numpy as np

def save_as_audio_file(idft_values, sample_rate, file_name):
    audio = wave.open(file_name, 'w')
    audio.setnchannels(1)
    audio.setsampwidth(2)
    audio.setframerate(sample_rate)

    audio_data = np.clip(idft_values, -32768, 32767).astype(np.int16)
    audio_data = np.array(audio_data, dtype=np.int16)
    
    audio.writeframes(audio_data.tobytes())
    audio.close()