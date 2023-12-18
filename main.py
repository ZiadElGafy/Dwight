import os, random, json, torch
from modules.googleMeet import driver as google_meet_driver
from modules.searchTheWeb import driver as search_the_web_driver
from modules.googleCalendar import driver as google_calendar_driver
from modules.prayerTimes import driver as prayer_times_driver
from modules.weatherForecast import driver as weather_forecast_driver
from chatbot.nltk_utls import bag_of_words, tokenize
from chatbot.identifyTag import driver as get_tag
from chatbot.model import NeuralNet
from chatbot.preprocessModel import driver as preprocess_model
from chatbot.controllers.promptController import driver as execute_prompt
from tools.say import driver as say

def main():
    # moving this line to the global namespace improves performance
    # but immediately calls preprocess_model() at the start of main.py
    intents, all_words, device, model, tags = preprocess_model()

    print("Start")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break
        tag = get_tag(intents, all_words, device, model, tags, sentence)
        execute_prompt(intents, tag, sentence)

if __name__ == "__main__":
    main()