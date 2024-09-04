# program to find the sum of diagonal elements in a 2D array.
def sum_of_diagonals(matrix):
    if not matrix or not matrix[0]:
        raise ValueError("Matrix is empty")
    
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]
    
    return primary_diagonal_sum, secondary_diagonal_sum

# Example Usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Calculate the sum of the diagonals
    primary_sum, secondary_sum = sum_of_diagonals(matrix)

    # Print the results
    print(f"Sum of the primary diagonal: {primary_sum}")
    print(f"Sum of the secondary diagonal: {secondary_sum}")
