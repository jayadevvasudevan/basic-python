#decimal to binary

num = int(input("Enter number: "))
print("Binary: ", end = '')
s = ""
while num>0:
    dig = num&1
    s = str(dig) + s
    num = num>>1
print(s)
