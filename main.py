import argparse
import os

from core.psutil_monitor import get_cpu_memory_stats
from core.perf_wrapper import run_perf
from core.timing import time_block
from utils.logger import save_report
from utils.parser import parse_perf_output
from core.thermal_monitor import read_temperature_sensors

def run_code_from_file(filepath: str, block_name="SCRIPT"):
    if not os.path.isfile(filepath):
        print(f"❌ File not found: {filepath}")
        return

    with open(filepath, "r") as f:
        code = f.read()

    # Execute and time
    with time_block(block_name):
        exec(code, globals())

    # System metrics
    sys_stats = get_cpu_memory_stats()

    # Perf metrics
    perf_raw = run_perf(code)
    perf_parsed = parse_perf_output(perf_raw)

    # Inside report generation
    temperatures = read_temperature_sensors()

    # Save report
    report = {
        "source_file": filepath,
        "system_stats": sys_stats,
        "perf_stats": perf_parsed,
        "raw_perf_output": perf_raw,
        "temperatures": temperatures
    }

    save_report(report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Profile a Python script using CPU and perf stats.")
    parser.add_argument("--file", type=str, help="Path to the Python file to profile", required=True)
    parser.add_argument("--name", type=str, help="Label for profiling block", default="PROFILED_SCRIPT")

    args = parser.parse_args()
    run_code_from_file(args.file, args.name)
