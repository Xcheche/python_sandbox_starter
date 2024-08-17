# def greet(name):
#     print(f'Good morning!{name}\n')


# name = input('What is  your name:\n')


# greet(name)

# name = """
# Good morning!John
# Tell me my name?
# Im 32 years old.
# How old are you?
# """
# print(name)


def add_num(a, b):
    sum = a + b
    return sum


a = int(input("Enter first number: \n"))
b = int(input("Enter second number:\n "))
print("Adding two numbers...\n")
print("The sum is: \n")
print(add_num(a, b))
