def get_fibonacci_sequence(n): 
    if n <= 0: 
        return [] 
    elif n == 1: 
        return [0] 
        
    # Initialize the sequence with the first two terms 
    sequence = [0, 1] 
    
    # Iteratively calculate the next terms 
    for _ in range(2, n): 
        sequence.append(sequence[-1] + sequence[-2]) 
        
    return sequence

# Example usage 
print(get_fibonacci_sequence(8))
