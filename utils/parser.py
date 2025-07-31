import re

def parse_perf_output(perf_raw: str):
    result = {}
    lines = perf_raw.splitlines()
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2 and parts[0].replace(',', '').isdigit():
            metric = parts[-1]
            value = int(parts[0].replace(',', ''))
            result[metric] = value
    return result
