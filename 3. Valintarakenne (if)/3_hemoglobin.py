# introduction to the program
print(f'\nHi! Lets check if your hemoglobin is ok!')
print(f'\nFirst we need to know your biological sex.\nPlease write M for male & F for female and press ENTER.\n')

# user input for biological sex
sex = str(input('I am: '))

# user input and instructions for hemoglobin
print(f'\nNext we need your hemoglobin in g/l.\n')

hg = float(input('My hemoglobin is: '))

# for making the program feel more interactive
print(f'\nResults are in:')

# if user inputs male
if sex == 'm' or sex == 'M':

    if 134 <= hg <= 195:
        print(f'\nAll good!')

    elif hg <= 134:
        print(f'\nOh no! Your hemoglobin is too low!')

    elif hg >= 195:
        print(f'\nOh no! Your hemoglobin is too high!')

# if user inputs female
elif sex == 'F' or sex == 'f':

    if 117 <= hg <= 175:
        print(f'\nAll good!')

    elif hg <= 117:
        print(f'\nOh no! Your hemoglobin is too low!')

    elif hg >= 175:
        print(f'\nOh no! Your hemoglobin is too high!')

else:
    print(f'\nSomething went wrong. Check your inputs and try again.')
