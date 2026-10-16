import tracemalloc

tracemalloc.start()

small_data = bytearray(1 * 1024 * 1024)  # 1 MB
large_data = bytearray(10 * 1024 * 1024)  # 10 MB

snapshot = tracemalloc.take_snapshot()
stats = snapshot.statistics("lineno")

print("内存分配最多的代码行：")
for stat in stats[:5]:
    print(stat)

tracemalloc.stop()
