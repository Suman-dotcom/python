# program to enter n elements in an array and find smallest number among them.
def find_smallest_number(arr):
    if not arr:
        raise ValueError("Array is empty. Cannot find the smallest number.")
    
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    
    return smallest

# Example Usage:
if __name__ == "__main__":
    # Enter number of elements
    n = int(input("Enter the number of elements in the array: "))
    
    # Initialize an empty array
    array = []
    
    # Enter n elements
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        array.append(element)
    
    # Find the smallest number
    smallest_number = find_smallest_number(array)
    
    # Print the result
    print(f"The smallest number in the array is: {smallest_number}")
