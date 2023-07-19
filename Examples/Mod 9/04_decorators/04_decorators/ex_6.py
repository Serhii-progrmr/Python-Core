def decorator(func):

    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, **kwargs)
        print('finish decorator...')
    return inner

# def say(name, surname, age):
#     print('hello', name, surname,age)

# # def buy():
# #     print('buy world')

# say = decorator(say)
# say('Peter','Ivanko', 20)

def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

@table
@header
def say(name, surname, age):
    print('hello', name, surname,age)



# say = table(header(say))
say('Peter','Ivanko', 20)
