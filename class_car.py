class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0
    
    def accelerate(self, amount:int):
        self.speed += amount
        print(f'가속, 현속도{self.speed}임')

    
    def brake(self, amount:int):
        self.speed -= amount
        print(f'감속, 현속도{self.speed}임')

    
    def get_speed(self):
        return self.speed
    

car = Car(model='ToYoTa', color='Red')
car.accelerate(20)
car.accelerate(15)
car.brake(5)
print(car.model, car.color, car.get_speed())