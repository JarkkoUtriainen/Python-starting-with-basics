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
        
class Race:
    
    def __init__(self, name, raceLenght, racers):
        self.name = name
        self.raceLenght = raceLenght
        self.racers = racers
        self.lapcount = 0
        
    def hourPasses(self):
        for x in cars:
            x.accelerate(random.randint(-10, 15))
            x.travel(1)
            
    def scoreTable(self):
        cars.sort(key=lambda x: x.distance, reverse=True)
        i = 1
        for x in cars:
            print(f'Sijalla {i}. {x.reg}'
            f' Jonka nopeus on {x.speed}km/h. Hän on kulkenut {x.distance}km!')
            i += 1
            
    def raceOver(self):
        for x in cars:
            if x.distance > self.raceLenght:
                # pieni fanfaari voittajalle koska miksipäs ei
                print(f'\n\nVoittaja on {cars[0].reg}! Onnea voittajalle!\n\nKilpailun tulokset:')
                self.scoreTable()
                print(f'\n')
                return True
            else:
                return False

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

# kisa
race1 = Race('Grand_Demolition_Derby', 8000, cars)
Win = False

print('\n\nKilpailu alkaa!\n\n')

while Win == False:
    
    race1.hourPasses()
    
    lapCheck = race1.lapcount/10
    needScore = lapCheck.is_integer()
    
    if needScore == True:
        race1.scoreTable()
        print('\n')
    
    if race1.raceOver() == True:
        Win = True
    else:
        pass
    
    race1.lapcount += 1
