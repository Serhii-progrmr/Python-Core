class Car:
    color = 'blue'
    speed = 120
    
    def start_engine(self, time):
        print(f"Engine work {time} minutes")


car1 = Car()

car1.start_engine(10)    