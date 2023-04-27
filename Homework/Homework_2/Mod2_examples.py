#Логічні вирази
#Example1

# money = input('Enter money' )
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

#Example2
# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# task 2_15
# is_active = input("Is the user active? ")
# is_admin = input("Is the user administrator? ")
# is_permission = input("Does the user have access? ")
# print (is_active)

# is_active = bool(is_active)
# #is_admin = bool(is_admin)
# is_permission = bool(is_permission)

# if is_admin := True:
#     access = True 
#elif is_active and is_permission := True:
    #access = True 

#task 2_16
# work_experience = int(input("Enter your full work experience in years: "))

# if  work_experience > 1 and work_experience <= 5:
#     developer_type = "Middle"
# elif  work_experience <= 1:
#     developer_type = "Junior"
# else :
#     developer_type = "Senior"
# print(developer_type)

#task 4/15
# num = int(input("Enter a number: "))

# if num > 0:
#     if (num % 2) != 0:
#         result = "Positive odd number"
#     else:
#         result = "Positive even number"
# elif num < 0:
#     result = "Negative number"
# else:
#     result = "It is zero"
# print(result)   

#task 5/15 square equation
# import math
# a = int(input("Enter coefficient a: "))
# b = int(input("Enter coefficient b: "))
# c = int(input("Enter coefficient c: "))

# D = b ** 2 - 4 * a * c

# if D > 0:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
# else:
#     print (f"the equation has no real roots")

#task 6/15
# num = int(input("Enter an integer number: "))

# n = bool(num % 2 == 0)
# print(n)
# is_even = True if n else False 
# print(is_even)

#task 7/15
#examle 
# num = int(input("Введіть ціле число (0 до 10): "))
# count = 10 - num
# i = 1
# while i <= count:
#     print(f"Ітерація {i}")
#     i = i + 1

# print("Програма закінчена")

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# i = 1
# while i <= num:
#     sum = sum +i
#     i = i + 1
     
# print(f"sum is {sum}") 

   
# for variable in range(0, 5, 3):
#     print(variable)  # 0 1 2 3 4

# fruit = 'apple'
# for char in fruit:
#     print(char)

#task 8/15
# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0

# for item in message:
#      if item == search:   
#         result += 1

# print(result)
#message = 'python is popular programming language'

# number of occurrence of 'p'
##print('Number of occurrence of r:', message.count('r'))

# Output: Number of occurrence of p: 4
        
#count = 0

# my_string = "Programiz"
# my_char = "r"

# for i in my_string:
#     if i == my_char:
#         count += 1

# print(count)

#task 9/15 

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# if first - second < 0:
#      gcd = first 
# else:
#      gcd = second
# while second % gcd != 0 or first % gcd != 0:
#     gcd = gcd - 1

# print (gcd)

#task 10/15
# num = int(input("Enter integer (0 for output): "))
# sum = 0
# i = 0
# while i <= num and num != 0: 
#     for i in range(0,num):
#         i += 1
#         sum = sum + i       
#     num = int(input("Enter integer (0 for output): "))
# print(sum)        


#task 11/15
# num = 10
# for variable in range(num):
#     if variable % 2 == 1:
#         continue
#     print(variable)

#task 12/15
sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2 == 1: # if i % 2 != 0:
#       #    continue
#         sum = sum + i
 
# print(sum)
   
#task 13/15 Код Цезаря
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ch == " " or ch == "!":
        encoded_message = encoded_message + ch
        continue
    pos = ord(ch) - ord('a')
