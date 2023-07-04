def best_func(*args):
    if args:
        return args[0].capitalize()


def simple_func(*args):
    if args:
        return args[0] ** 2



def select_func(param):
    if param == int:
        return simple_func
    if param == str:
        return best_func
    return None


# my_func_str = select_func(str)
# my_func_int = select_func(int)
# my_func_none = select_func(None)

# print(my_func_str('hello'))

user_input = input(">>>")
if user_input.isnumeric():
    result = select_func(int)
    print(result(int(user_input)))
else:
    result = select_func(str)
    print(result(user_input))
