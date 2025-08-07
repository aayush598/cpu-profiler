import argparse
import os

from core.psutil_monitor import get_cpu_memory_stats
from core.perf_wrapper import run_perf
from core.timing import time_block
from utils.logger import save_report
from utils.parser import parse_perf_output
from core.thermal_monitor import read_temperature_sensors
from core.power_monitor import read_hwmon_power

def run_code_from_file(filepath: str, block_name="SCRIPT", output_path=None):
    if not os.path.isfile(filepath):
        print(f"❌ File not found: {filepath}")
        return

    print(f"▶ Running script: {filepath}")
    with open(filepath, "r") as f:
        code = f.read()

    # Execute and time
    with time_block(block_name):
        exec(code, globals())

    print("✅ Script executed successfully.")
    
    # System metrics
    sys_stats = get_cpu_memory_stats()

    # Perf metrics
    print("📊 Collecting performance metrics...")
    perf_raw = run_perf(code)
    perf_parsed = parse_perf_output(perf_raw)

    # Inside report generation
    temperatures = read_temperature_sensors()

    # Power metrics
    hwmon_power = read_hwmon_power()

    # Save report
    report = {
        "source_file": filepath,
        "system_stats": sys_stats,
        "perf_stats": perf_parsed,
        "raw_perf_output": perf_raw,
        "temperatures": temperatures,
        "hwmon_power": hwmon_power
    }

    save_report(report, filename=output_path)
    print(f"📁 Report saved to: {output_path or 'default location'}")


def get_input(prompt, required=True, default=None):
    while True:
        value = input(f"{prompt} " + (f"[default: {default}] " if default else ""))
        if value.strip() == "" and default is not None:
            return default
        elif value.strip() != "":
            return value
        elif not required:
            return None
        else:
            print("⚠ Please enter a valid value.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Profile a Python script using CPU and perf stats.")
    parser.add_argument("--file", type=str, help="Path to the Python file to profile")
    parser.add_argument("--name", type=str, help="Label for profiling block", default="PROFILED_SCRIPT")
    parser.add_argument("--output", type=str, help="Destination path for the JSON report")

    args = parser.parse_args()

    # Interactive fallback if not all arguments are provided
    filepath = args.file or get_input("Enter the path to the Python file to profile:")
    name = args.name or get_input("Enter a name/label for this profiling session:", default="PROFILED_SCRIPT")
    output = args.output or get_input("Enter output path for the report (leave empty for default):", required=False)

    run_code_from_file(filepath, name, output)
