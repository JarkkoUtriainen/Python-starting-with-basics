import random

def dice():
    return random.randint(1,6)

eye = dice()
print(eye)

while eye != 6:
    eye = dice()
    print(eye)

