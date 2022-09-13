from sqlite3 import IntegrityError

from src.bd_table import Table
from src.note import Note


class Crud:
    def __init__(self, table: Table):
        self.table = table

    def add_one_note(self):
        try:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            number = input("Enter number: ")
            address = input("Enter addres: ")
            date = input("Enter date born: ")
            if len(first_name) == 0 or len(last_name) == 0 or len(number) == 0:
                first_name, last_name, number = None, None, None
            else:
                first_name, last_name = first_name.capitalize(), last_name.capitalize()
            self.table.cur.execute(
                'INSERT INTO notes VALUES(?,?,?,?,?,?)', (None, first_name, last_name, number, address, date))
            print("\nNote added:")
            print(f'Notes in notebook: {self.table.amaunt_notes()}')
            indx = self.table.cur.execute("SELECT Id FROM notes WHERE First_name == ? AND Number = ?",
                                          (first_name, number,))
            idx = indx.fetchone()[0]
            return Note(idx=idx, first_name=first_name, last_name=last_name, number=number, address=address,
                        date=date)
        except IntegrityError as ex:
            print("\nException", ex)

    def del_note(self):
        amount_now = self.table.amaunt_notes()
        what_del = input('1 - Delete by first name\n2 - Delete by number\nAny key - Exit\n')
        match what_del:
            case '1':
                del_name = input("Enter first name: ")
                self.table.cur.execute(f'DELETE FROM notes WHERE First_name == ?', (del_name.capitalize(),))
            case '2':
                del_num = input("Enter number: ")
                self.table.cur.execute(f'DELETE FROM notes WHERE Number == ?', (del_num,))
            case _:
                pass
        if amount_now - self.table.amaunt_notes() == 1:
            print('note was deleted')
            print(f'Notes in notebook: {self.table.amaunt_notes()}')
        else:
            print("Нou entered incorrect data")

    def update_notes(self):
        line_update = input("Enter the note number to update: ")
        print("\nWhat attribute do you want to change:\n"
              "1 - First name\n2 - Last name\n3 - Number\n4 - Address\n5 - Date of Birth\n")
        what_to_update = input("Your choice: ")
        try:
            match what_to_update:
                case "1":
                    val = input("Enter new first name: ")
                    if len(val) == 0:
                        val = None
                    self.table.cur.execute("UPDATE notes SET First_name == ? WHERE Id == ?", (val, line_update,))
                case "2":
                    val = input("Enter new last name: ")
                    if len(val) == 0:
                        val = None
                    self.table.cur.execute(f"UPDATE notes SET Last_name == ? WHERE Id == ?", (val, line_update,))
                case "3":
                    val = input("Enter new number: ")
                    if len(val) == 0:
                        val = None
                    self.table.cur.execute("UPDATE notes SET Number == ? WHERE Id == ?", (val, line_update,))
                case "4":
                    val = input("Enter new adress: ")
                    self.table.cur.execute("UPDATE notes SET Address == ? WHERE Id == ?", (val, line_update,))
                case "5":
                    val = input("Enter new birth date ")
                    self.table.cur.execute("UPDATE notes SET Born_data == ? WHERE Id == ?", (val, line_update,))
                case _:
                    pass
        except IntegrityError as ex:
            print("Exception:", ex)
