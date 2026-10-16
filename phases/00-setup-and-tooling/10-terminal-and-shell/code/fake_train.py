import time

for epoch in range(1, 601):
    loss = 1 / epoch
    print(f"Epoch {epoch}, Loss: {loss:.4f}")
    time.sleep(1)
