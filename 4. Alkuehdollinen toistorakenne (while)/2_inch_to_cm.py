# starting values
stop = 0

# loop conditions
while stop < 1:

    # user input
    inch = float(input('Inch: '))

    # if positive
    if inch > 0:

        cm = inch * 2.51

        print(f'{cm}cm')

    # if negative
    elif inch < 0:

        print('Ohjelma lopetettu.')

        stop = stop + 1

    # if something goes wrong
    else:
        print('Jokin meni vikaan')
