MOD = 1000000007

# Function to calculate a^b under modulo MOD using binary exponentiation
def power(a, b):
    # If b = 0, whatever be the value of a, our result will be 1.
    res = 1
    while b > 0:
        # If b is an odd number, then (a^b) = (a * (a^(b–1)/2)^2)
        if b & 1:
            res = (res * a) % MOD
        # If b is an even number, then (a^b) = ((a^2)^(b/2))
        a = (a * a) % MOD
        b >>= 1
    return res

# Function to check if a number is good
def check(N, A, B):
    while N:
        # If any digit is neither A nor B, the number is not valid
        if N % 10 != A and N % 10 != B:
            return False
        N //= 10
    # All digits are either A or B
    return True

def excellentno(A, B, N):
    fact = [0] * (N + 1)
    inv = [0] * (N + 1)
    fact[0] = inv[0] = 1

    # Precompute factorials and their inverses
    for i in range(1, N + 1):
        # Compute factorial
        fact[i] = (fact[i - 1] * i) % MOD

        # Compute inverse factorial
        inv[i] = power(fact[i], MOD - 2)

    ans = 0
    for i in range(N + 1):
        # If the sum of digits is a good number, add the count to the answer
        if check(A * i + B * (N - i), A, B):
            # Total combinations = N! / (i!(N-i)!) = N! * inv[i] * inv[N-i]
            ans = (ans + (fact[N] * inv[i] % MOD * inv[N - i] % MOD)) % MOD

    return ans

# Example 1
A, B, N = 1, 2, 2
print(excellentno(A, B, N))

# Example 2
A, B, N = 2, 4, 6
print(excellentno(A, B, N))
