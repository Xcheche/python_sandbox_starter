class Instructor:

    def __init__(self, name, age, sex, followers=0):

        self.name = name
        self.age = age
        self.sex = sex
        self.followers = followers

    def birthday(self):
        self.age += 1

    def teach(self, subject):
        print(f'i love {self.teach} and i teach {subject}')

    def __str__(self):
        return f'{self.name} {self.age} {self.sex}'


instructor1 = Instructor(name='Cheche', age=40, sex='male', followers=3)
print(instructor1.age)
instructor1.birthday()
print(instructor1.age)
instructor1.teach('physics')
print(instructor1.followers)
