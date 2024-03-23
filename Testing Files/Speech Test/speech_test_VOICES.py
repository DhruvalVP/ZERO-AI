import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id) 
engine.setProperty("rate",145)

print(voices)
# SPEAKING Function()
    
def say(text):
    engine.say(text)
    engine.runAndWait()

say("I am ZERO A.I.")
say("Hello sir, how are you?")
say("Weather in anand is 29 degree celsius, and Humidity is 30%")
say("I am fine sir, how may i help you?")