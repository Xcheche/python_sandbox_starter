# Python has functions for creating, reading, updating, and deleting files.
# open file
myfile = open("cheche.txt", "w")

# print('name: ', myfile.name)
# print('closed: ', myfile.closed)
# print('opening mode: ', myfile.mode)


# writing to file
myfile.write("This is some text that will be written to the file.")


# continuos writing to file
myfile.write("i love python.")


# close the file
myfile.close()

# append even when closed

myfile = open("cheche.txt", "a")
myfile.write("i love javascript also.")
myfile.close()


# reading from file
myfile = open("cheche.txt", "r+")
text = myfile.read(100)
print(text)
