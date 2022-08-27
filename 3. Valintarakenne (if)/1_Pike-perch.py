# user input
length = float(input('Pike-perch length in cm: '))

# if length is over 37
if length >= 37:
    # results
    print('All good.')

# if length is under 37 and not equal
if 37 != length <= 37:
    # calculate missing length
    missing = 37 - length

    # results
    print(f'Too small. It needs to grow {missing}cm.')
