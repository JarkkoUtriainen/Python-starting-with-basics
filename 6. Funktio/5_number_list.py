import random

stop = False
numbers = []

user = input('Anna luku (! merkki arpoo 10 lukua): ')

if user == '!':
    numbers = random.sample(range(99), 10)
else:
    while not stop:
        user_repeat = input(' Anna luku (tyhjä vastaus antaa tulokset): ')
        if user_repeat == '':
            stop = True
        else:
            numbers.append(int(user_repeat))


def lst_2():
    numbers_list = [i for i in numbers if i % 2 != 0]
    return numbers_list


print(f'Kaikki numerot: {numbers}')
print(f'Karsitut numerot: {lst_2()}')
