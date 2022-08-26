import math

leiviska_str = input('give weight in leiviskä: ')
leiviska_value = float(leiviska_str)

naula_str = input('give weight in naula: ')
naula_value = float(naula_str)

luoti_str = input('give weight in luoti: ')
luoti_value = float(luoti_str)

luoti = 13.3
naula = 32*luoti
leiviska = 20*naula

weight = luoti_value*luoti+naula_value*naula+leiviska_value*leiviska

kg = math.trunc(weight/1000)
g = weight-kg*1000


print(f' {kg: 10.0f} kg and {g: 4.0f} g')