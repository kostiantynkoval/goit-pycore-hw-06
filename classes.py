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
    def __init__(self, person_name):
        self.name = Name(person_name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = list(filter(lambda p: p.value != phone, self.phones))

    def edit_phone(self, old_phone, new_phone):
        index = 0
        for p in self.phones:
            if p.value == old_phone:
                break
            else:
                index += 1

        if index is not None:
            self.phones[index] = Phone(new_phone)


    def find_phone(self, phone):
        try:
            return next(filter(lambda p: p.value == phone, self.phones))
        except Exception:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, person_record: Record):
        self.data[person_record.name.value] = person_record

    def find(self, person_name: str):
        return self.data[person_name]

    def delete(self, person_name):
        return self.data.pop(person_name)


try:
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("7777777777")
    print(f"Record Before edit: {john_record}")
    john_record.edit_phone("5555555555", "6666666666")
    john_record.remove_phone("7777777777")
    print(f"Record After edit: {john_record}")
    # john_record.add_phone("9999995555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 6666666666

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("6666666666")
    print(f"{john.name}: {found_phone}")  # Виведення: 6666666666

    # Видалення запису Jane
    book.delete("Jane")

    # Виведення всіх записів у книзі після видалення Jane
    for name, record in book.data.items():
        print(record)

    # Після видалення з книги Джейн рекорд все ще існує
    print(jane_record)

except InvalidPhoneException as exp:
    print(exp)
except Exception as e:
    print(e)

