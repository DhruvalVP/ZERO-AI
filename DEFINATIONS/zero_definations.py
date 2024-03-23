#from DEFINATIONS.Zero_Custom_Voice.zero_customVoice import say
import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import os
import datetime
from BRAIN.API_KEY.gpt_api_key import apikey
import wikipedia
import pygame
import time
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import threading

model = Model("E:\\Python\\Professional\\ZERO AI Laboratories\\ZERO Ultimate Offline\\BRAIN\\VOSK_MODEL\\vosk_model_en_danzu")    # Write NAME of the Folder of VOSK MODEL
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()

stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# SPEAKING Function()
    
def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id) 
    engine.setProperty("rate",165)
    engine.setProperty("threshold", 200)
    engine.say(text)
    engine.runAndWait()

def run_say_thread(text):
    say_thread = threading.Thread(target=say, args=(text))

    say_thread.start()
    

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        time.sleep(sound.get_length())  # Pause to let the sound finish playing
    except pygame.error as e:
        return None
    
def ListeningSound():
    play_sound("E:\\Python\\Professional\\ZERO AI Laboratories\\ZERO Ultimate Offline\\AUDIO_Files\\Listening v1.mp3")

chatStr = ""
# https://YOUtU.be/Z3ZAjoi4x6Q
def chat(query):
    global chatStr
    #print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n ZERO-AI:"
    response_raw = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt= chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0.4
    )
    response = response_raw["choices"][0]["text"]
    #todo: Wrap this inside of a Try catch box
    
    if "OpenAI" in response:
        response = response.replace("OpenAI","ZERO-AI Laboratories")
    try:
        print(response)
        say(response)
        chatStr += f"{response}\n"
        return response
    except Exception as e:
        return "."
        
    '''try:
        print(response["choices"][0]["text"])
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        return "."'''
    
    '''with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)'''

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    #todo: Wrap this text inside of a try catch block
    #print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"Openai/prompt- {random.randit(1, 23434343)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)



# LISTENING Function()

def takeCommand():
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        
        try:
            if recognizer.AcceptWaveform(data):
                query = recognizer.Result()
                query = json.loads(query)
                query = query['text']
                query = str(query)
                # hey_zero = text[14:-3]
                #print('Boss: ' + query['text'])
                return query
            
        except Exception as e:
            return "."

def takeCommand_google():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        r.energy_threshold = 300
        audio = r.listen(source)
        try:
            print("Processing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "."

#To Get current DATE and TIME value FUNCTION()
'''def print_time():
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%I:%M %p")   
    
    print("Current Time is : {}".format(formatted_time))

def print_date():
    current_datetime = datetime.datetime.now()
    formatted_date = current_datetime.strftime("%d-%B-%Y")    
    
    print("Current Date is : {}".format(formatted_date))'''

#Greating Function()
def greatMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning Sir. Begin your query by saying, 'Hey ZERO', or 'Okay ZERO'")
    elif hour >=12 and hour<=18:
        say("Good Afternoon Sir. Begin your query by saying, 'Hey ZERO', or 'Okay ZERO'")

    else:
        say("Good Evening Sir. Begin your query by saying, 'Hey ZERO', or 'Okay ZERO'")


def extract_query(hey_zero, prefixes):
    for prefix in prefixes:
        if hey_zero.startswith(prefix):
            query = hey_zero[len(prefix):].strip()
            return query
    return "."


'''def alarm(query):
    timehere = open("alarm_text.txt")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")'''