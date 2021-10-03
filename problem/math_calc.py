import os
import math

os.system("tput setaf 3")
print("\t"+72*"=")
print("\t\t\t\tWelcome To Calculator")
print("\t"+72*"=")
os.system("tput setaf 7")

x1 = input("Press Enter Key to see the Menu : ")

os.system("tput setaf 5")
print("\t\t\t"+15*">" + " Welcome To the Menu " +15*"<")

os.system("tput setaf 4")
print(""" ******************* Below Operation will applied between operators*******************
        \t\tPress + for Addition
        \t\tPress - for Subtraction
        \t\tPress * for Multiplication
        \t\tPress / for Division
        \t\tPress % for Modulus
        \t\tPress sqrt for Square Root
        \t\tPress ^ for a to the Power b""")

os.system("tput setaf 7")

while (True):
    y=input("Do You Want to Continue(yes/no) :")
    
    if y == 'yes':
      a=int(input("Write the First Operator : "))
      b=int(input("Write the Second Operator : "))
      op=input("Write the operation you want to perform :")

      if op == '+':
        print("Result of Addition : ",a+b)

      if op == '-':
        print("Result of Subtraction : ",a-b)

      if op=='*':
        print("Result of Multiplication : ",a*b)

      if op=='/':
        print("Result of Division : ",a/b)

      if op=='%':
        print("Result of Modulus : ",a%b)

      if op=='sqrt':
        print("Sq. Root of a : ",math.sqrt(a))
        print("Sq. Root of b : ",math.sqrt(b))

      if op=='sq':
          n=1
          p=1
          while n<=b:
              p = p*a
              n= n+1
          print("Power of a^b :",p)

   
    if y=='no':
      os._exit(1)




