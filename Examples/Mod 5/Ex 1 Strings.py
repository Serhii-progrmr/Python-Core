# this_is_string = "Hi there!"

# the_same_string = 'Hi there!'

# this_is_string == the_same_string  # True


# ord('a')  # 97
# print(ord('z'))

# text = """This is first line
# And second line
# Last third line"""

# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# search in strings
# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end)) # 5
# print(s.find("q"))  # -1

# Завдання 7/15 Mod 5
# replace_dict = {117: "o"}
# txt = "sun"
# print(txt)
# print(txt.translate(replace_dict))  # son  translate - метод, який повертає
# рядок, де деякі задані символи замінюються на символи, описані у словнику,
# або таблиці відображення. 
# #
# replace_dict = {ord("u"): "o"}
# txt = "sun"
# print(txt.translate(replace_dict))  # son
# #
# txt = "sun"
# my_table = txt.maketrans("u", "o") # Для створення таблиці відображення
# # використовується метод maketrans
# print(txt.translate(my_table))  # son
#
# txt = "sun"
# my_table = txt.maketrans("nus", "mot")
# print(txt.translate(my_table))  # tom
# #
# CYRILLIC = ("а", "ч", "ш")
# LATIN = ("a", "ch", "sh")

# TRANSLIT_DICT = {}

# for c, l in zip(CYRILLIC, LATIN):
#     TRANSLIT_DICT[ord(c)] = l
#     TRANSLIT_DICT[ord(c.upper())] = l.upper()

# print("чаша".translate(TRANSLIT_DICT))  # chasha
# print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA

# замінити всі підрядки, що відповідають регулярному виразу
# функція sub
import re

p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
print(p)  # color socks and color shoes













