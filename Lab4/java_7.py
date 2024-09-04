def print_pattern():
    current_num = 1
    rows = 3

    for i in range(1, rows + 1):
        for j in range(2 * i - 1):
            print(current_num, end=" ")
            current_num += 1
        print()  # Move to the next line after each row

# Example Usage:
print_pattern()
