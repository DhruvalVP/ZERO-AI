import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import os
import datetime
from BRAIN.API_KEY.gpt_api_key import apikey
import wikipedia
import requests
import subprocess
from pytube import YouTube
import threading
from plyer import notification
#from DEFINATIONS.Zero_Custom_Voice.zero_customVoice import say
from DEFINATIONS.zero_definations import say
from DEFINATIONS.zero_definations import takeCommand
from BRAIN.LOCATION.location import find_location

'''engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[4].id) 
engine.setProperty("rate",145)'''

'''def say(text):
    engine.say(text)
    engine.runAndWait()'''
    

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) +32
    return celsius, fahrenheit

def weather_report(CITY):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "d190d259afb6e0039746d99691712262"
    
    url = BASE_URL + "appid=" + api_key + "&q=" + CITY
    response = requests.get(url).json()
    try:
        temp_kelvin = response['main']['temp']
        #from cmd_functions import kelvin_to_celsius_fahrenheit
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        print(f"\nTemperature in {CITY} is {temp_celsius:.2f} °C")
        print(f"Feels like {feels_like_celsius:.0f} °C")
        print(f"Humidity in {CITY} is {humidity}%")
        print(f"{CITY} has {description}")
        say(f"Temperature in {CITY} is, {temp_celsius:.2f} degree celsius, but feels like, {feels_like_celsius:.0f} degree celsius. Humi-dity in {CITY} is, {humidity}%. In general, {CITY} has {description}.")
        return temp_celsius, temp_fahrenheit, feels_like_celsius, feels_like_fahrenheit, humidity, description
    
    except Exception as e:
        print(e)
        say("Give valid City name!")
        return "exception"
    '''print(f"Temperature in {CITY} : {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
    print(f"Temperature in {CITY} feels like : {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity in {CITY} : {humidity}%")
    print(f"General Weather in {CITY} : {description}")'''

def start_file_minimized(file_path):
    # Use the start /min command to run the file minimized on Windows
    subprocess.Popen(['start', '/min', file_path], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def start_alarm(query):
    #alarm_text = "E:\\Python\\Professional\\ZERO AI Laboratories\\ZERO Ultimate Offline\\BRAIN\\ALARM_SYSTEM\\alarm_text.txt"
    timehere = open(r"alarm_text.txt", "a")
    timehere.truncate(0)
    timehere.write(query)
    timehere.close()
    #file_path = "alarm.py"

    start_file_minimized(r"alarm.py")
    #os.startfile("alarm.py")

def yt_download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    print("\nDownloading video")
    notification.notify(
        title='Download Started',
        message=f'Downloading {youtube_object.title}',
        app_name='YouTube Downloader'
    )

    try:
        youtube_object.download()
        print("Video downloaded Successfully!")
        notification.notify(
            title='Download Completed',
            message=f'{youtube_object.title} downloaded successfully',
            app_name='YouTube Downloader'
        )
        return None
    
    except:
        print("An error has occurred")
        #say("Error occured while Downloading the video")
        notification.notify(
            title='Download Error',
            message=f'An error occurred during download',
            app_name='YouTube Downloader'
        )
        return None

def download_video_thread(link):
    yt_download(link)


def cmd_functions(query):
    sites = [["youtube", "https://www.youtube.com"],["you tube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            say(f"opening {site[0]} sir.")
            webbrowser.open(site[1])

    if "open music" in query.lower():
        os.startfile("D:\\Protected D\\Music\\Engulis Rocks")

    elif "open music" in query.lower():
        os.startfile("D:\\Protected D\\Music\\Engulis Rocks")

    elif 'take input' in query:
        say("Enter your Query")
        query = input("\nEnter your query : ")
        from zero_ultimate_main import chat
        chat(query)

    elif 'your name' in query:
        say("I am ZERO. I am here to assist you.")
    
    elif 'who are you' in query:
        say("I am ZERO A I Assistant. I can answer to your queries and do several tasks on your command.")
    
    elif 'how are you' in query:
        say("I am great. How can I help you.")

    elif 'how r you' in query:
        say("I am great. How can I help you.")

    elif 'how r u' in query:
        say("I am great. How can I help you.")

    elif 'how are u' in query:
        say("I am great. How can I help you.")
        
    elif "check time" in query or 'jack time' in query:
        strfTime = datetime.datetime.now().strftime("%I:%M %p")
        say(f"The time is {strfTime}")

    elif query.startswith("check date") or 'jack date' in query or 'jack did' in query or 'check did' in query:
        strfDate = datetime.datetime.now().strftime("%d-%B-%Y")
        say(f"The Date is {strfDate}")
    
    elif "set an alarm" in query or "set alarm" in query or "sat alone" in query or "set alone" in query or "sat alarm" in query:
        say("if you want to set alarm, say yes, else say no!!")
        while True:
            print("Listening...\n")
            y_n_alarm = takeCommand().lower()
            if y_n_alarm == "yes":
                print("Input time example HH MM : ")
                say("please input alarm time in following format!")
                a = input("Please tell the time :- ")
                start_alarm(a+" 00")
                say("Done, sir")
                break
            elif y_n_alarm == "no":
                say("Okay, not setting alarm!!")
                break
            else:
                say("Sir do you want to set alarm, yes or no!!")

    elif 'my location' in query or 'check location' in query or 'current location' in query:
        say("Fetching your location...")
        my_location = find_location()
        say(my_location)

    elif any(keyword in query for keyword in ['run speedtest', 'check internet speed', 'check speed', 'run speed test', 'internet speed']):
        from BRAIN.SPEED_TEST.speed_test import testSpeed
        print("Checking your Internet speed sir...")
        say("Checking your Internet speed sir...")
        internet_speed = threading.Thread(target=testSpeed, args=())
        internet_speed.start()

        

    elif 'wikipedia' in query:
        say('Searching Wikipedia...')
        query = query.replace("wikipeedia", "")
        results = wikipedia.summary(query, sentences=2)
        say("According to Wikipedia")
        say(results)
    
    elif 'open browser' in query:
        msedge = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(msedge)
        say("Opening Microsoft Edge!")


        """elif 'check weather' in query:

            CITY = "Anand"
            weather_report(CITY)"""
        
    elif query.startswith("download youtube") or query.startswith("download video"):
        say("Enter the YouTube video Link")
        link = input("Enter the YouTube video URL: ")
        download_thread = threading.Thread(target=download_video_thread, args=(link,))
        download_thread.start()
        say("Downloading in Background")
    

    elif "zero ai laboratories" in query or "zero ai" in query or "zero" in query:
        say("ZERO-AI Laboratory was founded by Dhruval Patel and Jack in year 2024. This AI project had to be made for a Hackathon event organized at CVM University in March 2024.")
    
    elif "using your intelligence" in query.lower():
        from zero_ultimate_main import ai
        ai(prompt=query)
    
    elif query.startswith("goodbye"):
        say("Goodbye Sir! See you later!")
        exit()
    
    
    else:
        from zero_ultimate_main import chat
        chat(query)