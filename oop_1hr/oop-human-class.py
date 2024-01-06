class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.sex = sex

    @property
    def age(self):  # getter
        return self._age

    @age.setter
    def age(self, value):  # setter
        self._age = value

    def __str__(self):
        return f'{self.name} {self.age} {self.sex}'

    def eat(self, food):
        print(f'{self.name} is eating {food}')


class Woman(Human):
    def __init__(self, name, age, sex, height):
        self.height = height
        super().__init__(name, age, sex)

    def eat(self, food):
        print(f'{self.name} is cooking {food}')

    def __str__(self):
        return f'{self.name} {self.age} {self.sex} {self.height}'


class Boy(Human):
    def __init__(self, name, age, sex, height, color):
        self.height = height
        self.color = color
        super().__init__(name, age, sex)

    def eat(self, food):
        print(f'{self.name} dosent like cooking {food}')


p1 = Human('Ebuka', 23, 'male')
p1._age = 60
print(p1._age)
print(p1.__str__())
p1.eat('rice')

print('---------------------------------')
w1 = Woman('Cheche', 25, 'female', 5)
print(w1.__str__())
w1.eat('rice')


print('---------------------------------')
b1 = Boy('Cheche', 25, 'male', 5, 'black')
print(b1.__str__())
b1.eat('beans')
b1.age = 30
print(b1.age)
