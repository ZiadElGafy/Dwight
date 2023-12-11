import pyttsx3

def driver(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()