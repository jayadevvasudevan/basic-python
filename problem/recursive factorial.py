n = int(input('Enter number:'))

def Fac(i):
    if i <= 1 :
        return 1

    return i*Fac(i-1)

print(Fac(n))
