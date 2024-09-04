# program to find the range of a 1D array.
def find_range(arr):
    """
    Find the range of a 1-dimensional array.
    
    Parameters:
    arr (list of int): The array for which to find the range
    
    Returns:
    int: The range of the array
    """
    if not arr:
        raise ValueError("Array is empty. Range cannot be computed.")
    
    # Compute the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)
    
    # Compute the range
    range_val = max_val - min_val
    
    return range_val

# Example Usage:
if __name__ == "__main__":
    array = [10, 2, 38, 23, 38, 23, 17]

    # Find the range of the array
    range_val = find_range(array)

    # Print the result
    print(f"Range of the array: {range_val}")
