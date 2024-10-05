# Opening a file in read mode ('r')
file = open('sample.txt', 'r')

# read() method gets all the content from the file
content = file.read()

print(content)

# Always close the file after you are done reading
file.close()

######################################################

# Opening a file in write mode ('w')
file = open('output.txt', 'w')

# Use write() method for writing to the file
file.write("Hello, Hacktoberfest 2024!\n")
file.write("Contributing to open-source is fun!")

# Note: Writing to a file replaces all the previous contents in the file and creates a file if it doesn't exist

file.close()

#######################################################

# Opening a file in append mode ('a')
file = open('output.txt', 'a')

file.write("\nAppending more content to this file!")

file.close()

#######################################################

# Using 'with' statement to open the file
with open('sample.txt', 'r') as file:
    # While using 'with' No need to explicitly close the file, 'with' handles that
    content = file.read()
    print(content)

#######################################################

# Reading a file line by line
file = open('sample.txt', 'r')

# Use a loop to iterate through each line in the file
for line in file:
    # Print each line (the newline is automatically added at the end)
    print(line.strip())  # strip() removes extra newline characters

file.close()

#######################################################