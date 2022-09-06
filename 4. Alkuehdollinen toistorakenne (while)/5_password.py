# this is not a secure way to ask passwords! just for training
# starting values
N = 0
stop = 0

# user input and repeat condition
while N < 5 and stop < 1:
    ac = input('Käyttäjätunnus: ')
    pw = input('Salasana: ')

    N = N + 1

    key = ac == 'python' and pw == 'rules'

    # if correct
    if key:
        print('\nTervetuloa\n')

        stop = stop + 1
    # if wrong
    else:
        print('\nPääsy evätty\n')
