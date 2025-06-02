from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text)
    filepath = f"Assets/Audio/{filename}"
    tts.save(filepath)
    return filepath
