# A List is a collection which is ordered and changeable. Allows duplicate members.
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# general appending

fruits.append('orange')

# specific appending
fruits.insert(1, 'mango')

# removing general
fruits.remove('banana')

# specific position removal
fruits.pop(1)

# fruits reverse

fruits.reverse()

# sorting

fruits.sort()
fruits.sort(reverse=True)

# copy

# fruits2 = fruits.copy()

# clear

# fruits.clear()


print(fruits)
