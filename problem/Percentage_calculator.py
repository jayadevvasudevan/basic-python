print("Percentage calculator")
Totalmarks=int(input("Enter Total marks:"))
Totalgainedmarks=int(input("Enter Total gained marks:"))
Percentage=(Totalgainedmarks/Totalmarks)*100
print("Percentage:",Percentage)
if(Percentage>=90):
    print("1st division(merit)")
elif(Percentage>=80):
    print("1st division")
elif(Percentage>=60):
    print("2nd division")
else:
    print("3rd division")
