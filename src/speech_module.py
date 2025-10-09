import os
import logging
import speech_recognition as sr
import tempfile
import whisper

# ------------------- Configure Logging -------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ------------------- Speech Module Class -------------------
class SpeechModule:
    """
    Speech-to-Text module with wake/sleep word detection.
    Uses local OpenAI Whisper for transcription (offline).
    """
    def __init__(self, wake_word="hi", sleep_word="bye"):
        # Set wake/sleep words
        self.wake_word = wake_word.lower()
        self.sleep_word = sleep_word.lower()

        # Initialize recognizer and microphone
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        logging.info("🎤 Microphone ready. Say your wake word to start.")

        self.active = False  # transcription state

        # Load local Whisper model
        logging.info("🧠 Loading Whisper model (this may take a few seconds)...")
        self.model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
        logging.info("✅ Whisper model loaded successfully.")

    # ------------------- Keyword Detection -------------------
    def listen_for_keywords(self):
        """Listen for wake/sleep words and return the state."""
        with self.mic as source:
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio).lower()
            logging.info(f"🗣 You said: {text}")

            if self.wake_word in text:
                logging.info("✅ Wake word detected!")
                return "wake"
            elif self.sleep_word in text:
                logging.info("🛑 Sleep word detected!")
                return "sleep"
            else:
                return None

        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            logging.error(f"❌ Google STT error: {e}")
            return None

    # ------------------- Real-Time Transcription -------------------
    def transcribe_audio(self):
        """Capture audio from mic and transcribe using local Whisper."""
        with self.mic as source:
            logging.info("🎧 Listening for transcription...")
            audio = self.recognizer.listen(source, phrase_time_limit=5)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio.get_wav_data())
            tmp_path = tmp.name

        try:
            result = self.model.transcribe(tmp_path)
            logging.info(f"💬 Transcription: {result['text']}")
        except Exception as e:
            logging.error(f"❌ Whisper local error: {e}")

    # ------------------- Main Loop -------------------
    def run(self):
        """Run the module continuously with wake/sleep toggle."""
        logging.info("🚀 Speech module started. Waiting for wake word...")

        while True:
            keyword = self.listen_for_keywords()

            if not self.active and keyword == "wake":
                self.active = True
                logging.info("🚀 Wake word detected → Transcription ON")

            elif self.active and keyword == "sleep":
                self.active = False
                logging.info("💤 Sleep word detected → Transcription OFF")

            elif self.active:
                self.transcribe_audio()

# ------------------- Example Usage -------------------
if __name__ == "__main__":
    module = SpeechModule()
    module.run()

