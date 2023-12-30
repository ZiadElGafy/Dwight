import os

from dotenv import load_dotenv
from openai import OpenAI

from modules.gpt import read_json
from modules.gpt import write_json
from modules.gpt import clear_history

from tools.say import driver as say

load_dotenv("dotenv.env")

API_KEY = os.getenv("OPENAI_API_KEY")
WINDOW_SIZE = 2

def driver(prompt):
    client = OpenAI(api_key = API_KEY) 
    
    chat_history = read_json()
    
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

    response_obj = {"role": response.role , "content":response.content}
    chat_history.append(response_obj)

    if len(chat_history) == (2 * WINDOW_SIZE) + 1:
        chat_history = clear_history(False, chat_history)
    
    write_json(chat_history)