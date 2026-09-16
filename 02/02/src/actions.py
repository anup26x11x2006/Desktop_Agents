import configparser
import datetime
import os
import re
import subprocess
import sys
import webbrowser
from pathlib import Path
from urllib.parse import quote_plus

import pyttsx3
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_CANDIDATES = [
    Path.cwd() / "config.ini",
    PROJECT_ROOT / "config.ini",
    PROJECT_ROOT / "Requirements&COC" / "config.ini",
]

DEFAULT_CONFIG_CONTENT = """[DEFAULT]
master = YourName
search_engine = Google
debug = False
musicpath =
voice = Male
rate = 150
volume = 100
energy_threshold = 300

[EMAIL]
server = smtp.gmail.com
port = 587
username =
password =
"""


def ensure_default_config(config_path=None):
    target = Path(config_path) if config_path is not None else get_config_path()
    if target.exists():
        return target

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(DEFAULT_CONFIG_CONTENT, encoding="utf-8")
    return target


def get_config_path():
    for config_path in CONFIG_CANDIDATES:
        if config_path.exists():
            return config_path
    return PROJECT_ROOT / "config.ini"


def load_config():
    config_path = ensure_default_config(get_config_path())
    config = configparser.ConfigParser()
    config.read(config_path, encoding="utf-8")
    return config


def save_config(config):
    config_path = get_config_path()
    with open(config_path, "w", encoding="utf-8") as config_file:
        config.write(config_file)


def normalize_query(query):
    if query is None:
        return ""
    normalized = str(query).lower().replace("’", "'")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9\s']", " ", normalized)
    return " ".join(normalized.split())


def extract_search_query(query):
    normalized = normalize_query(query)
    if not normalized:
        return ""

    for keyword in ("search for", "search", "look for"):
        if keyword in normalized:
            remainder = normalized.split(keyword, 1)[1].strip()
            if remainder.startswith("for "):
                remainder = remainder[4:]
            return remainder.strip()

    return ""


def extract_command_target(query):
    normalized = normalize_query(query)
    if not normalized:
        return ""

    for prefix in ("open ", "launch ", "goto "):
        if normalized.startswith(prefix):
            return normalized[len(prefix):].strip()

    if normalized.startswith("search for "):
        return ""

    return ""


config = load_config()
engine = pyttsx3.init()
voices = engine.getProperty("voices") or []

def set_voice_from_config():
    selected_voice = config.get("DEFAULT", "voice", fallback="Male").strip().lower()
    if selected_voice == "male" and voices:
        engine.setProperty("voice", voices[0].id)
    elif voices:
        engine.setProperty("voice", voices[-1].id)

    try:
        engine.setProperty("rate", int(config.get("DEFAULT", "rate", fallback="150")))
        engine.setProperty("volume", max(0.0, min(1.0, int(config.get("DEFAULT", "volume", fallback="100")) / 100)))
    except ValueError:
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 1.0)


set_voice_from_config()


def search_engine_selector(config_obj):
    search_engine = config_obj.get("DEFAULT", "search_engine", fallback="Google").strip()
    normalized = search_engine.lower()
    mappings = {
        "google": "https://www.google.com",
        "bing": "https://www.bing.com",
        "duckduckgo": "https://www.duckduckgo.com",
        "youtube": "https://www.youtube.com",
    }

    if normalized in mappings:
        return mappings[normalized]

    candidate = f"https://{search_engine.lower()}.com"
    try:
        response = requests.get(candidate, timeout=5)
        if response.status_code == 200:
            return candidate
    except requests.RequestException:
        pass
    return "https://www.google.com"


def open_url(url):
    if not url:
        return

    try:
        webbrowser.open(url, new=2)
    except Exception:
        pass

    try:
        if sys.platform.startswith("win"):
            os.startfile(url)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", url])
        else:
            subprocess.Popen(["xdg-open", url])
    except Exception:
        pass


def search(search_query, search_engine):
    query = quote_plus(search_query.strip())
    if search_engine.startswith("http"):
        base_url = search_engine.rstrip("/")
    else:
        base_url = search_engine_selector({"DEFAULT": {"search_engine": search_engine}})
    open_url(f"{base_url}/search?q={query}")


def gui_speak(text):
    return None


def set_gui_speak(command):
    global gui_speak
    gui_speak = command


def speak(text):
    if callable(gui_speak):
        gui_speak(text)

    if engine is not None:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass


def wish_me(master):
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak(f"Good Morning {master}")
    elif hour < 18:
        speak(f"Good Afternoon {master}")
    else:
        speak(f"Good Evening {master}")


def change_rate(query, take_command):
    try:
        rate = int(query.split("to")[-1].strip())
        engine.setProperty("rate", rate)
        speak("Do you want to keep this config?")
        if take_command().lower() == "yes":
            config["DEFAULT"]["rate"] = str(rate)
            save_config(config)
        else:
            pass
    except (ValueError, IndexError):
        speak("Invalid value. Please try again.")


def change_voice(query, take_command):
    try:
        voice = query.split("to")[-1].strip().lower()
        if voice == "male":
            if voices:
                engine.setProperty("voice", voices[0].id)
            speak("Do you want to keep this config?")
            if take_command().lower() == "yes":
                config["DEFAULT"]["voice"] = "Male"
                save_config(config)
        elif voice == "female":
            if len(voices) > 1:
                engine.setProperty("voice", voices[1].id)
            speak("Do you want to keep this config?")
            if take_command().lower() == "yes":
                config["DEFAULT"]["voice"] = "Female"
                save_config(config)
        else:
            speak("Invalid value. Please try again.")
    except Exception:
        speak("Invalid value. Please try again.")


def change_volume(query, take_command):
    try:
        volume = int(query.split("to")[-1].strip())
        engine.setProperty("volume", max(0.0, min(1.0, volume / 100)))
        speak("Do you want to keep this config?")
        if take_command().lower() == "yes":
            config["DEFAULT"]["volume"] = str(volume)
            save_config(config)
    except (ValueError, IndexError):
        speak("Invalid value. Please try again.")
