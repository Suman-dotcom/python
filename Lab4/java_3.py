def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_euler(n_terms):
    e = 1
    for i in range(1, n_terms):
        e += 1 / factorial(i)
    return e

# Example Usage:
n_terms = 10  # Number of terms in the series
euler_number = compute_euler(n_terms)
print(f"The approximate value of Euler's number with {n_terms} terms is: {euler_number:.10f}")
