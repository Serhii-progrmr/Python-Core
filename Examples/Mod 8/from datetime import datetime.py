## Можливості деяких вбудованих пакетів Python
# Робота з датою і часом у Python реалізована у пакеті datetime.
# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime) # 2023-04-18 16:56:08.413483

from datetime import datetime #

current_datetime = datetime.now()

print(current_datetime.year)        # 2020
print(current_datetime.month)       # 10
print(current_datetime.day)         # 09
print(current_datetime.hour)        # 22
print(current_datetime.minute)      # 32
print(current_datetime.second)      # 22
print(current_datetime.microsecond) # 819366

from datetime import datetime, timedelta

# 1 variant
def get_birthdays_per_week(users):
    today = datetime.today()
    #print(today)
    next_week = today + timedelta(days=7)
    #print(next_week)

    for user in users:
        if today <= user['birthday'] <= next_week:
            #print(f"Happy birthday to {user['name']} on {user['birthday'].strftime('%A, %B %d, %Y')}")
            print({user['birthday'].strftime('%A')}, {user['name']})

users = [
    {"name": "John", "birthday": datetime(1990, 6, 18)},
    {"name": "Andrii", "birthday": datetime(1987, 6, 26)},
    {"name": "Alex", "birthday": datetime(1995, 6, 24)},
    {"name": "Anna", "birthday": datetime(1985, 6, 24)},
    {"name": "Mike", "birthday": datetime(1991, 6, 25)},
    {"name": "Kate", "birthday": datetime(1992, 6, 28)},
    {"name": "Tim", "birthday": datetime(1998, 6, 29)}
]

get_birthdays_per_week(users)

