def print_pattern(rows):
    """
    Print the specified pattern with the given number of rows.
    
    Parameters:
    rows (int): Number of rows in the pattern
    """
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (2 * (i - 1)), end="")

        # Print the first number
        print(i, end="")

        # Print internal spaces between the numbers
        if i != rows:
            print(" " * (2 * (rows - i) - 1), end="")

            # Print the second number
            print(i, end="")

        # Move to the next line after each row
        print()

# Example Usage:
print_pattern(4)
