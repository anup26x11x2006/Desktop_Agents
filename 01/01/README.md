# Jarvis Desktop Voice Assistant

A personal desktop voice assistant built with Python for simple hands-free tasks on a Windows machine.

## Features

- Voice command recognition
- Time and date announcements
- Open Google and YouTube
- Search Wikipedia
- Play music from the local Music folder
- Take screenshots
- Tell jokes
- Change assistant name
- Shutdown or restart the computer

## How it works

The program listens to microphone input with `SpeechRecognition`, converts the spoken words into text, checks for matching command keywords, and then performs the required task using Python libraries such as `pyttsx3`, `webbrowser`, `wikipedia`, `pyautogui`, and `pyjokes`.

## Requirements

- Python 3.9+
- Windows
- Microphone
- Speakers

## Setup

1. Open a terminal in the project folder.
2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate it:

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the app:

```bash
python Jarvis/jarvis.py
```

## Example commands

- "what time is it"
- "what is the date"
- "open google"
- "open youtube"
- "search wikipedia for python"
- "tell me a joke"
- "take a screenshot"
- "play music"
- "change your name"
- "shutdown"
- "restart"
- "exit"

## Project structure

```text
Jarvis-Desktop-Voice-Assistant/
├── Jarvis/
│   └── jarvis.py
├── README.md
├── requirements.txt
├── .gitignore
└── assistant_name.txt   # created at runtime if the assistant name is changed
```

## Author

Anup

- GitHub: https://github.com/anup26x11x2006

## License

This project is for personal use and learning purposes.

