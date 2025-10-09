# Real-Time Speech-to-Text with Wake and Sleep Words (Offline Whisper)

## Project Overview
This project implements a real-time Speech-to-Text (STT) system that continuously listens through a microphone and activates transcription only when a **wake word** is spoken. It stops listening when a **sleep word** is detected. The system works like a mini voice assistant and runs fully **offline** using **OpenAI Whisper local model**.

It is designed to run on **Windows (tested), macOS, and Linux** and can also be integrated into **mobile or web backends** such as React Native, FastAPI, or Flask.

---

## Features
- Automatic **Wake and Sleep word control**
- **Real-time speech recognition**
- **Offline Whisper transcription** (no OpenAI API key required)
- **Modular Python design** for application integration
- **Privacy-friendly** (runs entirely on local machine)
- **Cross-platform support**

---

## Project Structure
SpeechToText
│
├── src/
│ ├── speech_module.py # Core wake/sleep logic and transcription
│ ├── api_server.py # Optional FastAPI server for API access
│
├── app.py # Demo runner script
├── test_speech_module.py # Unit tests (optional)
├── requirements.txt # Dependencies
├── .env # Optional config file
└── README.md

## Requirements
- Python 3.10 or higher
- FFmpeg installed
- Working microphone
  
## Python Libraries Used
| Library | Purpose |
|---------|---------|
| openai-whisper | Local speech-to-text transcription |
| torch, torchaudio, torchvision | Backend for Whisper |
| speechrecognition | Microphone input handling |
| pyaudio | Audio streaming |
| python-dotenv | Environment variable support |

## How to Clone and Run

1. Clone repository
2. git clone https://github.com/vishnuofficial004-ui/SpeechToText.git
   cd SpeechToText
3. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate        # Windows
4. Install dependencies
   pip install -r requirements.txt
5. Install and verify FFmpeg
   ffmpeg -version
6. Run the demo
   python src/speech_module.py
7. Run FastAPI server
   python src/api_server.py
How It Works
   The system listens continuously in idle mode.
   When it hears the wake word, it activates transcription.
   Audio is processed locally by Whisper.
   Transcribed text is displayed in the terminal or returned as function output.
   When it hears the sleep word, it goes back to idle mode.

Example Console Output
Microphone ready. Say your wake word to start.
You said: hi hi
Listening...
Transcription: Hello, how are you?
You said: bye bye
Sleeping mode activated.
Key File: speech_module.py
Function	Description
listen_for_wake_word()	Listens for wake word activation
start_transcription()	Begins real-time transcription
stop_transcription()	Stops transcription on sleep word
load_model()	Loads Whisper locally
handle_errors()	Handles audio and mic errors

Technical Workflow

Microphone Input
        ↓
SpeechRecognition Audio Stream
        ↓
Wake Word Detected?
    No → Keep Listening
    Yes → Start STT Mode
                ↓
       Whisper Transcription
                ↓
      Display or Return Text
                ↓
Sleep Word Detected?
    Yes → Go Idle
    No  → Continue STT

Example Use Cases
  Voice note-taking
  AI voice assistant
  Hands-free voice command system
  Meeting transcription
  Accessible voice input tools

## Video Demonstration

Watch the demo videos showing wake/sleep word functionality and real-time STT:

1. [Implementation Details Video 1(Implementation+Transcription)](https://drive.google.com/file/d/1st3vWXRlYpcyxWSfNMR4V3tLFKHddEXa/view?usp=sharing)
2. [Implementation Details Video 2(Fastapi Integration)](https://drive.google.com/file/d/16HAs6ef6cfeSVjNlFzdSKa7LQr1pSmkO/view?usp=sharing)


Author
Name: Vishnu M
GitHub: vishnuofficial004-ui
Platform Used: Windows 10

License
This project is released under the MIT License. See LICENSE file for details.

Future Enhancements

 Support multiple wake words
 Add text-to-speech feedback
 Integration with mobile apps for offline voice commands
 GPU acceleration for faster transcription

