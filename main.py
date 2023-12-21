from chatbot.controllers.promptController import driver as get_prompt
from chatbot.preprocessModel import driver as preprocess_model

def main():
    intents, all_words, device, model, tags = preprocess_model()

    while True:
        get_prompt(intents, all_words, device, model, tags)

if __name__ == "__main__":
    main()