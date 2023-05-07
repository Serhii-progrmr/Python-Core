class A:
    value = 'a'
    
    
class B(A):
    value = 'b'

a = A()

b = B()

print(b.value, a.value)