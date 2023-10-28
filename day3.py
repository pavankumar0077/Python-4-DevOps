# Open the file and it is in read mode
file = open('day3.txt', 'r')
# file = open('day3.txt', 'w')
# file = open('day3.txt', 'a')

# Reading the whole file
content = file.read()
# print(content)

# Read only 1st line Ex: My name is Pavan.
# line = file.readline()
# print(line)

# Read multiple lines list line Ex: ['My name is Pavan.\n', 'I am working at IDRBT']
# lines = file.readlines()
# print(lines)

# Close the file
# file.close

# Write to the file
# file.write("I am working in RBI\n")

# DIfference b/w write mode and append mode is
# Write will overwrite the file
# Append mode will append to the existing content

# Write to the file using appending -- adding in the end fo the file
# file.write("I am working in RBI\n")
print(content)
file.close
