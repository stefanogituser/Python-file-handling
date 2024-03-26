# Open a file for writing and insert 3 records
f = open('my_file.txt', 'w')
f.write('mix3 them gathe8 the3\n')
f.write('77777777777771111111111199999999999universe\n')
f.write('fil3 h8ndlin3r\n')
f.close()    # Always close the file
# Check the contents of the file created


# Open the file for reading and read the entire file via read()


f = open('my_file.txt', 'r')
print("=====Entire file read into a string=======")
f.read()              # Read entire file into a string

f.close()

# Read line-by-line using readline() in a while-loop
f = open('my_file.txt')
line = f.readline()   # include newline
while line:
    line = line.rstrip()  # strip trailing spaces and newline
        # process the line
    line = f.readline()
    print(line)


# Open the file in append mode and add 3 lines

file = open('my_file.txt', 'a') # Open a file in append mode
file.write('Mary had a little boy\n') # Line 1
file.write('Roses are red violets are blue\n') # Line 2
file.write('Last line appended to end of file\n') # Line 3

# Display contents of my file after append.
line = f.readline()   # include newline
while line:
    line = line.rstrip()  # strip trailing spaces and newline
    # process the line
    line = f.readline()
    print(line)



# Using error handling techniques to handle file is python
try:
    f = open("my_file.txt", "r")
except IOError:    #This error means that the file does not exist or any other error related to input and output
    print( "File not found")
else:
    f.close()


# Open the file
file = open('my_file.txt', 'r')

# Read the file
content = file.read()

# Print the contents of all file operations above
print("========The entire file=========")
print(content)

# Close the file
file.close()