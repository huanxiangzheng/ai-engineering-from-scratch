from line_profiler import profile
import time
@profile
def load_data() -> list[int]:
    time.sleep(0.3)
    return list(range(500_000))

@profile
def process_data(data: list[int]) -> list[int]:
    return [value * value for value in data]


def main() -> None:
    start = time.perf_counter()

    data = load_data()
    after_load = time.perf_counter()

    _result = process_data(data)
    after_process = time.perf_counter()

    print(f"读取数据用时：{after_load - start:.4f} 秒")
    print(f"处理数据用时：{after_process - after_load:.4f} 秒")


if __name__ == "__main__":
    main()
