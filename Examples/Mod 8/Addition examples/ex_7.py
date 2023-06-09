"""
Виконати симулювання 1000 викидів гральних кісток. Порівняти очікуваний результат ймовірності випадання з
реальним.
Очікуваний відсоток
2: 2,78  # 2: - це сума костів, яка випаде. 2,78 - ймовірність
3: 5,56
4: 8,33
5: 11,11
6: 13,89
7: 16,67
8: 13,89
9: 11,11
10: 8,33
11: 5,56
12: 2,78
результат зберегти у текстовий файл формату md, як таблиці.
"""

import random

NUMBER_ATTEMPTS = 1000

expected_outcome = {
   "2": 2.78,
   "3": 5.56,
   "4": 8.33,
   "5": 11.11,
   "6": 13.89,
   "7": 16.67,
   "8": 13.89,
   "9": 11.11,
   "10": 8.33,
   "11": 5.56,
   "12": 2.78
}
def dice_roll():
   return random.randint(1, 6)

def experiment():
   values = {
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0,
      "6": 0,
      "7": 0,
      "8": 0,
      "9": 0,
      "10": 0,
      "11": 0,
      "12": 0
   }

   random.seed()
   for el in range(NUMBER_ATTEMPTS + 1):
      roll_one = dice_roll()
      roll_two = dice_roll()
      sum_roll = str(roll_one + roll_two)
      current = values.get(sum_roll)
      values.update({sum_roll: current + 1})

   for k, v in values.items():
      values[k] = round(v / NUMBER_ATTEMPTS * 100,3)

   return values

def write_result(result):
   with open('data.md', 'w', encoding='utf-8') as f:
      f.write('| Вихід | Експеремент % | Орієнтир % |\n')
      f.write('| :----: | :--------: | :---------: |\n')
      for key in expected_outcome.keys():
         f.write('|{:<7}|{:^15}|{:^12}|\n'.format(key, result.get(key), expected_outcome.get(key)))

result = experiment()
write_result(result)
