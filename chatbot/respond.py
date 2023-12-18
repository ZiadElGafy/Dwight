import random

def driver(intents, tag):
    response = ""
    for intent in intents['intents']:
        if tag == intent["tag"]:
            if len(intent["responses"]):
                response = random.choice(intent["responses"])
            break

    return response