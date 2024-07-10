def fibonacci3(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b

print(f"Wynik dla n = 1: {fibonacci3(1)}")
print(f"Wynik dla n = 2: {fibonacci3(2)}")
print(f"Wynik dla n = 5: {fibonacci3(5)}")
print(f"Wynik dla n = 35: {fibonacci3(35)}")
print(f"Wynik dla n = 100: {fibonacci3(100)}")
