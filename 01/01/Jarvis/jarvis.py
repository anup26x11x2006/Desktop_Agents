import datetime
import os
import random
import subprocess
import webbrowser
from pathlib import Path
from typing import Optional

import pyautogui
import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia

BASE_DIR = Path(__file__).resolve().parent.parent
NAME_FILE = BASE_DIR / "assistant_name.txt"

try:
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    if voices:
        preferred_voice = next(
            (voice for voice in voices if "female" in voice.name.lower() or "zira" in voice.name.lower()),
            voices[0],
        )
        engine.setProperty("voice", preferred_voice.id)
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1)
except Exception as exc:  # pragma: no cover
    engine = None
    print(f"TTS initialization failed: {exc}")


def speak(text: str) -> None:
    """Speak text using the installed TTS engine if available."""
    if not text:
        return

    if engine is None:
        print(text)
        return

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as exc:  # pragma: no cover
        print(f"Speech error: {exc}")
        print(text)


def get_time() -> None:
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("The current time is")
    speak(current_time)
    print(f"The current time is {current_time}")


def get_date() -> None:
    """Tell the current date."""
    now = datetime.datetime.now()
    formatted_date = f"{now.day} {now.strftime('%B')} {now.year}"
    speak("The current date is")
    speak(formatted_date)
    print(f"The current date is {formatted_date}")


def load_name() -> str:
    """Load the saved assistant name or fall back to Jarvis."""
    try:
        if NAME_FILE.exists():
            stored_name = NAME_FILE.read_text(encoding="utf-8").strip()
            if stored_name:
                return stored_name
    except OSError:
        pass
    return "Jarvis"


def wish_me() -> None:
    """Greeting for the user based on time of day."""
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 16:
        greeting = "Good afternoon!"
    elif 16 <= hour < 24:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"

    speak("Welcome back, sir!")
    speak(greeting)
    assistant_name = load_name()
    message = f"{assistant_name} at your service. Please tell me how may I assist you."
    speak(message)
    print(message)


def take_screenshot() -> None:
    """Save a screenshot in the Pictures folder."""
    try:
        image = pyautogui.screenshot()
    except Exception as exc:
        speak("I could not take a screenshot right now.")
        print(f"Screenshot error: {exc}")
        return

    picture_dir = Path.home() / "Pictures"
    picture_dir.mkdir(exist_ok=True)
    file_name = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = picture_dir / file_name
    image.save(file_path)
    speak(f"Screenshot saved as {file_path}.")
    print(f"Screenshot saved as {file_path}")


def open_application(app_name: str) -> None:
    """Open a common Windows application."""
    app_map = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "command prompt": "cmd.exe",
        "browser": "msedge.exe",
    }

    executable = app_map.get(app_name.lower(), app_name)
    try:
        subprocess.Popen(executable)
        speak(f"Opening {app_name}.")
        print(f"Opened {app_name}")
    except Exception as exc:
        print(f"Application open error: {exc}")
        speak(f"I could not open {app_name}.")


def open_website(url: str) -> None:
    """Open a website in the default browser."""
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"

    try:
        webbrowser.open(url)
        print(f"Opened website: {url}")
    except Exception as exc:
        print(f"Website open error: {exc}")
        speak("I could not open the website.")


def take_command() -> Optional[str]:
    """Capture voice input and return the cleaned recognized text."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)
    except sr.WaitTimeoutError:
        speak("Timeout occurred. Please try again.")
        return None
    except OSError:
        speak("Microphone is not available on this device.")
        return None

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        cleaned = query.strip().lower()
        print(cleaned)
        return cleaned
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None
    except Exception as exc:
        speak(f"An error occurred while processing your voice command: {exc}")
        print(f"Voice error: {exc}")
        return None


def play_music(song_name: str = "") -> None:
    """Play a song from the Music folder."""
    music_dir = Path.home() / "Music"
    if not music_dir.exists():
        speak("I could not find your music folder.")
        print("Music directory not found")
        return

    supported = {".mp3", ".wav", ".flac", ".m4a", ".aac"}
    songs = [
        file.name for file in music_dir.iterdir()
        if file.is_file() and file.suffix.lower() in supported
    ]

    if song_name:
        songs = [song for song in songs if song_name.lower() in song.lower()]

    if not songs:
        speak("No song found.")
        print("No song found.")
        return

    selected_song = random.choice(songs)
    song_path = music_dir / selected_song

    try:
        os.startfile(str(song_path))
        speak(f"Playing {selected_song}.")
        print(f"Playing {selected_song}")
    except AttributeError:
        speak("This feature is only supported on Windows.")
    except OSError as exc:
        speak("I could not open the selected song.")
        print(f"Music playback error: {exc}")


def set_name() -> None:
    """Ask the user for a new assistant name and save it."""
    speak("What would you like to name me?")
    chosen_name = take_command()
    if not chosen_name:
        speak("Sorry, I could not catch that.")
        return

    cleaned_name = chosen_name.strip()
    if not cleaned_name or len(cleaned_name) > 30:
        speak("That name is not valid. Please choose a shorter one.")
        return

    try:
        NAME_FILE.write_text(cleaned_name, encoding="utf-8")
        speak(f"Alright, I will be called {cleaned_name} from now on.")
        print(f"Assistant name set to {cleaned_name}")
    except OSError as exc:
        speak("I could not save the name right now.")
        print(f"Name save error: {exc}")


def search_wikipedia(query: str) -> None:
    """Search Wikipedia and speak a short summary."""
    if not query:
        speak("Please specify what you want to search for on Wikipedia.")
        return

    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
    except Exception:
        speak("I could not find anything on Wikipedia.")


def tell_joke() -> None:
    """Tell a random joke."""
    try:
        joke = pyjokes.get_joke(language="en")
        speak(joke)
        print(joke)
    except Exception as exc:
        print(f"Joke error: {exc}")
        speak("I could not think of a joke right now.")


def shutdown_system() -> None:
    """Shut down the system."""
    speak("Shutting down the system, goodbye!")
    try:
        os.system("shutdown /s /f /t 1")
    except Exception as exc:
        print(f"Shutdown error: {exc}")


def restart_system() -> None:
    """Restart the system."""
    speak("Restarting the system, please wait!")
    try:
        os.system("shutdown /r /f /t 1")
    except Exception as exc:
        print(f"Restart error: {exc}")


def get_help_message() -> str:
    """Return a list of supported command examples."""
    return (
        "You can ask me for the time, the date, a joke, a Wikipedia summary, "
        "to open Google or YouTube, to play music, to take a screenshot, to open "
        "Notepad or Calculator, or to restart or shut down the computer."
    )


def handle_command(query: str) -> bool:
    """Handle a spoken command and return whether the assistant should continue listening."""
    if not query:
        return True

    normalized = " ".join(query.strip().lower().replace("'", "").split())

    if any(phrase in normalized for phrase in ["what time", "time is it", "whats the time", "current time"]):
        get_time()
    elif any(phrase in normalized for phrase in ["what is the date", "date today", "current date", "whats the date"]):
        get_date()
    elif "who are you" in normalized or "your name" in normalized:
        speak(f"I am {load_name()}, your desktop assistant.")
    elif "help" in normalized:
        help_text = get_help_message()
        speak(help_text)
        print(help_text)
    elif "wikipedia" in normalized:
        topic = normalized.replace("wikipedia", "").strip()
        for prefix in ("search for", "search", "for", "about"):
            if topic.startswith(prefix):
                topic = topic[len(prefix):].strip()
        topic = topic.strip()
        if not topic:
            topic = "python"
        search_wikipedia(topic)
    elif "play music" in normalized or "play song" in normalized:
        song_name = normalized.replace("play music", "").replace("play song", "").strip()
        play_music(song_name)
    elif "open youtube" in normalized:
        open_website("https://youtube.com")
    elif "open google" in normalized:
        open_website("https://google.com")
    elif "open notepad" in normalized:
        open_application("notepad")
    elif "open calculator" in normalized:
        open_application("calculator")
    elif "open command prompt" in normalized or "open cmd" in normalized:
        open_application("command prompt")
    elif "change your name" in normalized:
        set_name()
    elif "screenshot" in normalized:
        take_screenshot()
        speak("I have taken the screenshot, please check it.")
    elif "tell me a joke" in normalized or "joke" in normalized:
        tell_joke()
    elif any(phrase in normalized for phrase in ["shutdown", "shut down", "power off"]):
        shutdown_system()
        return False
    elif "restart" in normalized:
        restart_system()
        return False
    elif "offline" in normalized or "exit" in normalized or "goodbye" in normalized:
        speak("Going offline. Have a good day!")
        return False
    else:
        speak("I am ready to help. Please ask me a valid command.")

    return True


def main() -> None:
    """Run the voice assistant loop."""
    wish_me()

    while True:
        query = take_command()
        if not query:
            continue

        if not handle_command(query):
            break


if __name__ == "__main__":
    main()
