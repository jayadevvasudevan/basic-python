##############################  <<< Fibonacci Sequence >>> ########################

###############Iterative approach #############

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = 10
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")

###############  Recursive approach  ############

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

###############  Memoization approach (Top-down dynamic programming)  ############

def fibonacci_memo(n, memo={}):
    # Define a function to calculate Fibonacci number using memoization.
    # `n` is the number for which we want to calculate the Fibonacci value.
    # `memo` is a dictionary used to store already computed Fibonacci values.

    if n <= 1:
        # Base case: if n is 0 or 1, return n as the Fibonacci value.
        return n

    if n not in memo:
        # If the Fibonacci value for n is not already computed and stored in `memo`,
        # recursively compute the Fibonacci value for n by calculating the sum of the
        # Fibonacci values of (n-1) and (n-2).
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    # Return the Fibonacci value of n, either from the memo or the computed value.
    return memo[n]

# Example usage:
n = 10
# Generate a list of Fibonacci numbers for the first `n` terms using list comprehension
fib_series = [fibonacci_memo(i) for i in range(n)]

# Print the generated Fibonacci series up to `n` terms
print(f"Fibonacci series using memoization up to {n} terms: {fib_series}")

