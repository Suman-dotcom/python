# Reverse the elements in an array of integers without using a second array.
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Move the pointers towards the center
        left += 1
        right -= 1

# Example Usage:
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    
    print("Original array:", array)
    
    # Reverse the array
    reverse_array(array)
    
    print("Reversed array:", array)
