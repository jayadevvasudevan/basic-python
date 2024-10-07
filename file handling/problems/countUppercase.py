# Program to count uppercase characters in a text file

def count_upper():
    f = open("article.txt", "r")
    content = f.read()
    count = 0
    for char in content:
        if char.isupper():
            count+=1
    return count

print(count_upper())