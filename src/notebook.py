import sqlite3

from src.validation import Validation
from src.user_interface import UserInterface
from src.connection import cur


class Notebook:
    def __init__(self):
        self.note_list = []

    def add_one_note(self):
        try:
            record = self.add_validation_note()
            cur().execute('INSERT INTO notes VALUES(?,?,?,?,?,?)',
                          (None, record[0], record[1], record[2], record[3], record[4]))
            tabl = self.select_notes("Number", record[2])
            return UserInterface().print_table(tabl)
        except sqlite3.IntegrityError as ex:
            print("\nException", ex)

    def add_validation_note(self):
        self.note_list.append(Validation().first_name_valid())
        self.note_list.append(Validation().last_name_valid())
        self.note_list.append(Validation().number_valid())
        self.note_list.append(Validation().address_valid())
        self.note_list.append(Validation().date_valid())
        return self.note_list

    def del_note(self):
        amount_now = self.amount_notes()
        menu_num = Validation().menu_valid(UserInterface().user_interface("del_menu"), 2)
        if menu_num == "0":
            print("Menu closed\n")
        else:
            note_id = Validation().id_valid()
            cur().execute(f'DELETE FROM notes WHERE Id== ?', (note_id,))
            if amount_now - self.amount_notes() == 1:
                print('Note was delete')
            else:
                print("You entered incorrect data")

    @staticmethod
    def update_notes():
        user_id = Validation().id_valid()
        try:
            cur().execute(
                f"UPDATE notes SET First_name = ?, Last_name = ?,Number = ?, Address = ?, Born_data = ? WHERE Id = ?",
                (Validation().first_name_valid(), Validation().last_name_valid(), Validation().number_valid(),
                 Validation().address_valid(), Validation().date_valid(), user_id))
            print("Note updated")
        except sqlite3.IntegrityError as ex:
            print("Exception:", ex)

    @staticmethod
    def select_notes(column_name, table_value):
        record = cur().execute(f'SELECT * FROM notes WHERE {column_name} == ?', (table_value,))
        return record.fetchall()

    @staticmethod
    def select_by_mask(column_name, table_value):
        record = cur().execute(f'SELECT * FROM notes WHERE {column_name} LIKE "{table_value}%"')
        return record.fetchall()

    @staticmethod
    def select_order_by():
        menu_num = Validation().menu_valid(UserInterface().user_interface("order_by_menu"), 4)
        if menu_num == "0":
            print("Menu is close")
        else:
            order_by_set = {1: "Id", 2: "First_name", 3: "Last_name"}
            records = cur().execute(f"SELECT * FROM notes ORDER BY {order_by_set[int(menu_num)]}")
            UserInterface().print_table(records)

    @staticmethod
    def amount_notes():
        count = cur().execute('SELECT COUNT(*) FROM notes')
        num_row = count.fetchone()[0]
        print(f'\nNotes in notebook: {num_row}')
        return num_row

    def find_record(self):
        line_find = Validation().menu_valid(UserInterface().user_interface("find_menu"), 4)
        match line_find:
            case "1":
                self.find_by_name()
            case "2":
                self.find_by_number()
            case "3":
                self.find_by_mask()
            case _:
                print("Menu closed")

    def find_by_mask(self):
        last_name = Validation().last_name_valid()
        record = self.select_by_mask("Last_name", last_name)
        UserInterface().print_table(record)

    def find_by_number(self):
        number = Validation().number_valid()
        record = self.select_notes("Number", number)
        UserInterface().print_table(record)

    def find_by_name(self):
        first_name = Validation().first_name_valid()
        record = self.select_notes("First_name", first_name)
        UserInterface().print_table(record)
