****Real-Time Speech-to-Text with Wake & Sleep Words (Offline Whisper)****
** Project Overview
      
     This project implements a real-time speech-to-text (STT) system that listens for a wake word to start transcription and a sleep word to stop it — just like a mini voice assistant.
     It uses OpenAI’s Whisper model locally (offline) to perform speech recognition and transcription, making it suitable for both desktop and mobile app integration (e.g., React Native).

**Features

  Wake/Sleep Word Control — activates/deactivates the transcription mode automatically
  Real-Time Speech Recognition using speech_recognition and pyaudio
  Offline Whisper Transcription (no API key required)
  App-Friendly Module Design — can be reused in a mobile or web app backend
  Lightweight & Secure — runs locally, no data sent to cloud
  Cross-Platform Support — works on Windows, macOS, and Linux

** Project Structure
SpeechToText
│
├── speech_module.py       
├── app.py                 
├── requirements.txt       
├── .env                   
└── README.md             

**Requirements
   Python 3.10+
   FFmpeg (for audio processing)
   Microphone input available

** Python Libraries
openai-whisper	                Local speech-to-text transcription
torch, torchaudio, torchvision	Machine learning backend
speechrecognition, pyaudio	Microphone input & speech capture
python-dotenv	                Environment variable management

## How to Clone & Run

Clone the repository:
    git clone https://github.com/vishnuofficial004-ui/SpeechToText.git
    cd SpeechToText
Install dependencies:
    pip install -r requirements.txt
Make virtual Environment
    python -m venv venv
    venv\Scripts\activate
Install and Verify ffmpeg
    ffmpeg -version
Run the project:
    python src\speech_module.py
Run the apiServer(optional)
    python src/api_server.py

**How It Works
   The system continuously listens through your microphone but stays inactive until it detects the wake word.
    On hearing the wake word, it switches into transcription mode and starts capturing speech.
    The captured audio is processed locally using Whisper, and the recognized text is displayed in the terminal or returned by the module.
    If the system detects the sleep word (e.g., “bye bye”), it pauses transcription and returns to idle listening.
    Run the demo: python app.py
    Microphone ready. Say your wake word to start.
    You said: hi hi
    Listening... (speech-to-text active)
    Transcription: Hello, how are you?
    You said: bye bye
    Sleeping mode activated.

 Key File — speech_module.py
**Responsibilities:
Function	Description
listen_for_wake_word()	Waits for user’s wake word
start_transcription()	Records and transcribes audio
stop_transcription()	Pauses listening when sleep word is said
load_model()	Loads Whisper model for offline inference
handle_errors()	Handles microphone/FFmpeg-related issues

This file can be imported as a Python module or used standalone for demonstration.

**Technical Workflow
    A[Microphone Input] --> B[SpeechRecognition Stream]
    B --> C{Wake Word?}
    C -- No --> B
    C -- Yes --> D[Activate STT Mode]
    D --> E[Record Audio]
    E --> F[Whisper Transcription (Offline)]
    F --> G[Display / Return Text Output]
    G --> H{Sleep Word?}
    H -- No --> D
    H -- Yes --> I[Stop & Go Idle]

**App-Friendliness

  The module is app-friendly because:
  The transcription logic is isolated in a single Python module.
  Can be wrapped in a Flask or FastAPI endpoint for mobile integration.
  Works offline (no dependency on OpenAI API).
  Easily portable to React Native or Electron-based frontends.

**Example Use Cases

   Voice note-taking or dictation tools
   AI voice assistants (custom wake/sleep trigger)
   Mobile apps requiring voice input (offline)
   Accessibility tools for hearing-impaired users
   Real-time meeting or lecture transcription

**Implementation Summary

1️  Set up Python environment and install libraries
2️  Configured microphone input using speech_recognition
3️  Added wake word detection logic
4️  Integrated Whisper model for local transcription
5️  Enabled sleep word to deactivate listening
6️  Verified real-time transcription in terminal
7  Removed dependency on .env once local mode worked


**Author
  Vishnu M
  GitHub: vishnuofficial004-ui

