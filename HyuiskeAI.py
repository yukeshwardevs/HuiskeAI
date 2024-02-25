import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
import requests
import shutil
from twilio.rest import Client
import ecapture as ec
import ctypes
import disutils

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I am Huiske")
    speak("Your personal desktop assistant")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    wish_me()

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Overflow. Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            music_dir = "C:\\Users\\GAURAV\\Music"  # Change to your music directory
            songs = os.listdir(music_dir)
            #os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'open opera' in query:
            code_path = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(code_path)

        elif 'email to gaurav' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "receiver_email@example.com"  # Change to the recipient's email address
                #send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = take_command()
                speak("Whom should I send")
                to = input()  # Enter the recipient's email address
                #send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you're fine")

        elif "exit" in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Gaurav.")

        elif "calculate" in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "").replace("play", "")
            webbrowser.open(query)

        elif "lock window" in query:
            speak("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown /p /f')

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'news' in query:
            # Add your news API handling here
            pass

        elif 'weather' in query:
            # Add weather API handling here
            pass

        elif 'send message' in query:
            # Add Twilio API handling here
            pass

        elif 'camera' in query or 'take a photo' in query:
            ec.capture(0, "Jarvis Camera", "img.jpg")

        # Add more functionalities as needed

