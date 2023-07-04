def pretty_func(value: int):
    print(value)
    def inner_func(param: int):
        def inner_inner_func(param2: int):
            return value + param + param2
        return inner_inner_func
    return inner_func


pretty_ten = pretty_func(10)(10)

print(pretty_ten(5), pretty_ten(100), pretty_ten(20), pretty_ten(50))

pretty_five = pretty_func(5)

print(pretty_five(5), pretty_five(100), pretty_five(20), pretty_five(50))

print(pretty_func(20)(40)(40))