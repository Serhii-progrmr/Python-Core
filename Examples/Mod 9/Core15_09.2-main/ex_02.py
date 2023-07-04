from datetime import datetime


def logger(write=False):
    def inner(func):
        def wrapper(*args):
            if write:
                with open("log.txt", "a") as file:
                    file.write(str(datetime.now().timestamp()))
                    file.write(", ".join([str(val) for val in args]))
                    file.write("\n")
            return func(*args)
        return wrapper
    return inner


write_to_log = False


def connection(*args):
    return "Connection success"


@logger(write_to_log)
def connect_db(db_name, db_pass):
    connect = connection(db_name, db_pass)
    print(connect)


@logger(write_to_log)
def print_result(*args):
    for i in args:
        print(i)


if __name__ == "__main__":
    # decor_connection = logger(connect_db)
    # decor_connection("DB_NAme", "PWD")
    # decor_print = logger(print_result)
    # decor_print(2, "Hello")
    connect_db("Name", "PWD")
    print_result("hello", "world")