# ## task 1_15
# # def real_len(text):
# #     new_text = ""
# #     remove_char = ('\n', '\f', '\r', '\t', '\v')
# #         # (s.find("er", start, end))
# #     for item in text:
# #         if item not in remove_char:
# #             new_text = new_text + item
# #     return len(new_text)
# #     print(new_text) 
# # text = 'Alex\nKdfe23\t\f\v.\r'
# # text = 'Al\nKdfe23\t\v.\r'    
# ## task 2_15
# #Треба реалізувати функцію find_articles для пошуку за статтями цього блогу.
# #Є список articles_dict, в якому міститься опис статей блогу. 
# #Кожен елемент цього списку є словником з наступними ключами: 
#     #прізвища авторів - ключ 'author', назва статті - ключ 'title', рік видання - ключ 'year'.

# #Реалізуйте функцію find_articles,Параметр key функції визначає поєднання букв для пошуку. 
# #Наприклад, при key="Python" функція шукає, чи є у списку articles_dict статті, у назві чи іменах авторів
# # яких зустрічається це поєднання літер. Якщо такі елементи списку були знайдені, треба повернути новий список зі словників,
# # що містять прізвища авторів, назву та рік видання всіх таких статей.
# #Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час пошуку регістр літер. 
# #За умовчанням він дорівнює False і регістр немає значення тобто пошук в тексті "Python" і "python" це те ж саме.
# # Інакше потрібно шукати повний збіг.
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]


# def find_articles(key, letter_case=False):
#     found_articles = []
#     for i in articles_dict:
#         if (str(i).lower().find(key.lower()) != -1 and not letter_case) or str(i).find(key) != -1:
#             found_articles.append(i)
#     print(f"{key}, {letter_case} - {found_articles}")
#     return found_articles

## task 3_15
# phone = "    +38(050)123-32-34"
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   "

# def sanitize_phone_number(phone):
    
#     new_ph_n = ''
#     phone.strip()
#     remove_char = ('+', '(', ')', '-', ' ')    
#     for i in phone:
#         if i not in remove_char:
#             new_ph_n = new_ph_n + i

# # #     return len(new_text)
#     # print(phone)
#     return new_ph_n

# print(sanitize_phone_number(phone))
# print(phone)

# task 4_15
#  функціz is_check_name приймає два параметри (fullname, first_name) і повертає
# логічне значення True або False. Це результат перевірки,
#  чи є рядок first_name префіксом рядка fullname.

# def is_check_name(fullname, first_name):
#    # if  first_name == "":
#    #     return True
#    # else:
#    #     return False
# #def is_check_name(fullname, first_name):
#     return fullname.startswith(first_name)

# task 5_15
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# def get_phone_numbers_for_countries(list_phones):
#     sanitazed_phones = [sanitize_phone_number(phone) for phone in list_phones]
#     phone_dict = {"UA": [], "JP": [], "TW": [], "SG": []}
#     for phone in sanitazed_phones:
#         if phone[:2] == '81':
#             phone_dict["JP"].append(phone)
#         elif phone[:2] == '65':
#             phone_dict["SG"].append(phone)
#         elif phone[:3] == '886':
#             phone_dict["TW"].append(phone)
#         else:
#             phone_dict["UA"].append(phone)
#     return phone_dict

# 2-nd variant (is not working)
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

 
# def get_phone_numbers_for_countries(list_phones):
#     phone_codes = {
#         'JP': '+81',
#         'SG': '+65',
#         'TW': '+886',
#         'UA': '+380'
#     }

#     phone_country = {
#         'UA': [],
#         'JP': [],
#         'TW': [],
#         'SG': []
#     }

#     for phone in list_phones:
#         phone = sanitize_phone_number(phone)
#         prefix = phone[:2] if len(phone) >= 2 else phone[:3]
#         country = phone_codes.get(prefix, 'UA')
#         if phone not in phone_country[country]:
#             phone_country[country].append(phone)

#     return phone_country

# task 6_15
# завдання на перевірку спаму в електронному листі або фільтрацію
# заборонених слів у повідомленні.
import re

def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    if space_around:
        for word in spam_words:
            if re.search(rf"(?<![a-zа-яё0-9]){word.lower()}(?![a-zа-яё0-9])", text):
                return True
        return False
    else:
        for word in spam_words:
            if word.lower() in text:
                return True
        return False

# Приклад виклику функції з різними параметрами
print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
print(is_spam_words('Молох бог ужасен.', ['лох']))  # True


# !!!!wrong code:
# import re

# def is_spam_words(text, spam_words, space_around=False):
#     text_list = re.findall(r"\w+", text.lower())
#     if space_around:
#         for word in spam_words:
#             if word.lower() in text_list:
#                 return False
#         return True
#     else:
#         for word in spam_words:
#             for text_word in text_list:
#                 if word.lower() == text_word:
#                     return True
#         return False
    
# print(is_spam_words("Молох", ["лох"]))  # True
# print(is_spam_words("Молох", ["лох"], True))  # False
# видає результат навпаки:
    # False
    # True
# 2-nd case: # !!!!wrong code
import re


def is_spam_words(text, spam_words, space_around=False):
    text_list = re.findall(r"\w+", text.lower())
    if space_around:
        for word in spam_words:
            if f" {word.lower()} " in f" {' '.join(text_list)} ":
                return True
        return False
    else:
        for word in spam_words:
            if word.lower() in text_list:
                return True
        return False

# Приклад виклику функції з різними параметрами
print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
print(is_spam_words('Молох бог ужасен.', ['лох']))  # True
# !!!!wrong code # Тепер функція повинна повернути правильні результати. У третьому виклику функції отримаємо True, оскільки слово "лох" зустрічається у рядку "Молох бог ужасен." і є простір навколо слова.

# task 7_15
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def translate(name):
    trnsl_name = name.translate(TRANS)
    return trnsl_name





    

