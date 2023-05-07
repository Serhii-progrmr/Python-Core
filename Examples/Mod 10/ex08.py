class Bus:
    
    def __init__(self, color: str, seats: int) -> None:
        self.color = color
        self.seats = seats
    
    def __str__(self) -> str:
        return f'{self.color} : {self.seats}'


bus1 = Bus('Yellow', 18)

# result = str(bus1)

print(bus1)