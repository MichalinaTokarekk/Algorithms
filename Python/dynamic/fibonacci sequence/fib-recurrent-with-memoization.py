def fibonacci2(n, memo=None):
    if memo is None:
        memo = {1: 1, 2: 1}
    if n in memo:
        return memo[n]
    memo[n] = fibonacci2(n - 1, memo) + fibonacci2(n - 2, memo)
    return memo[n]

print(f"Wynik dla n = 1: {fibonacci2(1)}")
print(f"Wynik dla n = 2: {fibonacci2(2)}")
print(f"Wynik dla n = 5: {fibonacci2(5)}")
print(f"Wynik dla n = 35: {fibonacci2(35)}")
print(f"Wynik dla n = 100: {fibonacci2(100)}")
