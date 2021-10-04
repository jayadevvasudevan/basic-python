#binary to decimal

bi = int(input("Enter binary number: "))

ans = 0
i = 0
while (bi>0):
    temp = bi%10
    ans = ans + temp*(1<<i)
    i += 1
    bi = bi//10

print("Decimal number: ", ans)
