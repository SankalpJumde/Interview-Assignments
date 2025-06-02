from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text)
    filepath = f"assets/audio/{filename}"
    tts.save(filepath)
    return filepath
