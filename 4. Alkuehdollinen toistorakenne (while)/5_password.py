N = 0

while N <= 5 or key not True:
    ac = input('Käyttäjätunnus: ')
    pw = input('Salasana: ')

    N = N + 1

    key = ac == 'python' and pw == 'rules'

    if key:
         print('oikein')

    else:
        print('väärin')


