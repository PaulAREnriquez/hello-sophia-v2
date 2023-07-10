import random
import json
import torch
from model import ChatNet

from nltk_utils import bag_of_words, tokenize

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open("./data/intents.json", "r") as f:
    intents = json.load(f)

file = "data.pth"
data = torch.load(file)

input_size = data["input_size"]
hidden_layer_size = data["hidden_layer_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = ChatNet(
    input_size=input_size, hidden_layer_size=hidden_layer_size, num_classes=output_size
).to(device)
model.load_state_dict(model_state)

# Evaluation
model.eval()

bot_name = "Sophia"
threshold = 0.75


def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)

    X = X.reshape(1, X.shape[0])  # 1 row of X.shape[0] elements

    X = (
        torch.from_numpy(X).to(dtype=torch.float).to(device)
    )  # we convert the numpy array to float tensor [[]]

    output = model.forward(
        X
    )  # returns a tensor [[]], which is the prediction of the model

    # torch.max() returns a tuple, the max value and the index of the max value
    # we get the index of the maximum value
    _, predicted = torch.max(output, dim=1)

    # predicted is the same as predicted.item(), they are equal to the index
    # .item() is used to get the python integer, it can only be used for scalars
    # we get the item in the tags list on that sepcific index
    tag = tags[predicted.item()]

    probs = torch.softmax(
        output, dim=1
    )  # torch.softmax converts the predictions into probabilities

    # probs[0] contains the array of probabilities, and we pass [predicted.item()] as an indexer to get the index of the
    # highest probability
    prob = probs[0][predicted.item()]

    if (
        prob.item() > threshold
    ):  # we check if the highest probability is greater than our threshold
        for intent in intents["intents"]:
            # we check if the tag we have is equal to a tag key, this can also be written as tag in intent["tag"]
            # although intent["tag"] is a string, that's why it's more reasonable to write it as written below
            if tag == intent["tag"]:
                selected_response = random.choice(
                    intent["responses"]
                )  # we return a random response

                # Extract the text and link (if available) from the selected response
                response_text = selected_response["text"]
                link = selected_response.get("link")

                # Build the final response with or without a link
                if link:
                    response_with_link = f'{response_text} <a href="{link}" target="_blank">here</a>.'
                    return response_with_link
                else:
                    return response_text
    else:
        return "Sorry, but I do not understand..."
