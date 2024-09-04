import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def cosine_series(x, n):
    cosine_sum = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        cosine_sum += term
    return cosine_sum


x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms to use in the series: "))

if n > 0:
    result = cosine_series(x, n)
    print(f"The computed value of cos({x}) using {n} terms is: {result}")
    print(f"The value of cos({x}) using math.cos is: {math.cos(x)}")
else:
    print("Please enter a positive integer for the number of terms.")
