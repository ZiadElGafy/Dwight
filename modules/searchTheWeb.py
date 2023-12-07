import webbrowser
import threading
import time

import os
from dotenv import load_dotenv
load_dotenv()

BROWSER_PATH = os.getenv("BROWSER_PATH")

def search(text):
    words = text.split(" ")
    url = ""

    if len(words) == 1 and '.' in words[0]:
        url = words[0]
    else:
        url = "https://www.google.com/search?q=" + words[0]
        for i in range(len(words) - 1):
            url = url + '+' + words[i + 1]
    
    webbrowser.get(BROWSER_PATH).open_new(url)
    
def driver(text):
    if not text:
        text = input("Enter text to search for: ")
    browser_thread = threading.Thread(target=search, args=(text,))
    # Allow thread to run even after program exits
    browser_thread.daemon = True
    browser_thread.start()
    time.sleep(0.5)