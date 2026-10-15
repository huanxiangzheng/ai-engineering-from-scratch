from pathlib import Path
from datasets import load_dataset

dataset = load_dataset("nyu-mll/glue", "mrpc")
print(dataset)

train_dataset = dataset["train"]
print("训练集样本数：", len(train_dataset))


for i in range(5):
    sample = train_dataset[i]
    print(f"\n第P{i + 1}个样本：")
    print("句子1：", sample["sentence1"])
    print("句子2：", sample["sentence2"])
    print("标签：", sample["label"])

data_dir = Path(__file__).resolve().parent.parent / "data"
data_dir.mkdir(parents=True, exist_ok=True)


csv_path = data_dir / "mrpc_train.csv"
parquet_path = data_dir / "mrpc_train.parquet"

train_dataset.to_csv(str(csv_path), index=False)
train_dataset.to_parquet(str(parquet_path))

csv_size = csv_path.stat().st_size
parquet_size = parquet_path.stat().st_size

print("保存目录：", data_dir)
print("CSV文件大小：", csv_size, "字节")
print("Parquet文件大小：", parquet_size, "字节")

csv_copy =load_dataset(
    "csv", data_files=str(csv_path), split="train"
)
parquet_copy = load_dataset(
    "parquet", data_files=str(parquet_path), split="train"
)

print("CSV 数据内容一致：", csv_copy[:] == train_dataset[:])
print("Parquet 数据内容一致：", parquet_copy[:] == train_dataset[:])