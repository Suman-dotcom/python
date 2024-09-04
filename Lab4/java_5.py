def generate_combinations():
    numbers = [1, 2, 3]
    
    # Generate combinations of length 1
    for i in numbers:
        print([i])
    
    # Generate combinations of length 2
    for i in numbers:
        for j in numbers:
            print([i, j])
    
    # Generate combinations of length 3
    for i in numbers:
        for j in numbers:
            for k in numbers:
                print([i, j, k])

# Example Usage:
generate_combinations()
