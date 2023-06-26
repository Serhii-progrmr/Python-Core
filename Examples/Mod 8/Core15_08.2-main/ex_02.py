from dataclasses import dataclass

@dataclass
class Cat:
    nickname: str
    age: int
    owner: str


barsik = Cat("Barsik", 3, "Perry")

print(barsik.nickname)