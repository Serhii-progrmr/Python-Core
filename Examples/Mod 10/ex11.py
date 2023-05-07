from collections import UserList


class MyList(UserList):
    
    def append(self, item: any) -> None:
        if isinstance(item, str):
            self.data.append(item)
        else:
            raise TypeError('item must be a string')
    
    def __str__(self) -> str:
        return '; '.join(self.data)
    
    
my_list = MyList()

# for i in range(10):
#     my_list.append(str(i))

# print(my_list)

try:
    my_list.append(str(5))
except TypeError as e:
    print(e)

print(my_list)