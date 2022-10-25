class Car:
    def __init__(self, reg, topSpeed):
        self.reg = reg
        self.topSpeed = topSpeed
        self.speed = 0
        self.travel = 0


car = Car("ABC-123", 142)

print(f' Car: {car.reg}'
      f'\nTop speed: {car.topSpeed}'
      f'\nCurrent speed: {car.speed}'
      f'\nTravel distance: {car.travel}')
