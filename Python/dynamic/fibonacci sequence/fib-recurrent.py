def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"n=1: {fibonacci(1)}")
print(f"n=2: {fibonacci(2)}")
print(f"n=5: {fibonacci(5)}")
print(f"n=35: {fibonacci(35)}")
# print(f"n=100: {fibonacci(100)}")  # To będzie bardzo wolne ze względu na rekurencyjny charakter
