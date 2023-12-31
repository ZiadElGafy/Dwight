import datetime
import os

from dotenv import load_dotenv
from datetime import datetime
from modules.googleSheets import driver as add_to_sheet
from modules.gpt import read_json
from modules.gpt import write_json
from modules.gpt import clear_history
from openai import OpenAI

from tools.say import driver as say

load_dotenv("dotenv.env")

API_KEY = os.getenv("OPENAI_API_KEY")
WINDOW_SIZE = 3
THREAD_TIMEOUT = 90

def clear_gpt_thread():
    chat_history = read_json()
    clear_history(entire_file = True, chat_history = chat_history)

def thread_timed_out():
    chat_history = read_json()

    if len(chat_history) == 1:
        return True
    
    time_str = chat_history[-1]["time"]
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    if (datetime.now() - time).seconds > THREAD_TIMEOUT:
        return True
    
    return False

def driver(prompt):
    client = OpenAI(api_key = API_KEY) 
    
    chat_history = read_json()

    # Remove time from object as the gpt api doesn't recognize it
    for object in chat_history:
        if "time" in object:
            del object["time"]

    print(chat_history)
    
    new_prompt = {
        "role": "user",
        "content": prompt,
    }
    chat_history.append(new_prompt)
    
    ChatCompletion = client.chat.completions.create(
        messages = chat_history,
        model="gpt-3.5-turbo",
    )
    response = ChatCompletion.choices[0].message
    say(response.content)
    add_to_sheet(prompt, response.content)

    now = datetime.now()
    time_now = now.strftime("%Y-%m-%d %H:%M:%S")

    response_obj = {"role": response.role , "content": response.content, "time": time_now}
    chat_history.append(response_obj)

    if len(chat_history) == (2 * WINDOW_SIZE) + 1:
        chat_history = clear_history(False, chat_history)
    
    write_json(chat_history)