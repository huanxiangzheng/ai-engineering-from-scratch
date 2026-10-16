import torch


def show_memory(stage):
    torch.cuda.synchronize()
    allocated = torch.cuda.memory_allocated() / 1024 **2
    reserved = torch.cuda.memory_reserved() / 1024 **2
    print(
        f"{stage}: allocated={allocated:.1f} MiB,"
        f" reserved={reserved:.1f} MiB"
    )

show_memory("创建前")

x = torch.zeros((4096, 4096), dtype=torch.float32, device="cuda")
show_memory("创建后")

del x
show_memory("删除后")
torch.cuda.empty_cache()
show_memory("清理缓存后")
        