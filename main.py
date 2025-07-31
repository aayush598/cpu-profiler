from core.python_hooks import profile_function

@profile_function("Heavy Calculation")
def test_heavy_operation():
    x = 0
    for i in range(10_000_000):
        x += i * i
    return x

if __name__ == "__main__":
    result = test_heavy_operation()
    print("Result:", result)
