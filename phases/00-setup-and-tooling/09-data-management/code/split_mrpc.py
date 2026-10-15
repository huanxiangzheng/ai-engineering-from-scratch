from pathlib import Path
from datasets import load_dataset

data_dir = Path(__file__).resolve().parent.parent / "data"

data = load_dataset(
    "parquet",
    data_files=str(data_dir / "mrpc_train.parquet"),
    split="train",
)

def split_dataset(source, seed):
    first =source.train_test_split(test_size=0.30, seed=seed)
    second = first["test"].train_test_split(test_size=0.50, seed=seed)

    return {
        "train": first["train"],
        "validation": second["train"],
        "test": second["test"]
    }

splits = split_dataset(data, seed=42)
repeat = split_dataset(data, seed=42)

output_dir = data_dir / "splits"
output_dir.mkdir( exist_ok=True)

for name,part in splits.items():
    print(f"{name}:{len(part)}条，占{len(part)/len(data):.2%}")
    print("重复切分内容一致：", part[:] == repeat[name][:])
    part.to_parquet(str(output_dir / f"mrpc_{name}.parquet"))