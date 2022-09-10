# main program is a copy from assignment 5
import random

stop = False
numbers = []

user = input('Anna luku (! merkki arpoo 5 lukua): ')

if user == '!':
    numbers = random.sample(range(99), 5)
else:
    numbers.append(int(user))
    while not stop:
        user_repeat = input(' Anna luku (tyhjä vastaus antaa tulokset): ')
        if user_repeat == '':
            stop = True
        else:
            numbers.append(int(user_repeat))


def numbers_sum():
    nbrs_sum = sum(numbers)
    return nbrs_sum


print(f'Saadut numerot: {numbers}')
print(f'Numeroiden summa: {numbers_sum()}')
