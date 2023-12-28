try:
    x = int(input('Enter a number: '))
    print(x)
except ValueError:
    print('Something went wrong....')
else:
    print('Nothing went wrong...')

finally:
    print('Try except is done...')
