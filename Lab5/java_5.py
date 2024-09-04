# program to search an element in an array.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example Usage:
if __name__ == "__main__":
    # Array and target element
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 70

    # Linear search
    linear_index = linear_search(array, target)
    if linear_index != -1:
        print(f"Linear Search: Element {target} found at index {linear_index}.")
    else:
        print(f"Linear Search: Element {target} not found.")

    # Binary search (array must be sorted)
    binary_index = binary_search(array, target)
    if binary_index != -1:
        print(f"Binary Search: Element {target} found at index {binary_index}.")
    else:
        print(f"Binary Search: Element {target} not found.")
