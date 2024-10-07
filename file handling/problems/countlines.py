# Program to count the number of lines in file

file = open('poetry.txt', 'r')

line_count = 0

for line in file:
    line_count += 1

print(f"Total number of lines: {line_count}")

file.close()
