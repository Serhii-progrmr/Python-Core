num_list = [n for n in range(10)]


def simple_func(x):
    return x * x


gen_map = map(simple_func, num_list)

print(next(gen_map))
print(next(gen_map))
print(next(gen_map))
print(next(gen_map))