import math

# input for leiviska
leiviska_str = input('give weight in leiviskä: ')
leiviska_value = float(leiviska_str)

# input for naula
naula_str = input('give weight in naula: ')
naula_value = float(naula_str)

# input for luoti
luoti_str = input('give weight in luoti: ')
luoti_value = float(luoti_str)

# give weight values in grams
luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

# multiply gram weight of the given unit with user input and add it all together
weight = luoti_value * luoti + naula_value * naula + leiviska_value * leiviska

# calculate kg from weight and use that for calculating grams
kg = math.trunc(weight / 1000)
g = weight - kg * 1000

# show results without decimals
print(f' {kg: 10.0f} kg and {g: 4.0f} g')
