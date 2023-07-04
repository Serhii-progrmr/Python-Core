def all_capitalize(func):
    def wrapper(ch):
        # result = func(ch).capitalize()
        result = "Hello world"
        return result
    return wrapper


@all_capitalize
def simple_func(word):
    return word[0]


# simple_func = all_capitalize(simple_func)

print(simple_func("hello"))