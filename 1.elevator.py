
class Lift:
    def __init__(self,HighFloor,LowFloor):
        self.HighFloor = HighFloor
        self.LowFloor = LowFloor
        self.currentFloor = LowFloor
        
    def floor_up(self):
        self.currentFloor += 1
        return
    def floor_down(self):
        self.currentFloor -= 1
        return
    def go_to_floor(self, floor):
        move = True
        
        if self.LowFloor > floor:
            move = False
            print('Elevator cant move lower than lowest floor.')
        
        elif self.HighFloor < floor:
            move = False
            print('Elevator cant move higher than highest floor.')
        
        else:
            while move == True:
                if self.currentFloor < floor:
                    self.floor_up()
                    print(f'Floor: {self.currentFloor}')
                elif self.currentFloor > floor:
                    self.floor_down()
                    print(f'Floor: {self.currentFloor}')
                elif self.currentFloor == floor:
                    move = False
                    print(f'Elevator at destination.')
                else:
                    print('Move error in go_to_floor while loop.')
        return
                

h = Lift(10,1)

h.go_to_floor(9)

h.go_to_floor(1)

