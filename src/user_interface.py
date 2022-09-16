class UserInterface:
    def __init__(self):
        pass

    @staticmethod
    def add_first_name():
        first_name = input("Enter first name: ")
        return first_name

    @staticmethod
    def add_last_name():
        last_name = input("Enter last name: ")
        return last_name

    @staticmethod
    def add_number():
        number = input("Enter number without +38: ")
        return number

    @staticmethod
    def add_address():
        address = input("Enter address: ")
        return address.capitalize()

    @staticmethod
    def add_date():
        date = input("Enter date born(dd.mm.yyyy): ")
        return date

    @staticmethod
    def input_id():
        note_id = input("Enter user id: ")
        return note_id

    @staticmethod
    def del_menu():
        choice = input('0 - Exit\n1 - Delete by Id\nYour choice: ')
        return choice

