# Määritellään olio
class Car:
    def __init__(self, reg, topSpeed):
        self.reg = reg
        self.topSpeed = topSpeed
        self.speed = 0
        self.travel = 0

    def accelerate(self, speedChange):
        self.speed += speedChange
        if self.speed < 0:
            self.speed = 0
        elif self.speed > self.topSpeed:
            self.speed = self.topSpeed

# luodaan olio
car = Car("ABC-123", 142)

# kiihdytykset
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f'\n1st Current speed: {car.speed}\n\n')

# hätäjarrutus
car.accelerate(-200)

print(f'\n2nd Current speed: {car.speed}\n\n')


