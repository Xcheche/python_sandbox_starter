# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    # construction below
    # self is a keyword that refers to the current instance of the class
    race = 'human'

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# inheriting class user


class Customer(User):
    # constructing below
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


person1 = User('cheche', '@cheche', 31)
person1.race = 'alien'
print(f'{person1.name} {person1.email} {person1.age} and of {person1.race}')
person1.has_birthday()

print(person1.greeting())
print('----------------------')
person2 = User('ebuka', '@ebuka', 32)
person2.race = 'black'
print(f'{person2.name} {person2.email} {person2.age} and of {person2.race}')
person2.has_birthday()
print(person2.greeting())

print('----------------------')
customer1 = Customer('john', '@john', 34)
customer1.set_balance(500)
print(f'{customer1.name} {customer1.email} {customer1.age} {customer1.balance} and of {customer1.race}')
print(customer1.greeting())
