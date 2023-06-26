# from datetime import datetime, timedelta

# # 1 variant
# def get_birthdays_per_week(users):
#     today = datetime.today()
#     #print(today)
#     next_week = today + timedelta(days=7)
#     #print(next_week)

#     for user in users:
#         if today <= user['birthday'] <= next_week:
#             #print(f"Happy birthday to {user['name']} on {user['birthday'].strftime('%A, %B %d, %Y')}")
#             print({user['birthday'].strftime('%A')}, {user['name']})

# users = [
#     {"name": "John", "birthday": datetime(1990, 6, 18)},
#     {"name": "Andrii", "birthday": datetime(1987, 6, 26)},
#     {"name": "Alex", "birthday": datetime(1995, 6, 24)},
#     {"name": "Anna", "birthday": datetime(1985, 6, 24)},
#     {"name": "Mike", "birthday": datetime(1991, 6, 25)},
#     {"name": "Kate", "birthday": datetime(1992, 6, 28)},
#     {"name": "Tim", "birthday": datetime(1998, 6, 29)}
# ]

# get_birthdays_per_week(users)

# 2 variant
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.now().date()
    print(today)
    # Знаходимо наступний понеділок
    next_monday = today + timedelta(days=(7 - today.weekday()))
    print(next_monday, 'next monday')
    # Обчислюємо дату наступного понеділка для перевірки днів народження
    check_date = next_monday

    # Створюємо словник для зберігання іменинників по днях тижня
    birthdays = {}

    # Обробляємо дні народження для наступного тижня
    for user in users:
        # Отримуємо день народження користувача
        birthday = user["birthday"].date()

        # Перевіряємо, чи є день народження на поточному тижні
        if today <= birthday < check_date:
            # Визначаємо день тижня дня народження
            birthday_day = birthday.strftime("%A")

            # Перевіряємо, чи потрібно змістити день народження на понеділок
            if birthday_day in ["Saturday", "Sunday"]:
                birthday_day = "Monday"

            # Додаємо користувача до словника birthdays
            if birthday_day in birthdays:
                birthdays[birthday_day].append(user["name"])
            else:
                birthdays[birthday_day] = [user["name"]]

    # Виводимо результат
    for day, users in birthdays.items():
        print(f"{day}: {', '.join(users)}")

# Тестовий список users
# users = [
#     {"name": "John", "birthday": datetime(1990, 6, 18)},
#     {"name": "Andrii", "birthday": datetime(1987, 6, 26)},
#     {"name": "Alex", "birthday": datetime(1995, 6, 24)},
#     {"name": "Anna", "birthday": datetime(1985, 6, 24)},
#     {"name": "Mike", "birthday": datetime(1991, 6, 25)},
#     {"name": "Kate", "birthday": datetime(1992, 6, 28)},
#     {"name": "Tim", "birthday": datetime(1998, 6, 29)}
# ]
users = [
    {"name": "John", "birthday": datetime(2023, 6, 18)},
    {"name": "Andrii", "birthday": datetime(2023, 6, 26)},
    {"name": "Alex", "birthday": datetime(2023, 6, 24)},
    {"name": "Anna", "birthday": datetime(2023, 6, 24)},
    {"name": "Mike", "birthday": datetime(2023, 6, 25)},
    {"name": "Kate", "birthday": datetime(2023, 6, 28)},
    {"name": "Tim", "birthday": datetime(2023, 6, 29)}
]
# Виклик функції для тестового списку users
get_birthdays_per_week(users)
