import pyttsx3
import datetime
import os

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id) 
engine.setProperty("rate",160)

def say(text):
    engine.say(text)
    engine.runAndWait()

extractedtime = open("alarm_text.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarm_text.txt", "r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace(" ",":")
    timeset = str(timenow)
    print(timeset)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == timeset:
            os.startfile("E:\\Python\\Professional\\ZERO AI Laboratories\\ZERO Ultimate Offline\\AUDIO_Files\\Alarm Chimes.mp3")
            say("Alarm ringing Sir!")
            exit()
        elif currenttime + "00:00:30" == timeset:
            exit()

ring(time)
exit()