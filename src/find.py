from src.validation import Validation
from src.crud import Crud
from src.user_interface import UserInterface


class Find:
    def __init__(self):
        pass

    def find_record(self):
        line_find = Validation().menu_validation(UserInterface().user_interface("10"), 4)
        match line_find:
            case "1":
                self.find_by_name()
            case "2":
                self.find_by_number()
            case "3":
                self.find_by_mask()
            case _:
                pass

    @staticmethod
    def find_by_mask():
        last_name = Validation().last_name_valid()
        record = Crud().select_notes("Last_name", last_name)
        UserInterface().print_table(record)

    @staticmethod
    def find_by_number():
        number = Validation().number_valid()
        record = Crud().select_notes("Number", number)
        UserInterface().print_table(record)

    @staticmethod
    def find_by_name():
        first_name = Validation().first_name_valid()
        record = Crud().select_notes("First_name", first_name)
        UserInterface().print_table(record)

