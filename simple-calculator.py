num1 = int(input('Enter first number:\n'))
num2 = int(input('Enter second number:\n'))
op = input('Enter operator:\n')

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)

elif op == '%':
    print(num1 % num2)
elif op == 'sqrt':
    print(num1 ** 0.5)
else:
    print('Invalid operator')
