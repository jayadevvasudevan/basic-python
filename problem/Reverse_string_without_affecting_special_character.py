'''
>>>>   Reverse String Without Affecting Special Characters  <<<<<<

Problem Statement: You have given a string. There can have multiple special characters inside the string.
Write a program to reverse the given string. The position of the special characters should not be changed

Example:

Input: 'abc/defgh$ij'
Output: 'jih/gfedc$ba'

Important : Place of special character not should be change 

'''

strSample=input("Enter String to reverse it (Non Integer) : ")
 
#convert string into list
listSample=list(strSample)
 
i=0
j=len(listSample)-1
 
while i<j:
    if not listSample[i].isalpha():
        i+=1
    elif not listSample[j].isalpha():
        j-=1
    else:
        #swap the element in the list 
        #if both elements are alphabets
        listSample[i], listSample[j]=listSample[j], listSample[i]
        i+=1
        j-=1

#convert list into string 
#by concatinating each element in the list
strOut=''.join(listSample)
print(strOut)