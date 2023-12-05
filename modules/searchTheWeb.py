import webbrowser
import threading
import time

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

def search(text):
    words = text.split(" ")
    url = ""

    if len(words) == 1 and '.' in words[0]:
        url = words[0]
    else:
        url = "https://www.google.com/search?q=" + words[0]
        for i in range(len(words) - 1):
            url = url + '+' + words[i + 1]
    
    webbrowser.get(chrome_path).open_new(url)
    
def driver():
    search_text = input("Enter text to search for: ")
    browser_thread = threading.Thread(target=search, args=(search_text,))
    # Allow thread to run even after program exits
    browser_thread.daemon = True
    browser_thread.start()
    time.sleep(0.5)
