class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


customer1 = BankAccount("John")
print(f'{customer1.owner}\'s balance is {customer1.balance}')
print(customer1.withdraw(100))
print(customer1.deposit(200))
