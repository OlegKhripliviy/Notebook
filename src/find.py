from src.bd_table import Table
from src.validation import Validation
from src.crud import Crud
from src.user_interface import UserInterface


class Find:
    def __init__(self, table: Table):
        self.table = table

    def find_record(self):
        line_find = Validation().menu_validation(UserInterface().find_menu(), 4)
        match line_find:
            case "1":
                self.find_by_name()
            case "2":
                self.find_by_number()
            case "3":
                self.find_by_mask()
            case _:
                pass

    def find_by_mask(self):
        last_name = Validation().last_name_valid()
        record = Crud(self.table).select_notes("Last_name", last_name)
        self.table.print_table(record)

    def find_by_number(self):
        number = Validation().number_valid()
        record = Crud(self.table).select_notes("Number", number)
        self.table.print_table(record)

    def find_by_name(self):
        first_name = Validation().first_name_valid()
        record = Crud(self.table).select_notes("First_name", first_name)
        self.table.print_table(record)

