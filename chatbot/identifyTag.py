import torch

from chatbot.nltk_utls import bag_of_words, tokenize

def driver(intents, all_words, device, model, tags, msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    print(tag, probs[0][predicted.item()])
    prob = probs[0][predicted.item()]

    if prob.item() > 0.85:
        return tag
    
    return "unknown"