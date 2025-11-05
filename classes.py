from collections import UserDict
from re import compile,fullmatch

phone_validator = compile(r"^[0-9]{10}$")


class InvalidPhoneException(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if fullmatch(phone_validator, self.value):
            self.value = value
        else:
            raise InvalidPhoneException(f'{self.value} is not a valid phone number')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        pass

    def remove_phone(self, phone):
        pass

    def edit_phone(self, phone):
        pass

    def find_phone(self, phone):
        pass

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        pass


try:
    phone_number = Phone('0975674585')
    print(phone_number)
except InvalidPhoneException as e:
    print(e)
