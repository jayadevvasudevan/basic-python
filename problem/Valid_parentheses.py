#function to print all the valid parenthesis
#using recursion
def printValidPar(left, right, out):
  if right==0:
    return
 
  elif left==0:
    print(out+right*" )")
 
 # you can adjust Space Between parentheses accordingly
  elif left==right:
    printValidPar(left-1, right, out+" (") 
 
  else:
    printValidPar(left-1, right, out+" (") 
    printValidPar(left, right-1, out+" )") 
 
 
#driver function
def validPar(n):
  printValidPar(n,n,"")
 
n=int(input("Enter Number of parentheses you want to generate : \n "))
validPar(n)