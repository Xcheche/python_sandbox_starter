person = {'first_name': 'cheche', 'last_name': 'ome', 'age': '31'}

print(person)

# constructor type dictionary
person2 = ({'first_name': 'cheche', 'last_name': 'ome', 'age': '38'})

print(person['first_name'])
print(person['last_name'])
print(person.items())
print(person.values())
print(person2)
print(person2.pop('first_name'))
print(person2.clear())
person3 = person.copy()
print(person3)
print(person3.clear())
