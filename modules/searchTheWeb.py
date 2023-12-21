import webbrowser
import threading
import time
from tools.getChromePath import driver as get_chrome_path

def search(text):
    words = text.split(" ")
    url = ""

    if len(words) == 1 and '.' in words[0]:
        url = words[0]
    else:
        url = "https://www.google.com/search?q=" + words[0]
        for i in range(len(words) - 1):
            url = url + '+' + words[i + 1]
    
    browser_path = get_chrome_path()
    webbrowser.get(browser_path).open_new(url)
    
def driver(text):
    browser_thread = threading.Thread(target=search, args=(text,))
    # Allow thread to run even after program exits
    browser_thread.daemon = True
    browser_thread.start()
    time.sleep(0.5)