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
