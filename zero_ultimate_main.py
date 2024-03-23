#from DEFINATIONS.Zero_Custom_Voice.zero_customVoice import say
from DEFINATIONS.zero_definations import say
from DEFINATIONS.zero_definations import play_sound
from DEFINATIONS.zero_definations import ListeningSound
from DEFINATIONS.zero_definations import chat
from DEFINATIONS.zero_definations import ai
from DEFINATIONS.zero_definations import takeCommand
from DEFINATIONS.zero_definations import greatMe
from DEFINATIONS.zero_definations import extract_query
from DEFINATIONS.zero_definations import takeCommand_google
from FUNCTIONS.cmd_functions import weather_report


if __name__ == '__main__':
    print('ZERO A.I.')
    greatMe()
    #say("Hello, I am ZERO A I")
    
    speech_mode = "offline"

    while True:
        print("\nListening...")

        if speech_mode == "online":
            hey_zero = takeCommand_google().lower()
        elif speech_mode == "offline":
            hey_zero = takeCommand().lower()

        prefixes = ("hey zero ", "okay zero ", "ok zero ", "a0", "hey siri", "okay 0", "ok 0")
        query = extract_query(hey_zero, prefixes)
        
        if query != ".":
            ListeningSound()
            print(f"User : {query}")
            #print("Extracted query:", query)

            if 'check weather' in query or 'check whether' in query or "jack whether" in query:
                say("Give name of the City!")
                while True:
                    print("\nCity...")
                    CITY = takeCommand_google()

                    if CITY == ".":
                        continue

                    elif 'stop' in CITY.lower() or 'no' in CITY.lower() or "don't" in CITY or 'do not' in CITY or 'exit' in CITY:
                        say("Okay, Not checking weather report.")
                        query = '.'
                        break
                     
                    weather_data = weather_report(CITY)
                    ListeningSound()
                    #print(weather_data)
                    if weather_data == 'exception':
                        continue
                    else:
                        query = '.'
                        break
            
            

            elif "offline mode" in query:
                speech_mode = "offline"
                say("Switching to Offline Mode now!!")
                query = "."
            elif "online mode" in query or "online mod" in query:
                speech_mode = "online"
                say("Switching to Online Mode now!!")
                query = "."
                    
            if "." in query:
                continue

            else:
                from FUNCTIONS.cmd_functions import cmd_functions
                cmd_functions(query)
                ListeningSound()
