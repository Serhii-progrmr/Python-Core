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
# def is_check_name(fullname, first_name):
#    # if  first_name == "":
#    #     return True
#    # else:
#    #     return False
# #def is_check_name(fullname, first_name):
#     return fullname.startswith(first_name)

# task 5_15 ЗАВДАННЯ: ВАЛІДАЦІЯ ПОВІДОМЛЕННЯ НА НАЯВНІСТЬ СПАМ СЛІВ
# import re


# def is_spam_words(text, spam_words, space_around = False):
#     text = text.lower()
#     if space_around:
#         for word in spam_words:
#             if re.search(rf"(?<![a-zа-яё0-9]){word.lower()}(?![a-zа-яё0-9])", text):
#                 return True
#         return False
#     else:
#         for word in spam_words:
#             if word.lower() in text:
#                 return True
#         return False

# # Приклад виклику функції з різними параметрами
# print(is_spam_words("Молох", ["лох"]))  # True
# print(is_spam_words("Молох", ["лох"], True))  # False
# print(is_spam_words('Молох бог ужасен.', ['лох']))  # True

# task 6_15 набір інструментів для обробки рядків
# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = {}

# for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = t
#     TRANS[ord(c.upper())] = t.upper()


# def translate(name):
#     trnsl_name = name.translate(TRANS)
#     return trnsl_name

# task 8_15
# приймає на вхід словник оцінювання студентів за предмет наступного вигляду:
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


# def formatted_grades(students):# приймає на вхід словник оцінювання студентів за предмет
#     formatted_list = []
#     for index, (name, grade) in enumerate(students.items(), start=1):
#         formatted_row = "{:>4}|{:<10}|{:^5}|{:^5}".format(index, name, grade, grades[grade])
#         formatted_list.append(formatted_row)
#     return formatted_list
# #повертає список відформатованих рядків, щоб під час виведення наступного коду:
# for el in formatted_grades(students):
#     print(el)
# Виходила наступна таблиця:
# 1|Nick      |  A  |  5
# 2|Olga      |  B  |  5
# 3|Mike      | FX  |  2
# 4|Anna      |  C  |  4

# task 9_15
# def formatted_numbers():
#     list_numbers = list()
#     list_numbers.append("| decimal  |   hex    |  binary  |")
#     print(list_numbers[0])
#     for n in range(16):
#         list_numbers.append("|{:<10d}|{:^10x}|{:>10b}|".format(n, n, n))
#         print(list_numbers[n])
#     return list_numbers


#formatted_numbers()

# task 10_15
# import re


# def find_word(text, word):# приймає два параметри: перший text та другий word?
#                         # виконує пошук зазначеного слова word у тексті text за
#                         #  допомогою функції search та повертає словник.
#     find = {'result': None,
#                 'first_index': None,
#                 'last_index': None,
#                 'search_string': None,
#                 'string': None,}
#     match = re.search(word,text)
#     if match:
#         find['result'] = True
#         find['first_index']  = match.span()[0]
#         find['last_index']  = match.span()[1]
#         find['search_string'] = word
#         find['string'] = text
#     else:
#         find['result'] = False
#         find['search_string'] = word
#         find['string'] = text
#     return find

    # 2-nd version of code
    # result_dict = {'result': '', 'first_index': '', 'last_index': '', 'search_string': '', 'string': '' }
    # if not text.find(word) ==-1:
    #     result_dict['result'] = True
    #     result_dict['first_index'] = text.find(word)
    #     result_dict['last_index'] = result_dict['first_index'] + len(word)
    #     result_dict['search_string'] = word
    #     result_dict['string'] = text
    # else:
    #     result_dict['result'] = False
    #     result_dict['first_index'] = None
    #     result_dict['last_index'] = None
    #     result_dict['search_string'] = word
    #     result_dict['string'] = text

    # return result_dict

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))

# task 11_15 #знайти всі відповідні шаблону значення функція findall
# import re


# def find_all_words(text, word):#яка шукає збіг слова в тексті. Функція повертає список всіх знаходжень
#                                 # слова в параметрі word в тексті
#     find_all = ()
#     match = re.findall(word,text,re.IGNORECASE) # Використовуючи цей флаг,
#             # можна забезпечити регістронезалежний пошук при використанні регулярних виразів.
#     if match:
#         return match

# task 12_15
# import re


# def replace_spam_words(text, spam_words):# Щоб замінити всі підрядки, що відповідають регулярному виразу
#     for spm_wrd in spam_words:
#         text = re.sub(spm_wrd, '*'*len(spm_wrd),text, flags=re.IGNORECASE) #Щоб замінити всі підрядки,
#         # що відповідають регулярному виразу
#     return text

# task 13_15 # регулярний вираз для функції find_all_emails, яка буде в тексті (параметр text) знаходити
# всі email та повертати список отриманих з тексту збігів

# import re


# def find_all_emails(text):
#     pattern = r"([A-Za-z]{1}[A-Za-z0-9._]{1,}@[A-Za-z]+\.[A-Za-z]{2,})"
#     result = re.findall(pattern, text)
#     #result = ['@'.join(match) for match in matches]
#     return result

# task 14_15 # шукатимемо номер телефону України в міжнародному форматі,
            # шаблон якого наступний: +380(67)777-7-777 або +380(67)777-77-77
import re


def find_all_phones(text):
    # result = re.findall(r"([+]{1}\d{3}\W\[067]{1}\[7]{3}\W\[7]{2})", text)
    result = re.findall(r"\+380\(\d{2}\)\d{3}-(?:\d{2}|\d-\d{3})", text)
    return result
