
class Car:
    def __init__(self, reg, topSpeed):
        self.reg = reg
        self.topSpeed = topSpeed
        self.speed = 0
        self.distance = 0
    def accelerate(self, speedChange):
        self.speed += speedChange
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.topSpeed:
            self.speed = self.topSpeed
    def travel(self, hours):
        self.distance += self.speed * hours
        
class ElectricCar(Car):
    def __init__(self, reg, topSpeed, battery) -> None:
        self.battery = battery
        super().__init__(reg, topSpeed)
    
    
class GasolineCar(Car):
    def __init__(self, reg, topSpeed, tank) -> None:
        self.tank = tank
        super().__init__(reg, topSpeed)
        
eCar = ElectricCar("ABC-15", 180, 52.5)
gasCar = GasolineCar("ACD-123", 165, 32.3)

eCar.speed = 100
gasCar.speed = 80

eCar.travel(2)
gasCar.travel(2)

print(f'Sähköauton matkamittari = {eCar.distance}km')
print(f'Polttomoottori auton matkamittari = {gasCar.distance}km')


        
    