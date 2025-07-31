import time
from contextlib import contextmanager

@contextmanager
def time_block(name="BLOCK"):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    duration = end - start
    print(f"[{name}] Elapsed time: {duration:.6f} seconds")
