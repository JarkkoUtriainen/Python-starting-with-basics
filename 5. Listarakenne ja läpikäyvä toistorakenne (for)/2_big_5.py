stop = 0
numbers = []

while stop == 0:
    number = input('Anna numero: ')

    if number == '':
        stop = 1

    else:
        int_num = int(number)
        numbers.append(int_num)

numbers.sort(reverse=True)
for row in range(5):
    print(numbers[row])