#user input
lenght = float(input('Pike-perch lenght: '))

#if lenght is over 37
if lenght>=37:

    #results
    print('All good.')

#if lenght is under 37 and not equal
if 37!=lenght<=37:

    #calculate missing lenght
    missing = 37-lenght

    #results
    print(f'Too small. It needs to grow {missing}')