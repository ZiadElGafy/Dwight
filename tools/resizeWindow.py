import pygetwindow as gw
from tools.say import driver as say

def trim(text):
    limiters = [
        "minimize",
        "maximize",
        "restore"
    ]

    for limiter in limiters:
        segments = text.split(limiter)
        text = segments[-1]
        if len(text) > 0 and text[0] == ' ':
            text = text[1:]

    return text

def resize_window(target_window_title, operation):
    try:
        target_window_segments = target_window_title.split()
        target_window = None
        for segment in target_window_segments:
            target_window = gw.getWindowsWithTitle(segment)
            if target_window:
                break
        if target_window:
            if operation == "minimize":
                target_window[0].minimize()
            elif operation == "maximize":
                target_window[0].maximize()
            elif operation == "restore":
                target_window[0].restore()
        else:
            say(f"Window '{target_window_title}' not found.")
    except Exception as e:
        print(f'Error: {e}')
