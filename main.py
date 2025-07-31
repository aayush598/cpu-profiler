from core.timing import time_block
from core.psutil_monitor import get_cpu_memory_stats
from core.perf_wrapper import run_perf
from utils.logger import save_report

def test_heavy_operation():
    x = 0
    for i in range(10_000_000):
        x += i * i
    return x

if __name__ == "__main__":
    # Time the block
    with time_block("Heavy Operation"):
        result = test_heavy_operation()

    # Collect system metrics
    sys_stats = get_cpu_memory_stats()

    # Collect perf stats
    perf_output = run_perf("""
x = 0
for i in range(10_000_000):
    x += i * i
""")

    # Aggregate all results
    report_data = {
        "result": result,
        "system_stats": sys_stats,
        "perf_output": perf_output,
    }

    # Save to JSON
    save_report(report_data)
