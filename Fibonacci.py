# Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = 10
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")


# Fibonacci sequence using recursive function
def fibonacci_recursive(n):
    # Base case: return the value for the first two numbers (0 and 1)
    if n <= 1:
        return n
    else:
        # Recursive case: sum of the two preceding numbers in the sequence
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Get user input for the number of terms in the Fibonacci sequence
n = int(input("\n" + "Enter the number of terms: "))

# Generate the Fibonacci series by calling the recursive function
fib_series = [fibonacci_recursive(i) for i in range(n)]

# Print the generated Fibonacci series
print(f"Fibonacci series up to {n} terms: {fib_series}")

