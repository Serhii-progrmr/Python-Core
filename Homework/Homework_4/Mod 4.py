## examples 1
# my_dict={'key_1': 'value_1',
#     'key_2': 'value_2',
#     'key_3': 'value_3'}

# #print (my_dict['key_13'])
# print (my_dict.get('key_13', None)) #  метод get не дає помилку!!!

## examples 2 # відфільтрувати числа 
# s = 'lsj94ksd231 9'
# result =[]
# for i in s :
#     if i.isdigit():
#         result.append(i)

# print(result)
## examples 3 # знайти числа, кратні 30 або 31 від 30 до 255
# res =[]
# for item in range (30, 256):
#     if item % 30 == 0 or item % 31 == 0:
#         res.append(item) 
# print(res)

## examples 4  # реалізувати рекурсивний прохід по директорії 
# вивести папки і файлиякі є всередині
# назва папки задається через командний рядок
# import sys
# from pathlib import Path
# # sys.argv[1] -> 0-й параметр - назва файлу, 1-й - назва папки
# path = Path(sys.argv[0:1]) 

# def parse_folder(path): # функція ітерування по директорії
#     for element in path.iterdir(): # element - бо невідомо чи папка чи файл
#         if element.is_dir(): # повертає bool-
#             print(f'parse folder: This is folder - {element.name}')
#         else:
#               print(f'parse folder: This is file - {element.name}')

# def parse_folder_recursion(path)parse_folder_recursion(path): 
#     for element in path.iterdir(): # element - бо невідомо чи папка чи файл
#         if element.is_dir(): # повертає bool-
#             print(f'parse folder: This is folder - {element.name}')
#             parse_folder_recursion(element) #рекурсія
#         else:
#               print(f'parse folder: This is file - {element.name}')
# if __name__ == "__main__":
#     parse_folder_recursi(path)     

## mod 2_14
# new_data = []
# def prepare_data(data):
#     new_data = sorted(data)
#     del new_data[0]
#     del new_data[-1]
#     # new_data = new_data.pop(-1)
#     return (new_data)
#         # print(val) 

# data = [1, -3, 4, 100, 0, -5, 10, 1, 1]
# print(data)
# print (prepare_data(data))

# def format_ingredients(items):
#     if len(items) == 0:
#         return ''
#     elif len(items) <2:
#         return items[0]
#     else:
#         return ','.join(items[0:-1]) + ' and '+ items[-1]
   
# items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]

# print(format_ingredients(items))

## mod 4_14
#
# table_1 = {"F": 1, "FX": 2, "E": 3, "D": 3, "C": 4, "B": 5, "A": 5}
# table_2 = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough",
#  "D": "Satisfactorily", "C": "Good", "B": "Very good", "A": "Perfectly"}

# def get_grade(key):
#     return  table_1.get(key)
    
# def get_description(key):
#      return  table_2.get(key)

# print(get_description("F"))

## mod 5_14
# def lookup_key(data, value):
#     list_keys = []
#     for l in data.items():
#         if l[1] == value:
#             list_keys.append(l[0])
#         # print(list_keys)
#     return list_keys 

## mod 6_14 #знайти середнє згачення в списку,
            #поділити на 2 списки
# def split_list(grade):
#     if not grade:
#         return [],[]
#     up_list =[] 
#     low_list =[]
#     tuple(grade)
#     grade.sort()

#     mid = sum(grade) / len(grade)
#     for i in range (len(grade)):
#         if grade[i] <= mid:
#             low_list.append(grade[i])
#         else:
#             up_list.append(grade[i])
#     return low_list, up_list

## mod 7_14 
#Є чотирикутна схема польотів дронів з координатами (1, 2, 3, 4).
# У нас є словник points, ключі якого — кортежі, точки польоту між координатами чотирикутника,
# вигляду (1, 2). Значення словника — це відстані між вказаними точками.
# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }

# coordinates = [0, 1, 3, 2, 0]
# #coordinates = [(0, 1), (1, 3), (2, 3), (1, 2)]


# def calculate_distance(coordinates):#приймає список координат чотирикутника зі словника
#     # виду [0, 1, 3, 2, 0]
#     #коли беремо у словника points значення, у ключі кортежі завжди має бути першою координата
#     #  з меншим значенням — (2, 3), але не (3, 2);
    
#     if len(coordinates) < 2:
#         return 0
    
#     total_distance = 0
#     for i in range(len(coordinates)-1):
#         p1, p2 = sorted((coordinates[i], coordinates[i+1])) 
# #Використання функції sorted() забезпечує те, що ми завжди будемо мати мінімальну координату
# #  з точки p1 та максимальну координату з точки p2. Наприклад, якщо ми маємо точки (3, 1) та (1, 3),
# #  функція sorted() поверне нам кортеж ((1, 3), (3, 1)), а змінній p1 буде присвоєно значення
# #  (1, 3), а змінній p2 — значення (3, 1). незалежно від того, яка з точок передана як перша, p1 завжди
# #  буде містити меншу координату, а p2 — більшу
#         distance = points[p1, p2]
#         total_distance += distance
#         print(total_distance)
#     return total_distance

## mod 8_14
# На вхід функції game подається два аргументи: список, що складається зі списків, та початкове
# значення power - енергія гравця.
# terra = [[1,2,5,10],[2,10,2],[1,3,1]]
# power = 1
# def game(terra, power):
#     for ls_enrg in terra:
#         for item in ls_enrg:
#             #print(item)
#             if power >= item:
#                 power += item           
#                 #print(power)
#             else:
#                  break                
#     print(power)
#     return power

# game(terra, power)  # right answer = 11

## mod 9_14 #буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр і
# # повертати логічне значення — валідний список чи ні. 
# # Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, всі вони зберігаються
# # у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.

# def is_valid_pin_codes(pin_codes): #Приклад аргументу для функції is_valid_pin_codes:
#                                     ['1101', '9034', '0011']
#     if not pin_codes: 
#         return False
    
#     set_pin_codes = set(pin_codes)
#     if len(set_pin_codes) != len(pin_codes):
#         return False
#     for code in pin_codes:
#         if len(code) != 4 or not code.isdigit():
#             return False
#     return True

# # mod 10_14
# from random import randint

# def get_random_password(): #має випадковим чином вибрати із запропонованого діапазону 8 символів
# #та повернути згенерований пароль у вигляді рядка.
#     paswset = "()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
#     password = ""
#     for i in range(8):
#         random_num = randint(40, 126) #randint(A, B) і повертає випадкове ціле число N, A ≤ N ≤ B
#         password += chr(random_num)
#     print (password)    
#     return password    

# get_random_password()      

## mod 11_14
# def is_valid_password(password):
  
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False
    
# #def is_valid_password(password): # 2-nd variant->

#     # Перевірка наявності хоча б однієї літери у верхньому регістрі
#     if not any(c.isupper() for c in password):
#         return False
#         # Перевірка наявності хоча б однієї літери у нижньому регістрі
#     if not any(c.islower() for c in password):
#         return False
#         # Перевірка наявності хоча б однієї цифри
#     if not any(c.isdigit() for c in password):
#         return False
    
#     # Якщо усі критерії виконуються, повертаємо True
#     return True 

# password = "i0zLnOwI"        
# is_valid_password(password)

# mod 12_14 # згенерує нам випадковий надійний пароль та поверне його.
# Алгоритм простий — ми генеруємо пароль за допомогою функції get_random_password і,
# якщо він проходить перевірку на надійність функцією is_valid_password, повертаємо його,
# якщо ні — повторюємо ітерацію знову.
# 

## mod 13_14
# import sys
# from pathlib import Path


# path = Path(sys.arg[1])

# def parse_folder(path):
#     files = []
#     folders = []
#     for el in path.iterdir():
#         # if el.isdir():
#     #         print(f'parce_folder: This is folder {el.name}')
#     #         folders.append(el.name)
#     #         parse_folder(el)
#     #     else:
#     #         print(f'parce_folder: This is file {el.name}')
#     #         files.append(el.name)
#     # return files, folders
#         if el.is_dir():
#             print(f'parse_folder: This is folder {el.name}')
#             sub_files, sub_folders = parse_folder(el)
#             files += sub_files
#             folders.append(el.name)
#             folders += sub_folders
#         else:
#             print(f'parse_folder: This is file {el.name}')
#             files.append(el.name)
#     return files, folders

    
# if __name__ == '__main__':
#     path = Path(sys.argv[1])
#     files, folders = parse_folder(path)
#     print(files, folders)

## mod 14_14
import sys


def parse_args():#повертає рядок, складений з аргументів командного рядка, розділених пробілами.
    # Наприклад, якщо скрипт був викликаний командою: python run.py first second, то функція
    #  parse_args повинна повернути рядок наступного виду 'first second'.
    result = ""
    for arg in sys.argv:
        result = ' '.join(sys.argv[1:])
    print(result)  
    return result
