from tools.resizeWindow import *
from tools.say import driver as say

def driver(prompt):
    window_title = trim(prompt)
    if "minimize" in prompt:
        resize_window(window_title, "minimize")
    elif "maximize" in prompt:
        resize_window(window_title, "maximize")
    elif "restore" in prompt:
        resize_window(window_title, "restore")
    else:
        say("Invalid Window Resize Command")