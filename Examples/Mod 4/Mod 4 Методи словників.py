#Методи словників
# chars = {'a': 1, 'b': 2}
# b_num = chars.pop('b')
# print(chars)  # {'a': 1}
# print(b_num)  # 2

# chars = {'a': 1, 'b': 2}
# chars.update({"c": 3, "d":4})
# print(chars)  # {'a': 1, 'b': 2, "c": 3}

# chars = {'a': 1, 'b': 2}
# c_idx = chars.get('a', )
# print(c_idx)  # -1

#Цикли та словники
# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }
# for key in numbers:
#     print(key)
# for key in numbers.keys():
#     print(key)
# for val in numbers.values():
#     print(val)
# for key, value in numbers.items():#переберемо пари ключ значення, використовуючи метод items.
#      #На кожній ітерації ми отримаємо пару (ключ, значення):
#     print(key, value)

# Операції и методи словників
# d = {'kyiv': '044', 'odesa': '048', 'lviv': '032'}
# print(d)
# dct = dict(kyiv= 44, odesa= 48, lviv= 32)
# print(dct)
# q= dict.fromkeys(['a', 'b','c'],100)
# print(q)
# m={}
# print(m,type(m))

# словники вкладення
# user_1 = {"name": "Jane", "age": 21}
# user_2 = {"name": "Moris", "age": 23}
# user_3 = {"name": "Steve", "age": 24}

# persons = [user_1, user_2, user_3]

# for user in persons:
#     for field in user:
#         print(user.get(field))
#     print(user.get("name"), user.get("age"))

# Множини -це невпорядковані набори найпростіших об'єктів
# empty = set()
# print(empty, type(empty))  # set() 
string_set = set("My set")
print(string_set)  # {'s', ' ', 'y', 'M', 't', 'e'}
list_set = set(["My", "set"])  # {'My', 'set'}
print(list_set) 

new_set = {1, 2, 3, "My", "set", "H", "i"}
print(new_set)  # {1, 2, 3, 'My', 'i', 'set', 'H'}