import torch

x = torch.randn(32, 784)
weights = torch.randn(784, 128)
output = x @ weights
# output[0, 0] = float("nan")

print("has_nan:", torch.isnan(output).any().item())
if torch.isnan(output).any().item():
    breakpoint()

print("程序运行结束")
