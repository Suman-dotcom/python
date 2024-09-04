def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal
def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

# Example Usage:
binary_num = "1010"
decimal_num = 10

# Convert Binary to Decimal
print(f"Binary to Decimal: {binary_num} -> {binary_to_decimal(binary_num)}")

# Convert Decimal to Binary
print(f"Decimal to Binary: {decimal_num} -> {decimal_to_binary(decimal_num)}")
