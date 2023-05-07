def decor(cls):
    def wrapper(*args, **kwargs):
        print('In decor')
        print(cls.__name__)
        return cls(*args, **kwargs)
    return wrapper

@decor
class A:
    def __init__(self) -> None:
        pass
    value = 100


a = A()

print(a.value)

