# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

# width = 6
# for num in range(16):
#     print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))

# s = "{name} {last_name}".format(last_name="Dilan", name="Bob")
# print(s)  # Bob Dilan
# s = "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
# print(s)  # 'Bob' Dilan

# 8_15
# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

# def formatted_grades(students):

#     grades_list = []
#     count = 0

#     for student, grad in students.items():
#         count += 1
#         grades_list.append(f"{count:>4}|{student:<10}|{grad:^5}|{grades.get(grad):^5}")

#         for el in formatted_grades(students):
#             print(el)

#     return grades_list

# for el in formatted_grades(students):
#     print(el)

# finditer повертає ітератор, що дає об'єкти збігів по всіх збігах, що не перекриваються для шаблону pattern у рядку string.
import re

regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"

test_str = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"

matches = re.finditer(regex, test_str)

for match in matches:
    print(f"{match.group()} start: {match.start()} end: {match.end()}")
