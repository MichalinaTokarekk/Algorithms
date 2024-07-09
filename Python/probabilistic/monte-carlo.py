import random

def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 0.5**2:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

# Przykład użycia
num_samples = 1000000
pi_estimate = monte_carlo_pi(num_samples)
print(f"Monte Carlo Algorithm - Approximation of Pi: {pi_estimate}")
