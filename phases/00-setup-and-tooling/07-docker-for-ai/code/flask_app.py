from flask import Flask, jsonify
import torch

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(
        message="Hello from Docker!",
        cuda_available=torch.cuda.is_available()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)