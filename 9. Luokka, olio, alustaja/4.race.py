import random

# Määritellään olio
class Car:
    def __init__(self, reg, topSpeed):
        self.reg = reg
        self.topSpeed = topSpeed
        self.speed = 0
        self.distance = 0
    # kiihdytys funktio
    def accelerate(self, speedChange):
        self.speed += speedChange
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.topSpeed:
            self.speed = self.topSpeed
    # kuljettu matka funktio
    def travel(self, hours):
        self.distance += self.speed * hours

# luodaan peli
# lista olioille
cars = []

# luodaan Car olioita annettujen ohjeiden mukaan
for x in range(1, 11):
    randomTopSpeed = random.randint(100, 200)
    new_reg = "ABC-"
    new_reg += str(x)
    carx = Car(new_reg, randomTopSpeed)
    cars.append(carx)

# kisa looppi
Win = False
while Win == False:
    for x in cars:
        x.accelerate(random.randint(-10, 15))
        x.travel(1)
        if x.distance >= 10000:
            Win = True

# järjestetään cars lista kuljettujen etäisyyksien mukaan
cars.sort(key=lambda x: x.distance, reverse=True)

# pieni fanfaari voittajalle koska miksipäs ei
print(f'\n\nVoittaja on {cars[0].reg}! Onnea voittajalle!\n\nKilpailun tulokset:')

# tehdään taulukko tuloksista
# jos kisailija suoriutuu erittäin huonosti saa hän erinlaisen tekstin
i = 1
for x in cars:
    if x.distance > 6000:
        print(f'Sijalla {i}. {x.reg}'
            f' jonka huippunopeus on {x.topSpeed}km/h. Hän kulki huimat {x.distance}km! Nopeus kisan loppuessa: {x.speed}km/h')
    else:
        print(f'Sijalla {i}. {x.reg}'
              f' jonka huippunopeus on {x.topSpeed}km/h. Hän kulki surkeat {x.distance}km! Nopeus kisan loppuessa: {x.speed}km/h. Booo!')
    i += 1
