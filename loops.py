# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['kate', 'john', 'james', 'anderson']


# While loops execute a set of statements as long as a condition is true.

# for person in people:
#     print('people', person)
#     if person == 'john':
#         break

for x in range(len(people)):
    print(people[x])


# traditional range

for i in range(0, 10, 4):
    print(i)

count = 0

while count <= 10:
    print('count', count)
    count += 1
