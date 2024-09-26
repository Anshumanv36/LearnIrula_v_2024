from pydub import AudioSegment
import os

# Directory for downloaded audio files
audio_dir = 'data/downloaded_audio/'
# Directory for the converted files
wav_dir = 'data/converted_audio/'
os.makedirs(wav_dir, exist_ok=True)

# Convert each .mp3 file to .wav
for mp3_file in os.listdir(audio_dir):
    if mp3_file.endswith('.mp3'):
        mp3_file_path = os.path.join(audio_dir, mp3_file)
        wav_file_path = os.path.join(wav_dir, f"{os.path.splitext(mp3_file)[0]}.wav")
        
        # Load and export as .wav
        audio = AudioSegment.from_mp3(mp3_file_path)
        audio.export(wav_file_path, format='wav')
        print(f"Converted: {mp3_file} to {wav_file_path}")
