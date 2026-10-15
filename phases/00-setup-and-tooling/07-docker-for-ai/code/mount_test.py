from pathlib import Path
import torch

x = torch.tensor([1.0, 2.0, 3.0],device="cuda")
result = (x * 3).cpu().tolist()

text = f"GPU: {torch.cuda.get_device_name(0)}\nResult: {result}\n"
Path("/workspace/mopunt_results.txt").write_text(text,encoding="utf-8")
print(text)
