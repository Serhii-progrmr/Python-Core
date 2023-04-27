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
