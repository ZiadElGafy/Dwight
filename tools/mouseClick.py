import os
import pyautogui
import pytesseract

from PIL import Image

from tools.say import driver as say

# Path to the Tesseract executable (update this based on your installation)
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def trim(text):
    limiters = ["double click on the",
                "double click on",
                "click on the",
                "click on",
                "press the",
                "press",
                "click the",
                "click",
                "tap the",
                "tap"]

    for limiter in limiters:
        segments = text.split(limiter)
        text = segments[-1]
        if len(text) > 0 and text[0] == ' ':
            text = text[1:]

    text = text.split(" button")[0]

    return text

def get_screenshot_path():
    script_path = os.path.dirname(os.path.abspath(__file__)) # Path to current file
    file_name = "img.png"
    path = f"{script_path}\\{file_name}"
    return path

def create_screenshot(path):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)
    image = Image.open(f'{path}')
    return image

def get_text_from_screenshot(image):
    text = pytesseract.image_to_string(image)
    return text

def is_text_in_image(image, text):
    return text in pytesseract.image_to_string(image).lower()

def parse(boxes, height):
    ret = []
    for box in boxes:
        split_box = box.split(' ')
        cur_box = [split_box[0].lower()]
        for num in split_box:
            if num == split_box[0]:
                continue
            cur_box.append(int(num))
        cur_box[2] = height - cur_box[2]
        cur_box[4] = height - cur_box[4]
        cur_box[2], cur_box[4] = cur_box[4], cur_box[2]
        ret.append(cur_box)
    return ret

def match(boxes, idx_boxes, text, idx_text):
    p1 = idx_boxes
    p2 = idx_text
    sz_text = len(text)
    while p2 < sz_text and p1 < len(boxes):
        if boxes[p1][0] == text[p2]:
            p1 += 1
            p2 += 1
        else:
            break
        
    return p2 == sz_text

def get_word_coordinates(boxes, idx, sz):
    cur = idx
    mn_col = int(1e9)
    mx_col = -1
    mn_row = int(1e9)
    mx_row = -1
    while cur < idx + sz:
        mn_col = min(mn_col, boxes[cur][1])
        mx_col = max(mn_col, boxes[cur][3])

        mn_row = min(mn_row, boxes[cur][2])
        mx_row = max(mx_row, boxes[cur][4])

        cur += 1
    
    return [mn_col, mn_row, mx_col, mx_row]

def remove_screenshot(path):
    if os.path.exists(path):
        os.remove(path)

def get_click_coordinates(image, search_word):
    coordinates = None

    # Get bounding boxes for each word
    boxes = pytesseract.image_to_boxes(image).splitlines()

    # Parse boxes to return an array for each box with the suitable types
    boxes = parse(boxes, image.height)

    # Search for the word and find its coordinates
    for i in range(len(boxes)):
        if match(boxes, i, search_word, 0):
            coordinates = get_word_coordinates(boxes, i, len(search_word))
            break
    
    if coordinates == None:
        raise Exception("There was a problem locating the word on the screen.")
    
    # Get the center of the word
    col = (coordinates[0] + coordinates[2]) // 2
    row = (coordinates[1] + coordinates[3]) // 2
    
    return col, row

def click(col, row, double_click):
    # Move the mouse to the center of the word
    pyautogui.moveTo(col, row, 0.4, pyautogui.easeInQuad)
    pyautogui.click() if double_click == False else pyautogui.doubleClick()