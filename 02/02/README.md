# Desktop Assistant

> A lightweight Python desktop voice assistant with voice commands, web automation, text-to-speech, music playback, and a basic graphical interface.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge\&logo=python)
![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux-Supported-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Experimental-orange?style=for-the-badge)

---

## Overview

**Desktop Assistant** is a Python-based voice assistant designed to provide a simple interface for interacting with a computer through spoken commands.

The project focuses on creating a lightweight and extensible architecture where voice input is converted into commands and mapped to actions such as opening websites, searching for information, playing music, and responding through text-to-speech.

Unlike a single-file implementation, this version separates important functionality into modules for commands, actions, GUI interaction, and platform-specific execution.

---

## Features

### Voice Interaction

* Voice command recognition
* Text-to-speech responses
* Hands-free interaction
* Configurable voice properties

### Web & Search

* Open Google
* Search the web
* Wikipedia search
* Browser shortcuts

### Media

* Play music
* Stop music
* Configurable music directory

### Desktop Interface

* Basic graphical user interface
* Command interaction
* Windows-specific execution support
* Linux/Ubuntu execution support

### Configuration

The assistant provides configurable settings through `config.ini`, including:

* Assistant/master name
* Search engine
* Debug mode
* Music path
* Voice selection
* Speech rate
* Speech volume
* Energy threshold

---

## Architecture

The project separates the assistant into multiple components:

```text
                    ┌─────────────────────┐
                    │    User Voice       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Speech Recognition │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Command Processing │
                    │     commands.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Action Handler    │
                    │      actions.py     │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
       ┌────────────┐   ┌─────────────┐  ┌────────────┐
       │ Web/Search │   │ Music/Media │  │ Desktop OS │
       └────────────┘   └─────────────┘  └────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Text-to-Speech /   │
                    │     GUI Response    │
                    └─────────────────────┘
```

This modular structure makes it easier to extend the assistant with additional commands and actions.

---

## Technology Stack

| Technology              | Purpose                 |
| ----------------------- | ----------------------- |
| **Python**              | Core application        |
| **Speech Recognition**  | Voice input             |
| **Text-to-Speech**      | Voice responses         |
| **Web Browser APIs**    | Browser interaction     |
| **Wikipedia**           | Information retrieval   |
| **GUI Framework**       | Basic desktop interface |
| **Configuration Files** | Runtime customization   |

---

## Project Structure

```text
02/
└── 02/
    ├── src/
    │   ├── actions.py
    │   ├── commands.py
    │   ├── gui.py
    │   ├── Jarvis2.py
    │   └── Jarvis2_4windows.py
    │
    ├── .vscode/
    ├── README.md
    ├── .gitignore
    ├── config.ini
    └── requirements.txt
```

The repository currently provides separate entry points for Windows and Linux/Ubuntu environments.

---

## Requirements

* Python **3.9+**
* Microphone access
* Internet connection for web and Wikipedia searches
* Speakers/headphones

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anup26x11x2006/Desktop_Agents.git
```

### 2. Navigate to the project

```bash
cd Desktop_Agents/02/02
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the assistant, configure `config.ini`.

Example:

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

These settings control the assistant's identity, search engine, debugging behavior, music directory, voice characteristics, speech rate, volume, and microphone energy threshold.

---

## Running the Assistant

### Windows

```bash
python src/Jarvis2_4windows.py
```

### Linux / Ubuntu

```bash
python src/Jarvis2.py
```

The project currently provides dedicated entry points for the two environments.

---

## Example Commands

Try commands such as:

```text
"Hello"
"What's up"
"Open Google"
"Search for Python tutorials"
"Search Wikipedia for machine learning"
"Play music"
"Stop music"
"Bye"
```

---

## How It Works

The assistant follows a straightforward command-processing pipeline:

### 1. Listen

The microphone captures the user's voice.

### 2. Recognize

Speech recognition converts the audio input into text.

### 3. Process

The command-processing layer determines what the user requested.

### 4. Execute

The appropriate action is executed, such as opening a website, searching Wikipedia, or controlling music playback.

### 5. Respond

The assistant provides a response through text-to-speech and/or the graphical interface.

This architecture keeps the implementation relatively simple while providing clear separation between command processing and action execution.

---

## Design Principles

The project emphasizes:

* **Modularity** — functionality is divided across multiple files.
* **Extensibility** — new commands and actions can be added.
* **Configurability** — behavior can be customized through `config.ini`.
* **Cross-platform execution** — separate Windows and Linux entry points are provided.
* **Simplicity** — the implementation remains approachable for learning and experimentation.

---

## Future Improvements

Potential improvements include:

* [ ] Natural-language command processing
* [ ] LLM integration
* [ ] Context-aware conversations
* [ ] More desktop automation commands
* [ ] Application launching
* [ ] Better command routing
* [ ] Plugin architecture
* [ ] Improved GUI
* [ ] Conversation history
* [ ] Persistent assistant memory
* [ ] Error recovery
* [ ] Command confirmation for sensitive actions
* [ ] Automated testing
* [ ] Logging and diagnostics

---

## Learning Objectives

This project provides practical experience with:

* Python application architecture
* Speech recognition
* Text-to-speech systems
* Desktop automation
* GUI development
* Configuration management
* Modular programming
* Cross-platform application design
* Web automation
* Command processing

---

## Safety

Desktop assistants can interact with operating-system resources and external services.

Do not grant an assistant more permissions than necessary, and review commands that can affect files, applications, or system state before executing them.

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
