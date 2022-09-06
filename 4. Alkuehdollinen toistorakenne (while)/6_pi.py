import random

# user input
N = float(input('Montako pistettä laksetaan: '))
n = 0
L = 0

# program repeats given calculation
while N > L:
    x = random.random()
    y = random.random()

    L = L + 1

    Cal = x ** 2.0 + y ** 2.0 < 1

    if Cal:
        n = n + 1

# calculate pi
Pi = 4 * n / N

# print results
print(f'{Pi}')
