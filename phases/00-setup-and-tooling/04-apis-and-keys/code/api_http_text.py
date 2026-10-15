import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv(override=True)

url = os.environ["ANTHROPIC_BASE_URL"].rstrip("/") + "/v1/messages"

headers = {
    "Content-Type": "application/json",
    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
    "anthropic-version": "2023-06-01",
}

payload = {
    "model": os.environ["LLM_MODEL"],
    "max_tokens": 256,
    "thinking":{"type":"disabled"},
    "messages": [
        {
            "role": "user",
            "content": "请用一句话解释什么是神经网络"
        }
    ],
}

body = json.dumps(payload, ensure_ascii=False).encode("utf-8")

request = urllib.request.Request(url, data=body, headers=headers, method="POST")

print("实际请求地址：",url)
print("模型名称：",os.getenv("LLM_MODEL"))

with urllib.request.urlopen(request) as response:
    print("HTTP Status Code:", response.status)
    result = json.loads(response.read())

print(json.dumps(result, ensure_ascii=False, indent=2))

