# starting values
stop = 0

big = None
small = None

print('Hei! Syötä mitä tahansa numeroita niin minä muistan mikä oli isoin numero ja mikä oli pienin numero.\n')

# repeat condition
while stop < 1:

    # user input
    number = input('Anna numero: ')

    #stop condition
    if number == '':

        stop = stop + 1

    # if user inputs numbers
    else:
        fnumber = float(number)

        # largest value
        if big is None:
            big = fnumber

        elif fnumber > big:
            big = fnumber

        # smallest value
        if small is None:
            small = fnumber

        elif fnumber < small:
            small = fnumber

# print results
print(f'Isoin numero: {int(big)}\nPienin numero: {int(small)}')
