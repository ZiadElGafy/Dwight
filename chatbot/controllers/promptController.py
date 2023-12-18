from chatbot.respond import driver as get_response

def driver(intents, tag, prompt):
    response = get_response(intents, tag)
    if response:
        print(response)