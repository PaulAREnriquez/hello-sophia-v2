import torch
import torch.nn as nn

class ChatNet(nn.Module):

    def __init__(self,input_size, hidden_layer_size, num_classes):
        
        super(ChatNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_layer_size)
        self.l2 = nn.Linear(hidden_layer_size, hidden_layer_size)
        self.l3 = nn.Linear(hidden_layer_size, num_classes)

        # activation
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)

        out = self.l2(out)
        out = self.relu(out)

        out = self.l3(out)
    
        return out