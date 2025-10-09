# test_speech_module.py

import speech_recognition as sr
from pathlib import Path

# --- Paths ---
AUDIO_FILE = Path("Hi_test.wav")  # or bye_test.wav

# --- Initialize recognizer ---
r = sr.Recognizer()

def test_audio_file(path: Path):
    """Test STT on a given audio file."""
    if not path.exists():
        print(f"❌ File not found: {path}")
        return

    with sr.AudioFile(str(path)) as source:
        print(f"🎧 Loading audio file: {path.name}")
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print(f"✅ Recognized text: '{text}'")
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌ API request error: {e}")

if __name__ == "__main__":
    test_audio_file(AUDIO_FILE)
