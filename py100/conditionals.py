# Truthy vs. Falsy

# Yes? No? Part 1

import random
random_number = random.randint(0, 1)

if random_number == 1:
    print('Yes!')
else:
    print('No')

# Yes? No? Part 2 (conditional expression)

print('Yes') if random_number else print('No')


# Check the Weather, Part 1

weather = 'state'

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print('Grab your umbrella.')
else:
    print("Let's stay inside.")


# Match-Case

# Check the Weather, Part 2

weather = 'state'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case _:
        print("Let's stay inside.")

# Logical Conditions 1
# Logical Conditions 2
# Logical Conditions 3


# Are we moving?

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)