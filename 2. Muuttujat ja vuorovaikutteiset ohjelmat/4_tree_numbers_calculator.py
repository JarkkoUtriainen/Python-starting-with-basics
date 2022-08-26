input('Are you ready to see something cool? Press ENTER')

x_str = input('Give me number, any number: ')
x = float(x_str)

y_str = input('one more: ')
y = float(y_str)

z_str = input('last one: ')
z = float(z_str)

sum = x+y+z
product = x*y*z
average = (x+y+z)/3

print('sum is: ' + str(sum))
print('product is: ' + str(product))
print('average is: ' + str(average))