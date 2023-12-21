import json
import os
import torch

from chatbot.model import NeuralNet

def driver():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open("chatbot/intents.json") as json_data:
        intents = json.load(json_data)

    data_dir = os.path.join(os.path.dirname(__file__))
    FILE = os.path.join(data_dir, 'chatdata.pth')
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    return intents, all_words, device, model, tags