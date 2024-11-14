# model/recommendation_model.py
import torch
import torch.nn as nn

class MenuRecommendationNet(nn.Module):
    def __init__(self, input_size):
        super(MenuRecommendationNet, self).__init__()
        self.fc1 = nn.Linear(input_size, 16)
        self.fc2 = nn.Linear(16, 32)
        self.fc3 = nn.Linear(32, 16)
        self.output = nn.Linear(16, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.sigmoid(self.output(x))
        return x
    
    def initialize_weights(self, preferences):
        for i, weight in enumerate(preferences):
            self.fc1.weight.data[:, i] = weight