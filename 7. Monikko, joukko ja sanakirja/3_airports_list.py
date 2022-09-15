stop = False
lentokentat = {}

print('\nKirjoita: "lisää" lisätäksesi uuden lentokentän, "hae" hakeaksesi jo tallennetun lentokentän tai "lopeta" '
      'lopettaaksesi ohjelman.\n')

while not stop:
    toiminto = input('\nMitä haluat tehdä: ')
    toiminto = toiminto.lower()

    if toiminto == 'lisää':
        icao = input('Anna kentän ICAO-koodi: ')
        nimi = input('Anna kentän nimi: ')
        lentokentat[icao] = nimi

    elif toiminto == 'hae':
        icao_x = input('Anna kentän ICAO-koodi: ')
        print(f'Kentän nimi: {lentokentat[icao_x]}')

    elif toiminto == 'lopeta':
        stop = True

    else:
        print('Virhe')