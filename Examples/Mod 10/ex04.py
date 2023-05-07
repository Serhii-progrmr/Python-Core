class Car:
    color = 'blue'
    speed = 120
    
    def start_engine(self, *args):
        print(f"Engine work {args[0]} minutes")


car1 = Car()

car2 = Car()

car2.speed = 200

car1.start_engine(10)    