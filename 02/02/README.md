# Desktop Assistant

A personal desktop voice assistant built with Python for simple automation tasks on a computer.

This project is designed to be lightweight, easy to understand, and easy to expand for your own ideas.

## Features

- Voice command recognition
- Web browsing shortcuts
- Search engine support
- Wikipedia search
- Text-to-speech responses
- Music playback support
- Basic desktop GUI

## Project Structure

```text
DesktopAssistant/
├── README.md
├── .gitignore
├── config.ini
├── requirements.txt
├── src/
│   ├── actions.py
│   ├── commands.py
│   ├── gui.py
│   ├── Jarvis2.py
│   └── Jarvis2_4windows.py
└── .vscode/
```

## Prerequisites

- Python 3.9+
- Microphone access
- Internet connection for web and Wikipedia searches

## Installation

Clone the project:

```bash
git clone https://github.com/anup26x11x2006/DesktopAssistant.git
cd DesktopAssistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Update the values in `config.ini`:

```ini
[DEFAULT]
master = YourName
search_engine = Google
debug = False
musicpath =
voice = Male
rate = 150
volume = 100
energy_threshold = 300
```

## Run

### Windows

```bash
python src/Jarvis2_4windows.py
```

### Linux / Ubuntu

```bash
python src/Jarvis2.py
```

## Example Commands

- Hello
- What’s up
- Open Google
- Search for Python tutorials
- Search Wikipedia for machine learning
- Play music
- Stop music
- Bye

## How It Works

1. The app listens to your microphone.
2. The speech recognition library converts the voice into text.
3. The assistant matches the text with known commands.
4. It performs the action such as opening a website or speaking a response.
5. It responds with voice output using text-to-speech.

This keeps the project simple and easy to extend with new features later.

## Notes

This is a personal project created for learning and experimentation with Python, desktop automation, and voice interfaces.

## GitHub

- Profile: https://github.com/anup26x11x2006
- Repository: https://github.com/anup26x11x2006/DesktopAssistant

