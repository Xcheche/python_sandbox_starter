# counter = 0

# while counter <= 20:
#     print('counter', counter)
#     counter += 1

fruit = []

while True:
    user_input = input('Enter a fruit (or type "stop" to finish): ')

    if user_input.lower() == 'stop':
        break  # Exit the loop if the user types "stop"

    fruit.append(user_input)

print('List of fruits:', fruit)
