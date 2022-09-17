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
            tabl = self.select_notes("Number", (record[2],))
            return self.table.print_table(tabl)
        except IntegrityError as ex:
            print("\nException", ex)

    def del_note(self):
        amount_now = self.amaunt_notes()
        if Validation().menu_validation(UserInterface().del_menu(), 2) == 0:
            print("Menu is close\n")
        else:
            note_id = Validation().id_validation()
            self.table.cur.execute(f'DELETE FROM notes WHERE Id== ?', (note_id,))
            if amount_now - self.amaunt_notes() == 1:
                print('Note was delete')
            else:
                print("You entered incorrect data")

    def update_notes(self):
        user_id = Validation().id_validation()
        try:
            self.table.cur.execute(
                f"UPDATE notes SET First_name = ?, Last_name = ?,Number = ?, Address = ?, Born_data = ? WHERE Id = ?",
                (Validation().first_name_valid(), Validation().last_name_valid(), Validation().number_valid(),
                 UserInterface().add_address(), Validation().date_valid(), user_id))
        except IntegrityError as ex:
            print("Exception:", ex)

    def select_notes(self, column_name, table_value):
        record = self.table.cur.execute(f'SELECT * FROM notes WHERE {column_name} = ?', (table_value,))
        record.fetchall()
        return record

    def select_order_by(self):
        menu_num = Validation().menu_validation(UserInterface().order_menu(), 4)
        if menu_num == 0:
            print("Menu is close\n")
        else:
            order_by_set = {1: "Id", 2: "First_name", 3: "Last_name"}
            records = self.table.cur.execute(f"SELECT * FROM notes ORDER BY {order_by_set[menu_num]}")
            self.table.print_table(records)

    def amaunt_notes(self):
        count = self.table.cur.execute('SELECT COUNT(*) FROM notes')
        num_row = count.fetchone()[0]
        print(f'Notes in notebook: {num_row}')
        return num_row










