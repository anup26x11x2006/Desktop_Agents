import configparser
import os
import sys
from pathlib import Path

import speech_recognition as sr

import gui
from actions import (
    change_rate,
    change_voice,
    change_volume,
    extract_command_target,
    extract_search_query,
    get_config_path,
    normalize_query,
    search_engine_selector,
    set_gui_speak,
    speak,
    wish_me,
)
from commands import (
    command_bye,
    command_hello,
    command_mail,
    command_nothing,
    command_open,
    command_pause_music,
    command_play_music,
    command_search,
    command_stop_music,
    command_unpause_music,
    command_whatsup,
    command_wikipedia,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "github": "https://www.github.com",
}


def main(search_engine, take_command, debug):
    def execute_the_command_said_by_user():
        query = take_command()
        normalized = normalize_query(query)

        phrases = {
            "whats up": command_whatsup,
            "how are you": command_whatsup,
            "nothing": command_nothing,
            "abort": command_nothing,
            "stop": command_nothing,
            "hello": command_hello,
            "bye": command_bye,
            "play music": command_play_music,
            "unpause": command_unpause_music,
            "pause music": command_pause_music,
            "stop music": command_stop_music,
        }

        for phrase, command in phrases.items():
            if phrase in normalized:
                command()
                break
        else:
            if "wikipedia" in normalized:
                command_wikipedia(debug, query)
            elif "open" in normalized or "launch" in normalized or "goto" in normalized:
                command_open(query, popular_websites, debug, search_engine, take_command)
            elif "search" in normalized or "look for" in normalized:
                search_query = extract_search_query(query)
                if search_query:
                    command_search(f"search {search_query}", search_engine)
                else:
                    command_search(query, search_engine)
            elif "mail" in normalized:
                command_mail(take_command)
            elif "change rate" in normalized:
                change_rate(query, take_command)
            elif "change voice" in normalized:
                change_voice(query, take_command)
            elif "change volume" in normalized:
                change_volume(query, take_command)

        speak("Next Command! Sir!")

    gui.set_speak_command(execute_the_command_said_by_user)
    set_gui_speak(gui.speak)
    gui.mainloop()


def run():
    config = configparser.ConfigParser()
    config.read(get_config_path(), encoding="utf-8")

    master = config.get("DEFAULT", "master", fallback="User")
    search_engine = search_engine_selector(config)
    debug = config.get("DEFAULT", "debug", fallback="False")

    if debug.strip().lower() == "true":
        def take_command():
            return input("Command |--> ").strip()
    else:
        def take_command():
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                recognizer.pause_threshold = 0.5
                recognizer.energy_threshold = int(config.get("DEFAULT", "energy_threshold", fallback="300"))
                audio = recognizer.listen(source)

            try:
                print("Recognizing....")
                query = recognizer.recognize_google(audio, language="en-in")
                print("user said: " + query)
                return query
            except sr.UnknownValueError:
                if debug == "True":
                    print("Sorry Could You please try again")
                speak("Sorry Could You please try again")
            except Exception as exc:
                if debug == "True":
                    print(exc)
                    print("Say That Again Please")
            return ""

    speak(text="Initializing Jarvis....")
    wish_me(master)
    main(search_engine, take_command, debug)


def main_entry():
    config_path = get_config_path()
    if config_path.exists():
        run()
    else:
        print("You need a config.ini file.")
        print("Check the documentation in the Github Repository.")


if __name__ == "__main__":
    main_entry()
