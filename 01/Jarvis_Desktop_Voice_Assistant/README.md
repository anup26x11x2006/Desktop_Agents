# Jarvis Desktop Voice Assistant

> A Python-powered desktop voice assistant for Windows that converts natural voice commands into practical desktop actions.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge\&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge\&logo=windows)
![Status](https://img.shields.io/badge/Status-Experimental-orange?style=for-the-badge)

---

## Overview

**Jarvis Desktop Voice Assistant** is a Python-based voice-controlled desktop assistant designed to perform common computer tasks through spoken commands.

The assistant listens through a microphone, converts speech into text, identifies the requested command, executes the corresponding desktop or web action, and provides voice feedback.

The project focuses on learning and implementing the fundamentals of:

* Speech recognition
* Text-to-speech interaction
* Desktop automation
* Command processing
* Web automation
* Python-based system control

---

## Features

### Voice Interaction

* Voice command recognition
* Text-to-speech responses
* Hands-free interaction
* Customizable assistant name

### Web & Information

* Open Google
* Open YouTube
* Search Wikipedia
* Perform information searches

### Desktop Automation

* Take screenshots
* Play music from the local Music folder
* Shutdown the computer
* Restart the computer

### Entertainment

* Tell jokes
* Voice-based responses

### Exit Control

The assistant can be terminated through a voice command.

---

## How It Works

The application follows a simple voice-command pipeline:

```text
┌──────────────────┐
│   User Speaks    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ SpeechRecognition│
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Convert Speech   │
│    to Text       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Command Matching │
└────────┬─────────┘
         │
         ▼
┌────────────────────────┐
│ Execute Requested Task │
└────────┬───────────────┘
         │
         ▼
┌──────────────────┐
│  Voice Response  │
└──────────────────┘
```

The assistant uses Python libraries to connect speech input with actions such as opening websites, searching Wikipedia, controlling the system, taking screenshots, and playing music.

---

## Technology Stack

| Technology            | Purpose                            |
| --------------------- | ---------------------------------- |
| **Python**            | Core application                   |
| **SpeechRecognition** | Voice input and speech-to-text     |
| **pyttsx3**           | Text-to-speech                     |
| **webbrowser**        | Opening websites                   |
| **Wikipedia**         | Information search                 |
| **PyAutoGUI**         | Screenshot and desktop interaction |
| **PyJokes**           | Joke functionality                 |

---

## Requirements

Before running the project, make sure you have:

* Python **3.9 or newer**
* Windows
* Working microphone
* Speakers/headphones
* Internet connection for web/Wikipedia features

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anup26x11x2006/Desktop_Agents.git
```

### 2. Navigate to the project

```bash
cd Desktop_Agents/01/01
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows CMD:**

```cmd
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Assistant

Start the application with:

```bash
python Jarvis/jarvis.py
```

Once started, speak a supported command into your microphone.

---

## Example Commands

Try commands such as:

```text
"What time is it?"
"What is the date?"
"Open Google"
"Open YouTube"
"Search Wikipedia for Python"
"Tell me a joke"
"Take a screenshot"
"Play music"
"Change your name"
"Shutdown"
"Restart"
"Exit"
```

---

## Project Structure

```text
01/
└── 01/
    ├── Jarvis/
    │   └── jarvis.py
    │
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    └── assistant_name.txt
```

`assistant_name.txt` is created at runtime when the assistant name is changed.

---

## Learning Objectives

This project was developed to explore practical Python concepts including:

* Speech recognition
* Voice interfaces
* Python automation
* Command-based application architecture
* External library integration
* Browser automation
* Desktop interaction
* System-level commands
* Text-to-speech systems

---

## Future Improvements

Possible future enhancements include:

* [ ] Natural-language command understanding
* [ ] LLM integration
* [ ] Context-aware conversations
* [ ] More desktop applications
* [ ] Application launching and control
* [ ] Better error handling
* [ ] Command confirmation for sensitive actions
* [ ] Configurable command system
* [ ] GUI dashboard
* [ ] Plugin-based architecture
* [ ] AI-powered task planning

---

## Safety

Some commands can perform system-level operations such as shutdown and restart.

Always review the commands and permissions available to the assistant before running it on a machine containing important or unsaved work.

---

## Author

### Anoop Patidar

**Software Engineer • AI & Data Science Enthusiast • Full-Stack Developer**

* GitHub: https://github.com/anup26x11x2006
* LinkedIn: https://www.linkedin.com/in/anoop-patidar-93a50a330/
* LeetCode: https://leetcode.com/u/anup26x11x2006/

---

## License

This project is intended for personal learning, experimentation, and educational purposes.
