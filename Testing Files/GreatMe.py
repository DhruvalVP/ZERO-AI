import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) 
engine.setProperty("rate", 140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greatMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir. Please tell me how can I help you?")
    elif hour >=12 and hour<=18:
        speak("Good Afternoon Sir. Please tell me how can I help you?")

    else:
        speak("Good Evening Sir. Please tell me how can I help you?")

    #speak("Please tell me how can I help you?")