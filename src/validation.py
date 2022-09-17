from datetime import datetime
from src.user_interface import user_interface


class Validation:
    def __init__(self):
        self.note_list = []

    def add_note_validation(self):
        self.note_list.append(self.first_name_valid())
        self.note_list.append(self.last_name_valid())
        self.note_list.append(self.number_valid())
        self.note_list.append(user_interface("4"))
        self.note_list.append(self.date_valid())
        return self.note_list

    @staticmethod
    def first_name_valid():
        while True:
            first_name = user_interface("1")
            if len(first_name) < 2 or not first_name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return first_name.capitalize()

    @staticmethod
    def last_name_valid():
        while True:
            last_name = user_interface("2")
            if len(last_name) < 2 or not last_name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return last_name.capitalize()

    @staticmethod
    def number_valid():
        while True:
            number = user_interface("3")
            if len(number) != 10 or not number.isdigit():
                print("Incorrect input phone number. Try again\n")
            else:
                return number

    @staticmethod
    def date_valid():
        while True:
            date = user_interface("6")
            if len(date) == 0:
                break
            try:
                if datetime.strptime(date, '%d.%m.%Y'):
                    return date
            except ValueError:
                print("Invalid data. Try again")
                return False

    @staticmethod
    def id_validation():
        while True:
            try:
                note_id = int(user_interface("7"))
                return note_id
            except ValueError:
                print("You didn't enter a number. Try again")

    @staticmethod
    def menu_validation(menu, menu_len: int):
        while True:
            try:
                if menu == '0':
                    return int(menu)
                elif int(menu) not in range(1, menu_len + 1):
                    print("Unknown command. Try again")
                else:
                    return int(menu)
            except ValueError:
                print("You didn't enter a number. Try again")


