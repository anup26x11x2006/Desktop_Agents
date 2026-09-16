#!/usr/bin/env python3

import datetime
import getpass
import os
import random
import smtplib
import subprocess
import sys
import webbrowser
from pathlib import Path

import pyttsx3
import speech_recognition as sr
import wikipedia

import gui

PROJECT_ROOT = Path(__file__).resolve().parent.parent

print("Initializing Jarvis....")
master = getpass.getuser() or "Harsha"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
}


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
    selected_engine = search_engines.get(search_engine.lower(), "https://www.google.com")
    open_url(f"{selected_engine}/search?q={search_query}")


def speak(text):
    gui.speak(text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass


def print_and_speak(text):
    print(text)
    speak(text)


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak(f"Good Morning {master}")
    elif hour < 18:
        speak(f"Good Afternoon {master}")
    else:
        speak(f"Good Evening {master}")


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 0.5
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source)

    print("Recognizing....")
    try:
        query = recognizer.recognize_google(audio, language="en-in")
        print("User said: " + query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry could you please try again?")
    except Exception as exc:
        print(exc)
        print("Say that again, please?")
    return ""


def execute_the_command_said_by_user():
    query = take_command()
    if not query:
        speak("Next Command! Sir!")
        return

    if "wikipedia" in query:
        speak("Searching wikipedia....")
        topic = query.replace("wikipedia", "", 1).strip()
        if topic:
            print_and_speak(wikipedia.summary(topic, sentences=2))

    elif "what's up" in query or "how are you" in query:
        messages = (
            "Just doing my thing!",
            "I am fine!",
            "Nice!",
            "I am nice and full of energy",
        )
        speak(random.choice(messages))

    elif "date" in query:
        print_and_speak(f"{datetime.datetime.now():%A, %B %d, %Y}")

    elif "time" in query:
        print_and_speak(f"{datetime.datetime.now():%I:%M %p}")

    elif "open" in query:
        website = query.replace("open", "", 1).strip().lower()
        if website:
            try:
                open_url(popular_websites[website])
            except KeyError:
                print(f"Unknown website: {website}")
                speak(f"Sorry, I don't know the website {website}")

    elif "search" in query:
        search_query = query.split("for")[-1].strip() if "for" in query else query.replace("search", "", 1).strip()
        search_engine = query.split("for")[0].replace("search", "", 1).strip().lower()
        search(search_query, search_engine or "google")

    elif "email" in query:
        speak("Who is the recipient?")
        recipient = take_command()
        if "me" in recipient:
            try:
                speak("What should I say?")
                content = take_command()
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("Your_Username", "Your_Password")
                server.sendmail("Your_Username", "Recipient_Username", content)
                server.close()
                speak("Email sent!")
            except Exception:
                speak("Sorry Sir! I am unable to send your message at this moment!")

    elif "nothing" in query or "abort" in query or "stop" in query:
        speak("Okay")
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "hello" in query:
        speak("Hello Sir")

    elif "bye" in query:
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "play music" in query:
        music_folder = str(PROJECT_ROOT / "music")
        music_files = ("music1", "music2", "music3", "music4", "music5")
        os.system(f"{music_folder}/{random.choice(music_files)}.mp3")
        speak("Playing your request")

    speak("Next Command! Sir!")


def main():
    speak("Initializing Jarvis....")
    wish_me()
    gui.set_speak_command(execute_the_command_said_by_user)
    gui.mainloop()


if __name__ == "__main__":
    main()
