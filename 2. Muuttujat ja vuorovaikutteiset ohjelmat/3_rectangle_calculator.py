#explanation on how to use this program for user
print('give values and then hit enter.')

#user imput
x_str = input('give rectangle lenght: ')
x = float(x_str)
y_str = input('give rectangle width: ')
y = float(y_str)

#math
area = x*y
circle = (2*x)+(2*y)

#show results
print('area is: ' + str(area))
print('cicle is ' + str(circle))