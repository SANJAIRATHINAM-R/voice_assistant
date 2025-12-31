# voice_assistant
Windows Voice Assistant (Offline, Tray-Based)

A lightweight Windows voice assistant inspired by Siri, designed to run silently in the background as a system tray application.
It listens continuously for a custom wake word and executes predefined system commands using offline speech recognition.

This project is intended for personal desktop automation and does not require internet access for speech recognition.

Key Characteristics

Windows-only

Background service (tray icon)

Offline speech recognition (Vosk)

Custom wake word: “Hey Darling”

JSON-based command configuration

No cloud APIs required

Modular, readable Python architecture

Functional Capabilities
Wake Word

Always listens for:

Hey Darling


After detection, switches into command-listening mode

Supported Commands

Application launch:

Chrome

Notepad

Calculator

System controls:

Wi-Fi on / off

Bluetooth on / off

Keyboard backlight

Volume up / down / mute

Brightness up / down

System shutdown

Open ChatGPT in browser

Fully customizable via JSON

Project Architecture
voice_assistant/
│
├─ assistant/
│  ├─ main.py            # Program entry point
│  ├─ wake_listener.py   # Wake word detection loop
│  ├─ listener.py        # Speech recognition logic
│  ├─ commands.py        # Command execution engine
│  ├─ tts.py             # Text-to-speech (optional)
│  ├─ tray.py            # System tray integration
│  ├─ commands.json      # User-defined commands
│
├─ models/
│  └─ vosk-model-small-en-us-0.15/   # Offline STT model (not pushed to GitHub)
│
├─ requirements.txt
└─ run.bat

Technology Stack
Component	Purpose
Python	Core language
Vosk	Offline speech recognition
sounddevice	Microphone input
pystray	System tray icon
pyttsx3	Offline text-to-speech
JSON	Command definitions
System Requirements

Windows 10 or Windows 11

Python 3.9 or newer

Working microphone

Administrator privileges (recommended for system commands)

Installation Guide
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/voice-assistant.git
cd voice-assistant

2. Install Python Dependencies
pip install -r requirements.txt

3. Download Offline Speech Model

Download Vosk model:

vosk-model-small-en-us-0.15


Extract to:

voice_assistant/models/vosk-model-small-en-us-0.15


⚠️ This folder is intentionally excluded from GitHub due to size.

Running the Assistant
Manual (Debug / First Run)
python assistant/main.py


Expected behavior:

Console shows listening status

Tray icon appears

Microphone activates

Say “Hey Darling”

Run Automatically in Background (Startup)

Edit run.bat:

@echo off
cd /d C:\voice_assistant
python assistant\main.py


Add to startup:

Press Win + R

Type:

shell:startup


Paste run.bat

The assistant now starts automatically with Windows.

Customizing Commands

Commands are defined in:

assistant/commands.json


Example:

{
  "open chrome": "chrome",
  "open notepad": "notepad",
  "volume up": "nircmd.exe changesysvolume 5000",
  "shutdown system": "shutdown /s /t 5"
}

Notes:

Keys = spoken phrases

Values = Windows commands

Changes take effect after restart

Troubleshooting
Assistant runs but does not respond

Check microphone permissions

Ensure correct Vosk model path

Set correct default input device

Speak clearly and naturally

JSON error on startup

Ensure commands.json is valid JSON

No empty file

No trailing commas

No tray icon

Check tray.py

Run manually to see errors

Known Limitations

Wake word accuracy depends on microphone quality

Offline models are less accurate than cloud services

Windows-only

Not intended for mobile use

Security & Privacy

No audio is sent to the internet

All processing is local

No data collection

No logging by default

License

MIT License
Free for personal and educational use.

Project Status

✔ Core functionality complete
✔ Stable offline operation
✔ Background execution supported
✔ GitHub-ready

If you want next, I can:

Validate your final code line-by-line

Fix wake-word accuracy issues

Convert this into a single .exe

Prepare a professional release tag
