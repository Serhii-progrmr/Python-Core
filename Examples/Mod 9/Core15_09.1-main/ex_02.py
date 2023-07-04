def adding(x, y):
    return x + y


def multiplying(x, y):
    return x * y


def apply_func(x, y, func):
    return func(x, y)


print(apply_func(5, 5, adding))

print(apply_func(2, 2, multiplying))