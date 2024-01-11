import speech_recognition as sr

recognizer = sr.Recognizer()

def driver():
    print("Listening")
    with sr.Microphone() as mic:
        # recognizer.pause_threshold = 0.5
        recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
        audio = recognizer.listen(mic)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print("Error with the speech recognition service; {0}".format(e))
            return None