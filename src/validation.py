from datetime import datetime
from src.user_interface import UserInterface

us = UserInterface()


class Validation:
    def __init__(self):
        self.note_list = []

    @staticmethod
    def first_name_valid():
        while True:
            first_name = us.add_first_name()
            if len(first_name) < 2 or not first_name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return first_name

    @staticmethod
    def last_name_valid():
        while True:
            last_name = us.add_last_name()
            if len(last_name) < 2 or not last_name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return last_name

    @staticmethod
    def number_valid():
        while True:
            number = us.add_number()
            if len(number) != 10 or not number.isdigit():
                print("Incorrect input phone number. Try again\n")
            else:
                return number

    @staticmethod
    def date_valid():
        while True:
            date = us.add_date()
            if len(date) == 0:
                break
            try:
                if datetime.strptime(date, '%d.%m.%Y'):
                    return date
            except ValueError:
                print("Invalid data. Try again")
                return False

    def add_note_validation(self):
        self.note_list.append(self.first_name_valid())
        self.note_list.append(self.last_name_valid())
        self.note_list.append(self.number_valid())
        self.note_list.append(us.add_address())
        self.note_list.append(self.date_valid())
        return self.note_list

    @staticmethod
    def id_validation():
        while True:
            try:
                note_id = int(us.input_id())
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


    # @staticmethod
    # def update_validation():
    #     us.update_note()


# print(Validation().del_note_validation())
