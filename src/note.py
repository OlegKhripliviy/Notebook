from src.user_interface import UserInterface
from src.validation import Validation
from src.bd_table import Table

table = Table()


class Palas:
    def __init__(self):
        self.table = Table

    def del_note(self):
        amount_now = table.amaunt_notes()
        if Validation().menu_validation(UserInterface().del_menu(), 2) == 0:
            print("fiasko")
        else:
            note_id = Validation().id_validation()

            table.cur.execute(f'DELETE FROM notes WHERE Id== ?', (note_id,))
            if amount_now - table.amaunt_notes() == 1:
                print(f'Note was deleted\nNotes in notebook: {table.amaunt_notes()}\n')
            else:
                print("You entered incorrect data")

Palas().del_note()
