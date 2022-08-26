import random

#get 3 diffrent random values
value_1 = str(random.randint(0,9))
value_2 = str(random.randint(0,9))
value_3 = str(random.randint(0,9))

#get 4 diffrent random values
value_10 = str(random.randint(1,6))
value_20 = str(random.randint(1,6))
value_30 = str(random.randint(1,6))
value_40 = str(random.randint(1,6))

#show values and make it pretty
print(f'\nYour tree number pincode with values between 0-9 is: {value_1}, {value_2}, {value_3}\n\nYour four number pincode with values between 1-6 is: {value_10}, {value_20}, {value_30}, {value_40}')