def fibonacci_sequence(num_terms):

    fib_sequence = [0, 1]

    for i in range(2, num_terms):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))

if num_terms <= 0:
    print("Number of terms should be greater than zero.")
else:
    result = fibonacci_sequence(num_terms)
    print(f"The Fibonacci sequence up to {num_terms} terms is:")
    print(result)
