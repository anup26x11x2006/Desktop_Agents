import configparser
import random
import smtplib
import sys

import wikipedia
from pygame import mixer

from actions import open_url, search, speak

config = configparser.ConfigParser()
config.read("config.ini")


def _get_music_folder():
    music_path = config.get("DEFAULT", "musicPath", fallback="")
    if not music_path:
        music_path = config.get("DEFAULT", "musicpath", fallback="")
    return music_path.strip().rstrip("/")


def command_wikipedia(debug, query):
    search_phrase = query.replace("wikipedia", "", 1).strip()
    if not search_phrase:
        speak("What do you want to search on Wikipedia?")
        return

    speak("Searching wikipedia...")
    try:
        results = wikipedia.summary(search_phrase, sentences=2)
        if debug == "True":
            print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as error:
        speak("There were multiple matches. Please be more specific.")
        if debug == "True":
            print(error)
    except Exception as error:
        speak("I could not find a matching Wikipedia result.")
        if debug == "True":
            print(error)


def command_whatsup():
    messages = [
        "Just doing my thing!",
        "I am fine!",
        "Nice!",
        "I am nice and full of energy.",
    ]
    speak(random.choice(messages))


def command_open(query, popular_websites, debug, search_engine, take_command):
    website = query.replace("open", "", 1).strip().lower()
    if not website:
        speak("Which website would you like to open?")
        return

    try:
        open_url(popular_websites[website])
    except KeyError:
        if debug == "True":
            print(f"Unknown website: {website}")
        speak(f"Sorry, I don't know the website {website}")
        speak(f"Do you want me to search {website} in the web?")
        if take_command().lower() == "yes":
            search(website, search_engine)


def command_search(query, search_engine):
    search_query = query.replace("search", "", 1).strip()
    if "for" in search_query:
        search_query = search_query.split("for", 1)[1].strip()
    if not search_query:
        speak("What should I search for?")
        return
    search(search_query, search_engine)


def command_mail(take_command):
    speak("Who is the recipient?")
    recipient = take_command().strip()

    try:
        speak("What should I say?")
        content = take_command()

        email = config["EMAIL"]
        server = smtplib.SMTP(email["server"], int(email["port"]))
        server.ehlo()
        server.starttls()
        server.login(email["username"], email["password"])
        server.sendmail(email["username"], recipient, content)
        server.close()
        speak("Email sent!")
    except Exception:
        speak("Sorry Sir!")
        speak("I am unable to send your message at this moment!")


def command_nothing():
    speak("Okay")
    speak("Bye Sir, have a good day.")
    sys.exit()


def command_hello():
    speak("Hello Sir")


def command_bye():
    speak("Bye Sir, have a good day.")
    sys.exit()


def command_play_music():
    music_folder = _get_music_folder()
    if not music_folder:
        speak("Music folder is not configured yet.")
        return

    try:
        mixer.init()
        music_files = [
            "music1.mp3",
            "music2.mp3",
            "music3.mp3",
            "music4.mp3",
        ]
        random_music = f"{music_folder}/{random.choice(music_files)}"
        speak("Playing your request")
        mixer.music.load(random_music)
        mixer.music.play()
    except Exception as exc:
        speak(f"I couldn't play the requested music. {exc}")


def command_pause_music():
    try:
        mixer.music.pause()
    except Exception:
        pass


def command_stop_music():
    try:
        mixer.music.stop()
    except Exception:
        pass


def command_unpause_music():
    try:
        mixer.music.unpause()
    except Exception:
        pass
