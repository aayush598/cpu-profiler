import torch
import torch.nn.functional as F

from core.timing import time_block

input_tensor = torch.randn(1, 3, 64, 64)
weights = torch.randn(16, 3, 3, 3)
bias = torch.randn(16)

with time_block("Conv2D Op"):
    output = F.conv2d(input_tensor, weights, bias, stride=1, padding=1)
