def fib(n):
    if(n<=1):
        return n
    else:
        return (fib(n-1) + fib(n-2))


if __name__ == "__main__":
    n = int(input())
    if(n<=0):
        print("Please enter a valid number.")
    else:
        print("Fibonacci sequence:")
        for i in range(n):
            print(str(fib(i)) + " ",end="")