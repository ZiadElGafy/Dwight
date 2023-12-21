from chatbot.identifyTag import driver as get_tag
from chatbot.preprocessModel import driver as preprocess_model
from chatbot.controllers.promptController import driver as execute_prompt

def main():
    # moving this line to the global namespace improves performance
    # but immediately calls preprocess_model() at the start of main.py
    intents, all_words, device, model, tags = preprocess_model()

    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break
        tag = get_tag(intents, all_words, device, model, tags, sentence)
        execute_prompt(intents, tag, sentence)

if __name__ == "__main__":
    main()