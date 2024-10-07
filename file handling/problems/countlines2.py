# count the number of lines from a text file which is not starting with a specific alphabet.
def count_lines():
    f = open("poetry.txt", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        if not line.lstrip().startswith("t"):
            count+=1
    f.close()
    return count

print(count_lines())