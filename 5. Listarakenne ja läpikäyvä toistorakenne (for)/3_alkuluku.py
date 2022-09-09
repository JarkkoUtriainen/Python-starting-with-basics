x = int(input('Anna numero:'))
if x > 1:
    for i in range(2,x):
        if (x % i) == 0:
            print('Ei ole alkuluku.')
            break

    else:
        print('On alkuluku.')

else:
    print('Ei ole alkuluku.')
