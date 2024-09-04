def compute_series_sum(n):
    series_sum = 0
    for i in range(1, n + 1):
        term = (-1) ** (i + 1) / i
        series_sum += term
    return series_sum

n = int(input("Enter a positive integer n: "))
if n > 0:
    result = compute_series_sum(n)
    print(f"The sum of the series up to {n} terms is: {result}")
else:
    print("Please enter a positive integer.")