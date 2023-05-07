class Car:
    color = 'blue'
    speed = 120
    
    def start_engine(self):
        print(self.speed)
        

car1 = Car()

car2 = Car()
car2.speed = 180

print(car1.color)

car1.start_engine()
car2.start_engine()