import random
D = int(input('Mitä noppaa heitetään? D'))

def dice():
    return random.randint(1,D)

eye = dice()
print(eye)

while eye != D:
    eye = dice()
    print(eye)