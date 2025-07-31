from core.perf_wrapper import run_perf

code = """
x = 0
for i in range(1000000):
    x += i * i
"""

print("\n[ PERF STATS ]")
print(run_perf(code))
