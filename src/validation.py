from datetime import datetime
from src.user_interface import UserInterface

Us = UserInterface()


class Validation:
    def __init__(self):
        pass

    @staticmethod
    def first_name_valid():
        while True:
            first_name = Us.user_interface("first_name")
            if len(first_name) < 2 or not first_name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return first_name.capitalize()

    @staticmethod
    def last_name_valid():
        while True:
            last_name = Us.user_interface("last_name")
            if len(last_name) < 2 or not last_name.isalpha():
                print("Too short or has number. Try again\n")
            else:
                return last_name.capitalize()

    @staticmethod
    def number_valid():
        while True:
            number = Us.user_interface("number")
            if len(number) != 10 or not number.isdigit():
                print("Incorrect input phone number. Try again\n")
            else:
                return number

    @staticmethod
    def date_valid():
        while True:
            date = Us.user_interface("date")
            if len(date) == 0:
                break
            try:
                if datetime.strptime(date, '%d.%m.%Y'):
                    return date
            except ValueError:
                print("Invalid data. Try again")

    @staticmethod
    def id_valid():
        while True:
            try:
                note_id = int(Us.user_interface("id"))
                return note_id
            except ValueError:
                print("You didn't enter a number. Try again")

    @staticmethod
    def address_valid():
        while True:
            address = Us.user_interface("address")
            if len(address) == 0:
                break
            return address

    @staticmethod
    def menu_valid(menu, menu_len: int):
        try:
            if menu == '0':
                return menu
            elif int(menu) not in range(1, menu_len + 1):
                print("Unknown command. Try again")
            else:
                return menu
        except ValueError:
            print("You didn't enter a number. Try again")
            return 0
