dict_list = [{"name": "Bill", "phone": "+123456"},
             {"name": "Jessie", "phone": "+34564565"},
             {"name": "Ron", "phone": "+64565744"}]

tuple_list = [("Bill", "123456"),
              ("Jessie", "34564565"),
              ("Ron", "64565744")]

list_list = [["Bill", "+123456"],
              ["Jessie", "+34564565"],
              ("Ron", "+64565744")]

def check_instance(lst):
    for i in lst:
        if isinstance(i, dict):
            print(f"{i['name']}: {i['phone']}")
        elif isinstance(i, tuple):
            print(f"{i[0]}: {i[1]}")
        else:
            print("Unsupported type of items")        

check_instance(list_list)