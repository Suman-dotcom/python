# program to find the sum of all odd numbers in a 2D array.
def sum_of_odd_numbers(matrix):
    """
    Calculate the sum of all odd numbers in a 2D array.
    
    Parameters:
    matrix (list of list of int): The 2D array (matrix)
    
    Returns:
    int: The sum of the odd numbers
    """
    total_sum = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:  # Check if the number is odd
                total_sum += num
    return total_sum

# Example Usage:
if __name__ == "__main__":
    # Define a 2D array (matrix)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Calculate the sum of odd numbers
    odd_sum = sum_of_odd_numbers(matrix)
    
    # Print the result
    print(f"Sum of odd numbers in the matrix: {odd_sum}")
