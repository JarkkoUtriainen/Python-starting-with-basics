import math

# introduction to the program
print(f'\nLet check if a given year is leap year or not. Please input year and press ENTER.\n')

# user input and taking away the decimal for showing results
year = float(input('What year would you like to check: '))
year_show = math.trunc(year)

# making boolean of the user input according the rules
year_count_100 = year/100
year_count_4 = year/4

check_year_100 = year_count_100.is_integer()
check_year_4 = year_count_4.is_integer()

# checking boolean if given year is divisible by 100 and give results for the user
if check_year_100:

    # making boolean to check if given year is divisible by 400 and give results for the user
    year_count_400 = year/400
    check_year_400 = year_count_400.is_integer()

    if check_year_400:
        print(f'\nYear {year_show} is a leap year.')

    # not divisible by 400
    else:
        print(f'\nYear {year_show} is not a leap year.')

# checking boolean if given year is not divisible by 100 but is divisible by 4 and give results for the user
elif check_year_4 and not check_year_100:

    print(f'\nYear {year_show} is a leap year.')

# if given year is not divisible by 100 or 4 and give results for the user
else:
    print(f'\nYear {year_show} is not a leap year.')


