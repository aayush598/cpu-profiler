# core/psutil_monitor.py

import psutil
import os

def get_cpu_memory_stats():
    process = psutil.Process(os.getpid())

    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),  # system-wide CPU %
        "memory_percent": process.memory_percent(),       # memory usage by this process
        "num_threads": process.num_threads(),             # threads in this process
    }
