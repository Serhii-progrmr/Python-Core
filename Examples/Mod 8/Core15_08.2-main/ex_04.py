from datetime import datetime, timedelta
from collections import defaultdict


employees = [{"name": "Pitier", "birthdate": datetime(1990, 6, 28)},
            {"name": "Angel", "birthdate": "01.07.2000"},
            {"name": "Angel", "birthdate": datetime(1985, 6, 28)}
            {"name": "John", "birthday": datetime(1990, 7, 1)},
    {"name": "Andrii", "birthday": datetime(1987, 7, 2)},
    {"name": "Alex", "birthday": datetime(1995, 6, 26)},
    {"name": "Anna", "birthday": datetime(1985, 6, 27)},
    {"name": "Mike", "birthday": datetime(1991, 6, 29)},
    {"name": "Kate", "birthday": datetime(1992, 6, 28)},
    {"name": "Tim", "birthday": datetime(1998, 6, 29)}
    ]


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def check_epl(list_of_emp: list) -> None:
    result =defaultdict(list)
    current_year = datetime.now().year
    for employee in list_of_emp:
        bd = employee["birthdate"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)

        start, end = get_period()

        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                result[bd].append(employee["name"])
            else:
                result[bd].append(employee["name"])
    return result


if __name__ == "__main__":
    for key, value in check_epl(employees).items():
        print(key.strftime("%A"), value)
    # print(get_period())
