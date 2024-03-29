import webbrowser

from tools.getChromePath import driver as get_chrome_path

def trim(text):
    limiters = ["search the internet for",
                "search the internet"
                "search the web for",
                "search the web",
                "search google for",
                "search google",
                "search for",
                "google",
                "search"]

    for limiter in limiters:
        segments = text.split(limiter)
        text = segments[-1]
        if len(text) > 0 and text[0] == ' ':
            text = text[1:]

    return segments[-1]

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