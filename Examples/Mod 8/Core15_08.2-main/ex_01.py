from collections import namedtuple


Cat = namedtuple("Cat", ["nickname", "age", "owner"])


barsik = Cat("Barsik", 4, "Perry")

print(type(barsik))

cat = {"nickname": "Sirko", "age": 2, "owner": "Bill"}

print(cat["nickname"])
