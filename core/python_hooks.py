import inspect
import textwrap
from functools import wraps

from core.timing import time_block
from core.psutil_monitor import get_cpu_memory_stats
from core.perf_wrapper import run_perf
from utils.logger import save_report

def profile_function(name="PROFILED_FUNCTION"):
    
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # === 1. Time block ===
            with time_block(name):
                result = fn(*args, **kwargs)

            # === 2. System metrics ===
            sys_stats = get_cpu_memory_stats()

            # === 3. Perf metrics ===
            source_lines = inspect.getsource(fn)
            code = textwrap.dedent("\n".join(source_lines.splitlines()[1:]))  # remove decorator line
            perf_output = run_perf(code)

            # === 4. Aggregate and save ===
            report_data = {
                "function": fn.__name__,
                "system_stats": sys_stats,
                "perf_output": perf_output
            }

            save_report(report_data)
            return result
        return wrapper
    return decorator
