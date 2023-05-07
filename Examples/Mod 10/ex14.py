from my_classes import Name, Phone, AddressBook

USERS = AddressBook()

@error_handler
def add_contact(name, phone):
    name = Name(name)
    phone = Phone(phone)
    record = Record(name, phone)
    result = USERS.add_record(record)
    return result
