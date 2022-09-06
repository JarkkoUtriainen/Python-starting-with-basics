import random

# intro to the "game"
print('\n    Guess The Number!\n\n! Game Of The Year Edition !')

# starting values and random number
goal = random.randint(1, 10)
stop = 0
n = 0

# repeat and stop condition
while stop < 1:

    # user input
    number = int(input('\nAnna numero väliltä 1-10:\n      --> '))

    # correct answer
    if goal == number:
        print('\nOikein')
        stop = stop + 1

        n = n + 1
        print(f'\nArvausten määrä: {n}')

    # guess too high
    elif goal < number:
        print('\nLiian suuri arvaus')

        n = n + 1
        print(f'\nArvausten määrä: {n}')

    # guess too low
    elif goal > number:
        print('\nLiian pieni arvaus')

        n = n + 1
        print(f'\nArvausten määrä: {n}')

    # if there is mistake (should not be useful in this example)
    else:
        print('\njokin meni vikaan')
        stop = stop + 1
