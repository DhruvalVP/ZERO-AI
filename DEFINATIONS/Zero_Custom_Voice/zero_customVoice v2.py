import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(query):
    tts = gTTS(text=query, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak("As of my last knowledge update in January 2022, there was no specific information about parameters like top_p, frequency_penalty, and presence_penalty in the ChatGPT API documentation. However, OpenAI may have introduced new features or updates since then.")