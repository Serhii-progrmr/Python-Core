def super_func(x, y, z):
    return x + y + z


print(super_func(10, 10, 5))


def super_carrying(x):
    def super_func(y, z):
        return x + y + z
    return super_func

adding_to_ten = super_carrying(10)

print(adding_to_ten(10, 5))