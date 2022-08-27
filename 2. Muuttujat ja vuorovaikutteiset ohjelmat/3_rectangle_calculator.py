# explanation on how to use this program for user
print('give values and then hit enter.')

# user input
x_str = input('give rectangle length: ')
x = float(x_str)
y_str = input('give rectangle width: ')
y = float(y_str)

# math
area = x * y
perimeter = (2 * x) + (2 * y)

# show results
print('area is: ' + str(area))
print('perimeter is ' + str(perimeter))
