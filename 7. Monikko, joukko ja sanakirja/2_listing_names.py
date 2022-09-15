nimet = set()

stop = False
while not stop:
    i = input('Nimi: ')
    if i == '':
        stop = True
    elif i in nimet:
        print('\nAiemmin syötetty nimi\n')
    elif i not in nimet:
        print('\nUusi nimi\n')
        nimet.add(i)

print('\nAnnetut nimet olivat: ')
for x in nimet:
    print(x)
