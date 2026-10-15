from pathlib import Path
from datasets import load_dataset

data_dir = Path(__file__).resolve().parent.parent / "data"

stream = load_dataset(
    "parquet",
    data_files=str(data_dir / "mrpc_train.parquet"),
    split="train",
    streaming=True,
)

print("数据类型：", type(stream).__name__)

for i, sample in enumerate(stream.take(5), start=1):
    print(f"\n第P{i}个样本：")
    print("句子1：", sample["sentence1"])
    print("句子2：", sample["sentence2"])
    print("标签：", sample["label"])
