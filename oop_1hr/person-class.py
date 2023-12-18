class Person:
    # constructor
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status

    def isolder(self):
        if self.age > 30:
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def birthday(self):
        self.age += 2

    def ismarried(self):
        if self.status == 'married':
            return True
        else:
            return False
        # class inheritance below


class Staff(Person):
    # constructor below
    def __init__(self, name, age, job):
        super().__init__(name, age, 'single')
        self.job = job


person1 = Person('Cheche', 31, 'married')

print(person1.isolder())
print(person1.get_name())
person1.birthday()
print(person1.age)
print(person1.ismarried())

print('---------------------------------')
person2 = Person('John', 30, 'single')
print(person2.ismarried())
print(person2.get_name())
person2.birthday()
print(person2.age)
print(person2.birthday())

print('---------------------------------')

staff1 = Staff('Cheche', 31, 'software developer')
staff1.birthday()
print(staff1.age)
print(staff1.isolder)
print(staff1.get_name())
print(staff1.ismarried)
