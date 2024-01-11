from controllers.promptController import execute_prompt
from chatbot.preprocessModel import driver as preprocess_model
from chatbot.identifyTag import driver as get_tag
from tools.listen import driver as listen
from tools.say import driver as say
from playsound import playsound

def main():
    intents, all_words, device, model, tags = preprocess_model()

    say("Ready")
    while True:
        text = listen()

        if not text:
            continue

        print(text)

        if "Dwight" in text:
            text = text.split("Dwight")[1][1:]

            if not text:
                playsound("sounds/on.mp3")
                text = listen()

            while not text:
                say("Didn't catch that")
                text = listen()

            playsound("sounds/off.mp3")

            say(f"You said: {text}")
            
            tag = get_tag(intents, all_words, device, model, tags, text)
            execute_prompt(intents, tag, text)
            say("done")

if __name__ == "__main__":
    main()