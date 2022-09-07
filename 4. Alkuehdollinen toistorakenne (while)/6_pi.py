import random
import time

# user input
N = float(input('Montako pistettä laksetaan: '))
n = 0
L = 0

time_1 = time.perf_counter()

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

time_2 = time.perf_counter()
time = time_2 - time_1
print(f'Laskemisessa kesti: {time:4.3f}s')
