class A:
    def __init__(self) -> None:
        self.value = 100
        self.field = 'Class A'
        # self.name = name

class B:
    def __init__(self) -> None:
        self.value = 200
        self.field = 'Class B'
        # self.name = name


class C(B, A):
    def __init__(self) -> None:
        super().__init__()
        self.value = 300


b = C()

print(b.field)