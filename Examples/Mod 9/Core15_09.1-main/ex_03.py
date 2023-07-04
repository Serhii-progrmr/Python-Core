def adding(x, y):
    return x + y


def multiplying(x, y):
    return x * y


def subtraction(x, y):
    return x - y


trampampam = {adding: ("+", "плюс", "додай", "add"),
              multiplying: ("*", ),
              subtraction: ("-", )}

x = 10
y = 5

# for i in ("+", "додай", "*", "add", "-", "плюс"):
while True:
    user_input = input(">>>")
    
    if not user_input:
        break
    
    for Пирятин, Суми in trampampam.items():
        if user_input in Суми:
            print(Пирятин(x, y))