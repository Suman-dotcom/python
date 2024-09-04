def print_pattern(N):
    for i in range(1, N + 1):
        # Print the top dots
        for j in range(N - i):
            print(" ", end="")
        print(".", end="")
        
        # Print the pattern lines
        if i > 1:
            print()
            for j in range(1, i):
                # Print spaces before the slashes
                for k in range(N - i):
                    print(" ", end="")
                # Print the slashes and underscores
                print("/", end="")
                for k in range(2 * j - 1):
                    if j == i - 1:
                        print("_", end="")
                    else:
                        print(" ", end="")
                print("\\", end="")
                print()

# Example usage:
N = int(input("Enter the value of N: "))
print_pattern(N)
