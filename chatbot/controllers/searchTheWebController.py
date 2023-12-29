import threading
import time

from modules.searchTheWeb import search
from modules.searchTheWeb import trim

from tools.say import driver as say

def driver(text):
    if '.' not in text:
        text = trim(text)
    
    if not text:
        say("What do you want to search for?")
        text = input()

    browser_thread = threading.Thread(target=search, args=(text,))
    # Allow thread to run even after program exits
    browser_thread.daemon = True
    browser_thread.start()
    time.sleep(0.5)