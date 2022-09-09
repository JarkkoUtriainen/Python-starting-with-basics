# stop condition
stop = False


# define and count gallons vs liters
def gas():
    liters = gallons_int * 3.78541178
    return liters


# while loop
while not stop:
    gallons = input('\nAnna polttoaineen määrä Yhdysvaltain nestegallonoina: ')
    # if user inputs empty then stop the program
    if gallons == '':
        stop = True
        print('\nOhjelma Lopetettu')
    # if user gives a number then continue program
    else:
        gallons_int = int(gallons)
        # if user gives negative number then stop the program
        if gallons_int < 0:
            stop = True
            print('\nOhjelma lopetettu')
        # if user gave positive number then stop the program
        else:
            print(f'\n {gas()}')
