def is_multiple(m, n):
    """
    Check if m is a multiple of n.
    
    Parameters:
    m (int): The number to check
    n (int): The number to divide by
    
    Returns:
    bool: True if m is a multiple of n, False otherwise
    """
    return m % n == 0

# Read two integers from the user
try:
    m = int(input("Enter the value of m: "))
    n = int(input("Enter the value of n: "))

    # Ensure that n is not zero to avoid division by zero error
    if n == 0:
        print("n cannot be zero. Please enter a non-zero integer for n.")
    else:
        # Check and print whether m is a multiple of n
        if is_multiple(m, n):
            print(f"{m} is a multiple of {n}.")
        else:
            print(f"{m} is not a multiple of {n}.")
except ValueError:
    print("Please enter valid integer values for both m and n.")
