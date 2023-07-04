from sys import getsizeof

def get_letter(word):
    for i in word:
        yield i


gen_letter = get_letter("python")

print(next(gen_letter))
print(next(gen_letter))
print(next(gen_letter))
print(next(gen_letter))
print(next(gen_letter))

gen_number = (x for x in range(1000000))

list_number = [x for x in range(1000000)]

print(getsizeof(list(gen_number)), getsizeof(list_number))