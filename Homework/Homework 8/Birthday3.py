from datetime import datetime, timedelta



def get_birthdays_per_week(users):
    # Отримуємо поточну дату і поточний рік
    today = datetime.now().date()
    current_year = datetime.now().year

    #print(today)
    # Знаходимо наступний понеділок
    next_monday = today + timedelta(days=(7 - today.weekday()))
    #print(next_monday, 'next monday')
    # Обчислюємо дату наступного понеділка для перевірки днів народження
    check_date = next_monday

    # Створюємо словник для зберігання іменинників по днях тижня
    birthdays = {}

    # Обробляємо дні народження для наступного тижня
    for user in users:
        # Отримуємо день народження користувача в поточному році
        birthday = user["birthday"].date()
        birthday = birthday.replace(year=current_year)
        #print(birthday)
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
users = [
    {"name": "John", "birthday": datetime(1990, 7, 1)},
    {"name": "Andrii", "birthday": datetime(1987, 7, 2)},
    {"name": "Alex", "birthday": datetime(1995, 6, 26)},
    {"name": "Anna", "birthday": datetime(1985, 6, 27)},
    {"name": "Mike", "birthday": datetime(1991, 6, 29)},
    {"name": "Kate", "birthday": datetime(1992, 6, 28)},
    {"name": "Tim", "birthday": datetime(1998, 6, 29)}
]

# Виклик функції для тестового списку users
get_birthdays_per_week(users)
