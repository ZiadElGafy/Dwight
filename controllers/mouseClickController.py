from tools.mouseClick import *
from tools.say import driver as say

def get_search_word(prompt):
    segments = prompt.split()

def driver(prompt):
    double_click = "double click" in prompt.lower() or "doubleclick" in prompt.lower()
    
    search_word = trim(prompt)

    if search_word == None:
        say("Enter word to search for")
        search_word = input()

    search_word = search_word.lower()

    screenshot_path = get_screenshot_path()

    # Create image variable
    image = create_screenshot(screenshot_path)

    # Search for the word in the image
    search_word_found = is_text_in_image(image, search_word)

    if search_word_found:
        col, row = get_click_coordinates(image, search_word)
        click(col, row, double_click)
    else:
        say(f"{search_word} was not found on the screen.")

    # Remove screenshot
    remove_screenshot(screenshot_path)