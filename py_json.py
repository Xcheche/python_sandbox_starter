# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json
# sample json
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'
# parse json to dictionary
user = json.loads(userJSON)
print(user)
print(user['age'])
# dictionary to json
car = {'name': 'Fer', 'year': 2018}
carJSON = json.dumps(car)
print(carJSON)
