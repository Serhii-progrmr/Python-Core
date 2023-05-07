class A:
    value_a = 'a'
    
    
class B:
    value_b = 'b'


class C:
    value = 'c'


class D(A, B, C):
    ...


d = D()

# print(D.mro())

print(d.value)