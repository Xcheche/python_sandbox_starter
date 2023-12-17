# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# lambda function
def greeting(name):
    print(f"Hello {name}")


greeting("Cheche")

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


def get_sum(num1, num2):
    return num1 + num2


print(get_sum(2, 3))


def greeting1():
    name = input('Enter your name: ')
    return f"Hello {name}"


response = greeting1()
print(response)
