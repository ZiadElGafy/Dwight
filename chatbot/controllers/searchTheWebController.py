from modules.searchTheWeb import driver as search_the_web_driver

from tools.say import driver as say

def trim(text):
    limiters = ["search ",
                "google ",
                "search for ",
                "search google for ",
                "search the web for ",
                "search the internet for ",]

    for limiter in limiters:
        segments = text.split(limiter)
        text = segments[-1]

    return segments[-1]

def driver(text):
    text = trim(text)
    
    if not text:
        say("What do you want to search for?")
        text = input()
        say("On it!")

    search_the_web_driver(text)