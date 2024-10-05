# Program to count the number of occurences of a word from a file

def count_occurences(word):
    f = open("poetry.txt", "r")
    lines = f.read()
    print(lines.lower().count(word))

count_occurences("the")