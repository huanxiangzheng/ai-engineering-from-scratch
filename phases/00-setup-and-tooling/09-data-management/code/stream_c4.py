import os
from time import perf_counter

os.environ.pop("HF_ENDPOINT", None)
os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] = "1"

from datasets import load_dataset

print("正在准备 C4 数据集...")

url = (
    "https://hf-mirror.com/datasets/allenai/c4/resolve/main/"
    "en/c4-train.00000-of-01024.json.gz"
)

print("正在读取文件：", url)

stream = load_dataset(
    "json",
    data_files={"train": url},
    split="train",
    streaming=True,
)


iterator = iter(stream)
first_example = next(iterator)

print("第一条数据：", first_example["text"][:80])

start = perf_counter()
count = 0

for example in iterator:
    count += 1
    if perf_counter() - start >= 10:
        break
elapsed = perf_counter() - start

print(f"读取条数:{count}")
print(f"耗时:{elapsed:.2f}秒")
print(f"平均每秒读取条数:{count/elapsed:.2f}")
