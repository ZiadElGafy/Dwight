import json

JSON_FILE = 'chatbot/gptHistory.json'
SYSTEM_PROMPT = {
    "role": "system",
    "content": "Your name is Dwight, you're a windows voice assistant. Keep all your answers as concise as possible.",
}

def read_json():
    with open(JSON_FILE, 'r') as file:
        data = json.load(file)
    
    return data

def write_json(content):
    with open(JSON_FILE, 'w') as file:
        json.dump(content, file, indent=4)

def clear_history(entire_file, chat_history):
    if entire_file:
        add_to_sheet(chat_history[1:])
        chat_history.clear()
        chat_history.append(SYSTEM_PROMPT)
        write_json(chat_history)
    else:
        add_to_sheet(chat_history[1:3])
        chat_history = [chat_history[0]] + chat_history[3:]
    
    return chat_history

def add_to_sheet(content):
    pass