def find_median(numbers):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate the median
    if n % 2 == 0:
        # If even number of elements, the median is the average of the two middle elements
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        # If odd number of elements, the median is the middle element
        median = sorted_numbers[n//2]
    
    return median

# Example Usage:
numbers = [12, 7, 3, 1, 8, 9, 5]

median = find_median(numbers)
print(f"The median of the list is: {median}")
