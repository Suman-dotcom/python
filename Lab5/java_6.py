# program to find the sum of even numbers in an integer array.
def sum_of_even_numbers(arr):
    total_sum = 0
    for number in arr:
        if number % 2 == 0:
            total_sum += number
    return total_sum

# Example Usage:
if __name__ == "__main__":
    array = [10, 21, 32, 43, 54, 65, 76]

    # Calculate the sum of even numbers
    even_sum = sum_of_even_numbers(array)

    # Print the result
    print(f"Sum of even numbers: {even_sum}")
