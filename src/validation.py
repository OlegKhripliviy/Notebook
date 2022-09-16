from datetime import datetime
from src.user_interface import UserInterface

us = UserInterface()


class Validation:
    def __init__(self):
        self.note_list = []

    @staticmethod
    def first_name_valid():
        while True:
            name = us.add_first_name()
            if len(name) < 2 or not name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return name

    @staticmethod
    def last_name_valid():
        while True:
            name = us.add_last_name()
            if len(name) < 2 or not name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return name

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


    def del_note_validation(self):
        while True:
            del_or_ex = us.input_del_or_ex()
            if del_or_ex != '0' and del_or_ex != '1':
                print("Unknown command. Try again")
            elif del_or_ex == '0':
                break
            try:
                note_id = int(us.input_id())
                return note_id
            except ValueError:
                print("You didn't enter a number. Try again")


print(Validation().del_note_validation())
