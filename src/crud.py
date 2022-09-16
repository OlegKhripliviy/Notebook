from sqlite3 import IntegrityError

from src.bd_table import Table
from src.validation import Validation
from src.user_interface import UserInterface


class Crud:
    def __init__(self, table: Table):
        self.table = table

    def add_one_note(self):
        try:
            record = Validation().add_note_validation()
            self.table.cur.execute('INSERT INTO notes VALUES(?,?,?,?,?,?)',
                                   (None, record[0], record[1], record[2], record[3], record[4]))
            self.table.amaunt_notes()
            tabl = self.table.cur.execute("SELECT * FROM notes WHERE Number = ?", (record[2],)).fetchall()
            return self.table.print_table(tabl)
        except IntegrityError as ex:
            print("\nException", ex)

    def del_note(self):
        amount_now = self.table.amaunt_notes()
        if Validation().menu_validation(UserInterface().del_menu(), 2) == 0:
            print("Menu is close\n")
        else:
            note_id = Validation().id_validation()
            self.table.cur.execute(f'DELETE FROM notes WHERE Id== ?', (note_id,))
            if amount_now - self.table.amaunt_notes() == 1:
                print('note was delete')
            else:
                print("You entered incorrect data")

    def update_notes(self):
        user_id = Validation().id_validation()
        try:
            self.table.cur.execute(
                f"UPDATE notes SET First_name = ?, Last_name = ?,Number = ?, Address = ?, Born_data = ? WHERE Id = ?",
                (Validation().first_name_valid(), Validation().last_name_valid(), Validation().number_valid(),
                 UserInterface().add_address(), Validation().date_valid(), user_id))
            new_note = self.table.cur.execute(f"SELECT * FROM notes WHERE Id == ?", (user_id,))
            record = new_note.fetchall()
            self.table.print_table(record)
        except IntegrityError as ex:
            print("Exception:", ex)
