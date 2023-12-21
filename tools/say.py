import pyttsx3, time

def driver(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    print("Dwight: " + text)
    engine.say(text)
    engine.runAndWait()