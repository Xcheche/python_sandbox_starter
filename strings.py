# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Cheche'
age = 31
job = 'software developer'

# String Formatting
print('My name is {}. I am {} years old . and a {} proffessional'.format(name, age, job))
# String MethodsJ

greeting = ' hello world!'
# Capitalize string first letters only
print(greeting.capitalize())

# Make all uppercase
print(greeting.upper())

# replace all instances of word
print(greeting.replace('world', 'goodbye!'))
