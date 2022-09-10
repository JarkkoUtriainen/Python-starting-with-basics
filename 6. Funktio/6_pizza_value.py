import math

print('Pizza 1\n')
pizza_1_diameter = int(input('Pizzan halkaisija (cm): '))
pizza_1_price = int(input('Pizzan hinta (€): '))
print('\n VS\n\nPizza 2\n')
pizza_2_diameter = int(input('Pizzan halkaisija (cm): '))
pizza_2_price = int(input('Pizzan hinta (€): '))


def value(diameter, price):
    area = math.pi * ((diameter / 2) * 100) ** 2
    value_holder = price / area
    return value_holder


if value(pizza_1_diameter, pizza_1_price) < value(pizza_2_diameter, pizza_2_price):
    print(f'\nPizza 1 on parempi vastine rahalle.\n')
    print(f'Pizza 1 hinta: {value(pizza_1_diameter, pizza_1_price)} €/m^2')
    print(f'Pizza 2 hinta: {value(pizza_2_diameter, pizza_2_price)} €/m^2')
elif value(pizza_1_diameter, pizza_1_price) > value(pizza_2_diameter, pizza_2_price):
    print(f'\nPizza 2 on parempi vastine rahalle.\n')
    print(f'Pizza 1 hinta: {value(pizza_1_diameter, pizza_1_price)} €/m^2')
    print(f'Pizza 2 hinta: {value(pizza_2_diameter, pizza_2_price)} €/m^2')
elif value(pizza_1_diameter, pizza_1_price) == value(pizza_2_diameter, pizza_2_price):
    print(f'\nMolemmat pizzat tarjoaa saman vastineen rahalle.\n')
    print(f'Pizza 1 hinta: {value(pizza_1_diameter, pizza_1_price)} €/m^2')
    print(f'Pizza 2 hinta: {value(pizza_2_diameter, pizza_2_price)} €/m^2')
