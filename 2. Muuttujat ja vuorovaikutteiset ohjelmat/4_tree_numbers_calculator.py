#make it fun
input('Are you ready to see something cool? Press ENTER')

#x input for user
x_str = input('Give me number, any number: ')
x = float(x_str)

#y input for user
y_str = input('one more: ')
y = float(y_str)

#z input for user
z_str = input('last one: ')
z = float(z_str)

#math
sum = x+y+z
product = x*y*z
average = (x+y+z)/3

#show results
print('sum is: ' + str(sum))
print('product is: ' + str(product))
print('average is: ' + str(average))