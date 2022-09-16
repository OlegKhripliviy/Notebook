from datetime import datetime
from src.user_interface import UserInterface

us = UserInterface()


class Validation:
    def __init__(self):
        pass

    @staticmethod
    def name_valid(name):
        if len(name) < 2 or not name.isalpha():
            print("First or last name is too short or has number. Try again\n")
            return False
        else:
            return True

    @staticmethod
    def number_valid(number):
        if len(number) != 10 or not number.isdigit():
            print("Incorrect input phone number. Try again\n")
            return False
        else:
            return True

    @staticmethod
    def date_valid(date):
        try:
            if datetime.strptime(date, '%m.%d.%Y'):
                return date
        except ValueError:
            print("Invalid data. Try again")
            return False

    def add_note_validation(self):
        records = us.add_note_interface()
        if not self.name_valid(records["first_name"]):
            self.add_note_validation()
        elif not self.name_valid(records["last_name"]):
            self.add_note_validation()
        elif not self.number_valid(records["number"]):
            self.add_note_validation()
        if not self.date_valid(records["date"]):
            self.add_note_validation()
        return records


print(Validation().add_note_validation())
