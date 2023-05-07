class MaxSeatsError(Exception):
    ...

class Bus:
    
    def __init__(self, mark: str, seats: int) -> None:
        self.mark = mark
        if seats > 60:
            raise MaxSeatsError('Seats count <= 60')
        self.seats = seats
    
    def __str__(self) -> str:
        return f'{self.mark}: {self.seats}'


bus1 = Bus('Mercedes', 18)

print(bus1)

try:
    bus2 = Bus('Neoplan', 60)
    print(bus2)
except MaxSeatsError as result:
    print(result)

