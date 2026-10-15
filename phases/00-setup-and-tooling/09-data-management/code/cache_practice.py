from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    filename="config.json",
    endpoint="https://hf-mirror.com",
    token=False,
)

print("缓存位置：", file_path)

cached_path = hf_hub_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    filename="config.json",
    endpoint="https://hf-mirror.com",
    token=False,
    local_files_only=True,
)

print("本地缓存路径一致：",cached_path == file_path)
