import time
import torch
x= torch.randn(4096,4096, device='cuda')
torch.cuda.synchronize()

print("阶段一：数据已放入显存，暂停10秒")
time.sleep(10)

print("阶段二：连续计算矩阵乘法20秒")
start = time.perf_counter()

while time.perf_counter() - start <20:
    result = x@x
    torch.cuda.synchronize()

print("阶段三：计算结束，暂停10秒")
time.sleep(10)
