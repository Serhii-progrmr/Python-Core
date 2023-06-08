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

def sanitize_phone_number(phone):

    new_ph_n = ''
    phone.strip()
    remove_char = ('+', '(', ')', '-', ' ')
    for i in phone:
        if i not in remove_char:
            new_ph_n = new_ph_n + i

# #     return len(new_text)
    # print(phone)
    return new_ph_n

print(sanitize_phone_number(phone))
print(phone)
