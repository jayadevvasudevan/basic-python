# Input test case (T)
print("Input test case: ")
t = int(input())

while(t>0):
  t=t-1

  # Input value of m and k 
  print("Input value of m and k: ") 
  m,k=list(map(int,input().split()))

  # Input array elements
  print("Input array elements: ")
  arr=list(map(int,input().split()))

  # Store first value
  res=arr[0]
  for i in range(1,m):
    # Perform the bitwise XOR operation 
    # on elements in array
    res=res^arr[i]

  # print the result
  print("Result is: ")
  print(k^res)
