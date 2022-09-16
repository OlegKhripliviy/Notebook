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
        return address

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

    @staticmethod
    def update_menu():
        update_menu = input("\nWhat attribute do you want to change:\n0 - Exit\n"
                            "1 - First name\n2 - Last name\n3 - Number\n4 - Address\n5 - Date of Birth\n")
        return update_menu

    @staticmethod
    def position_choice():
        choice = input("Your choice: ")
        return choice

    @staticmethod
    def new_value():
        value = input("Enter new value: ")
        return value
    # def update_note_interface(self):
    #     user_id = input("Enter user's id to update: ")
    #     print("\nWhat attribute do you want to change:\n"
    #           "1 - First name\n2 - Last name\n3 - Number\n4 - Address\n5 - Date of Birth\n")
    #     what_to_update = input("Your choice: ")
    #
    #     new_value = input("Enter new value: ")
