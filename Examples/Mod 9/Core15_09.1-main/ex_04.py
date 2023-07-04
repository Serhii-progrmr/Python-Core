"""LEGB"""

# age = 10

# if age == 10:
#     # name = "Bill"
#     print(__name__)


def get_name():
    name = "Bill"
    def get_age():
        age = 10
        return age
    # age = 
    return name, get_age()


print(get_name())