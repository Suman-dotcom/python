def add_matrices(matrix1, matrix2):
    """
    Add two 2-dimensional matrices.
    
    Parameters:
    matrix1 (list of list of int): The first matrix
    matrix2 (list of list of int): The second matrix
    
    Returns:
    list of list of int: The result of adding matrix1 and matrix2
    """
    # Get the number of rows and columns from the first matrix
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Add corresponding elements of matrix1 and matrix2
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

def print_matrix(matrix):
    """
    Print a 2-dimensional matrix.
    
    Parameters:
    matrix (list of list of int): The matrix to print
    """
    for row in matrix:
        print(" ".join(map(str, row)))

# Example Usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Calculate the sum of the matrices
sum_matrix = add_matrices(matrix1, matrix2)

# Print the resulting matrix
print("Sum of the two matrices:")
print_matrix(sum_matrix)
