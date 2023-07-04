num_list = [n for n in range(10)]
# num_list = None

gen_filtered = filter(None, num_list)

for i in gen_filtered:
    print(i)
    
    
text = "Hello World"

for i in filter(lambda x: x.isupper(), text):
    print(i)