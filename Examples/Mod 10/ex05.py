class Car:
    def __init__(self, color: str, speed: int = 100):
        self.color = color
        self.speed = speed
        
    def start_engine(self, *args):
        print(f"Engine work {args[0]} minutes")
    
class Ship:
    def __init__(self, color: str, speed: int = 100):
        self.color = color
        self.speed = speed
        


car1 = Car('black')

car2 = Car('blue', 120)

car3 = Car('red')

ship1 = Ship('white')

ship2 = Ship('green')

for transport in [car1, car2, car3, ship1, ship2]:
    print(f"{type(transport)} {transport.color}: {transport.speed}")