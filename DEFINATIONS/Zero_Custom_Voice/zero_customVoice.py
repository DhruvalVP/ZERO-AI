import os
import pygame
import time

voice1 = ""
voice2 = "en-GB-SoniaNeural"
voice3 = "en-IN-NeerjaNeural"
voice4 = "en-IN-PrabhatNeural"

def play_sound(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        time.sleep(sound.get_length())  # Pause to let the sound finish playing
    except pygame.error as e:
        return None

def say(query):
    voice = "en-US-SteffanNeural"
    command = f'edge-tts --rate=+15% --voice "{voice}" --text "{query}" --write-media "response.mp3"'
    os.system(command)

    try:
        play_sound("response.mp3")

    except Exception as e:
        #print(e)
        return None
    '''finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()'''


#say("As of my last knowledge update in January 2022, there was no specific information about parameters like top_p, frequency_penalty, and presence_penalty in the ChatGPT API documentation. However, OpenAI may have introduced new features or updates since then.")
text = "Chapter	1\nLOG	ENTRY:	SOL	6\nI’m	pretty	much	screwed.\nThat’s	my	considered	opinion.\nScrewed.\nSix	days	in	to	what	should	be	a	greatest	two	months	of	my	life,	and\nit’s	turned in to a	nightmare.\nI	don’t	even know	who’ll	read this. I	guess	someone	will	find it\neventually. Maybe	a	hundred years	from	now.\nFor	the	record… I	didn’t	die	on Sol	6. Certainly the	rest	of	the	crew\nthought	I	did, and I	can’t	blame	them. Maybe	there’ll	be	a	day of	national\nmourning for	me, and my Wikipedia	page	will	say “Mark Watney is	the\nonly human being to have	died on Mars.”\nAnd it’ll	be	right, probably. Cause	I’ll	surely die	here. Just	not	on Sol\n6 when everyone	thinks	I	did.\nLet’s	see… where	do I	begin?\nThe	Ares	program. Mankind reaching out	to Mars	to send people	to\nanother	planet	for	the	very first	time	and expand the	horizons	of\nhumanity blah, blah, blah. The	Ares	1 crew	did their	thing and came	back\nheroes. They got	the	parades	and fame	and love	of	the	world.\nAres	2 did the	same	thing, in a	different	location on Mars. They got	a\nfirm	handshake	and a	hot	cup of	coffee	when they got	home.\nAres	3. Well. That	was	my mission. Well, not	mine per	se.\nCommander	Lewis	was	in charge. I	was	just	one	of	her	crew. Actually, I\nwas	the	very lowest	ranked member	of	the	crew. I	would only be	“in\ncommand”	of	the	mission if	I	were	the	only remaining person.\nWhat	do you know?	I’m	in command.\nI	wonder	if	this	log will	be	recovered before	the	rest	of	the	crew	die	of\nold age?	I	presume	they got	back to Earth all	right. Well, guys, if	you’re\nreading this:	It	wasn’t	your	fault. You did what	you had to do. In your\nposition I	would have	done	the	same	thing. I	don’t	blame	you, and I’m\nglad you survived."
text_2 = "Hello World"
say(text)