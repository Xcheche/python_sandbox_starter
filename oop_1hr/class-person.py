class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


name = input('Enter name:')
age = int(input('Enter age:'))
p1 = Person(name, age)
p1.birthday()
print(f'{p1.name}\'s age is {p1.age}')
