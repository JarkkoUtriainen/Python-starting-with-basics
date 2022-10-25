# Määritellään olio
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


# luodaan olio
car = Car("ABC-123", 142)

# testataan
print(f'\n\nCurrent travelled distance is: {car.distance}km')
car.accelerate(60)
car.travel(1.5)
print(f'\nNew travelled distance is: {car.distance}km')