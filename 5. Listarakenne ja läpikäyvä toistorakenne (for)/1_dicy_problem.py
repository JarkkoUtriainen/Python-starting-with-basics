import random

# starting value
dice_value = 0

# for loop # repeats user input number of times
for i in range(int(input('Montako heittoa: '))):
    # randomize dice and add its value to the previous throws
    dice = random.randint(1, 6)
    dice_value = dice_value + dice

# print results
print(dice_value)
