import time
import threading
import pyttsx3
from playsound3 import playsound

engine = pyttsx3.init()
engine.setProperty('rate', 200)
def song():
    playsound ("bday.mp3")  # Ensure this is the correct path to your file

name = input("what is your name? >>> ")

def bday():

    song_thread = threading.Thread(target=song)
    song_thread.start()
    time.sleep(1.2)
    for i in range(2):
        engine.say("happy birthday to you")
        engine.runAndWait()
        time.sleep(2)
    engine.say(f"happy birthday dear {name},")
    engine.runAndWait()
    time.sleep(2)
    engine.say("happy birthday toooo you")
    engine.runAndWait()
    time.sleep(0.5)

    # Fix the input check by using 'in' for comparison
    if input("would u like that to play again? >>> ") ==  "yes"or "y" or "again"or "mhm" or 'yea' or "yeah" or "sure" or "ya":
        bday()

bday()
