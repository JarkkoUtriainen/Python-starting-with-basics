vuodenaika = ("Kevät", "Kesä", "Syksy", "Talvi")

kuukausi = int(input('Anna kuukauden numero ja ohjelma kertoo mikä vuoden aika on kyseessä: '))

if 3 > kuukausi or kuukausi == 12:
    print(vuodenaika[3])
elif 2 < kuukausi < 6:
    print(vuodenaika[0])
elif 5 < kuukausi < 9:
    print(vuodenaika[1])
elif 8 < kuukausi < 12:
    print(vuodenaika[2])
else:
    print('Virhe')
