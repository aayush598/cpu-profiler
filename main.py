from core.timing import time_block
from core.psutil_monitor import get_cpu_memory_stats

def test_heavy_operation():
    x = 0
    for i in range(10_000_000):
        x += i * i
    return x

if __name__ == "__main__":
    with time_block("Heavy Operation"):
        result = test_heavy_operation()

    stats = get_cpu_memory_stats()
    print("CPU Usage     :", stats["cpu_percent"], "%")
    print("Memory Usage  :", round(stats["memory_percent"], 2), "%")
    print("Threads Used  :", stats["num_threads"])
