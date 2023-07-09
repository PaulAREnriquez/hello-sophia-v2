import json
from nltk_utils import lemma, tokenize, bag_of_words
import numpy as np

from model import ChatNet

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

with open('./data/intents.json', 'r') as data:
    intents = json.load(data)


all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w) # we use extend here because w is a list, and we don't want to have a list of lists but a list of words instead
        xy.append((w, tag))

ignore_punctuations = ['?','.',';',',','!']

all_words = [lemma(words) for words in all_words if words not in ignore_punctuations]
#print(all_words)

# we make it a set so we will have a unique set of words
# then we use sorted() to make it a sorted list
all_words = sorted(set(all_words))

# we make it a set so we will have a unique set of words
# then we use sorted() to make it a sorted list
tags = sorted(set(tags))
#print(tags)

X_train = []
y_train = []
for pattern_sentence, tag in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    # .index() returns the index of the tag in tags
    # if the tag appears more than once, the index of the first occurence of the tag
    # will be used
    # This is the same as TargetEncoding
    # for multi-class classification
    # We do not want to onehot encode because we will be using
    # CrossEntropyLoss as our loss function
    # and it accepts just a single number not an array as the target
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):

    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.n_samples
    
output_size = len(tags)
input_size = len(X_train[0])
hidden_layer_size = 8

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = ChatNet(input_size=input_size,hidden_layer_size=hidden_layer_size, num_classes=output_size).to(device)


#Hyperparameters
batch_size = 8
learning_rate = 3e-3
num_epochs = 1000
# loss and optimizer parameters
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)


# training loop

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(dtype=torch.float).to(device) # REMEMBER TO CONVERT IT TO FLOAT TENSOR
        labels = labels.to(dtype=torch.long).to(device) # REMEMBER TO CONVERT IT TO LONG TENSOR

        # forward pass
        outputs = model.forward(words)
        # if y is onehot-encoded, we must apply
        # labels = torch.max(labels,1)[1]


        # loss
        loss = criterion(outputs, labels)
        

        # backward pass and optimizer step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch +1)%100 == 0:
        print(f"epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}")

print(f"Final loss, loss={loss.item():.4f}")

# Saving the model
data = {
    "model_state":model.state_dict(),
    "input_size": input_size,
    "hidden_layer_size": hidden_layer_size,
    "output_size": output_size,
    "all_words": all_words,
    "tags": tags,
}

file = "data.pth"
torch.save(data, file)
print(f"Training complete. File saved to: {file}")