def calculate_sum_and_average(arr):
    """
    Calculate the sum and average of an integer array.
    
    Parameters:
    arr (list): A list of integers
    
    Returns:
    tuple: A tuple containing the sum and average of the array
    """
    if not arr:
        return (0, 0)  # Handle empty array case
    
    total_sum = sum(arr)
    average = total_sum / len(arr)
    
    return total_sum, average

# Example Usage:
# Define an integer array
array = [10, 20, 30, 40, 50]

# Calculate sum and average
total_sum, average = calculate_sum_and_average(array)

# Print results
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
