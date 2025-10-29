# Function to find the factorial of a number
def factorial(n):
    # Base case: the factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)

# Main function to interact with the user
def main():
    # Prompt the user for input
    number = int(input("Enter a number to find its factorial: "))
    
    # Check if the number is non-negative
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Calculate and display the factorial
        print(f"Factorial of {number} is {factorial(number)}")

# Run the main function
if __name__ == "__main__":
    main()
