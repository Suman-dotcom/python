def print_pattern(rows):
    
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i) * 2, end="")

        # Print decreasing numbers
        for j in range(i, 0, -1):
            print(j, end=" ")

        # Print increasing numbers
        for j in range(2, i + 1):
            print(j, end=" ")

        # Move to the next line after each row
        print()

# Example Usage:
print_pattern(4)
