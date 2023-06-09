from datetime import datetime, timedelta

# 1 variant
def get_birthdays_per_week(users):
    today = datetime.today()
    #print(today)
    next_week = today + timedelta(days=7)
    #print(next_week)

    for user in users:
        if today <= user['birthday'] <= next_week:
            print(f"Happy birthday to {user['name']} on {user['birthday'].strftime('%A, %B %d, %Y')}")
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

## 2 variant
# def get_birthdays_per_week(users):
#     today = datetime.today()
#     # start_of_week = today - timedelta(days=today.weekday())
#     start_of_week = today
#     end_of_week = start_of_week + timedelta(days=6)

#     for user in users:
#         birthday = user["birthday"]
#         if start_of_week <= birthday <= end_of_week:
#             print(f"{user['name']} has a birthday on {birthday.strftime('%A, %B %d')}")

# get_birthdays_per_week(users)

# from datetime import datetime, timedelta

# # поточна дата
# current_date = datetime.today()

# # розраховуємо дату наступної суботи
# next_saturday = current_date + timedelta(days=(5 - current_date.weekday()) % 7)

# # розраховуємо дату наступної неділі
# next_sunday = current_date + timedelta(days=(6 - current_date.weekday()) % 7)

# # розраховуємо дату за #2 тижні до поточної дати
# #start_date = current_date - timedelta(weeks=2)
# start_date = current_date
# # розраховуємо дату на тиждень після поточної дати
# end_date = current_date + timedelta(weeks=1)

# users = [
#     {"name": "John", "birthday": datetime(1990, 5, 8)},
#     {"name": "Andrii", "birthday": datetime(1987, 5, 8)},
#     {"name": "Alex", "birthday": datetime(1995, 5, 9)},
#     {"name": "Anna", "birthday": datetime(1985, 5, 11)},
#     {"name": "Mike", "birthday": datetime(1991, 5, 9)},
#     {"name": "Kate", "birthday": datetime(1992, 5, 13)},
#     {"name": "Tim", "birthday": datetime(1998, 5, 14)}
# ]
# # змінюємо дату народження для користувачів відповідно до вимоги задачі
# for user in users:
#     if user["birthday"].date() < start_date.date() or user["birthday"].date() > end_date.date():
#         user["birthday"] = None

#     # якщо дата народження попадає в задані межі, видаляємо з datetime об'єкту години, хвилини та секунди
#     else:
#         user["birthday"] = user["birthday"].replace(hour=0, minute=0, second=0, microsecond=0)
#         print(users)
