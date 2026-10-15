import os
import json
import urllib.request

from dotenv import load_dotenv

load_dotenv(".env", override=True)

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    base_url=os.environ.get("ANTHROPIC_API_URL"),
    max_retries=0,
)


response = client.messages.create(
    model=os.environ.get("LLM_MODEL"),
    max_tokens=256,
    thinking={"type":"disabled"},
    messages=[{"role": "user", "content": "请用一句话解释什么是神经网络"}]
)

for block in response.content:
    if block.type == "text":
        print(block.text)