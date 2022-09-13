from src.note import Note
from src.bd_table import Table


class Find:
    def __init__(self, table: Table):
        self.table = table

    def find_record(self):
        line_find = input("\nFind line by:\n1 - First name\n2 - Number\n3 - Part of last name\n"
                          "Any key - back to menu\nYour choice: ")
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
        mask = input("\nEnter part of last name: ")
        record = self.table.cur.execute(f"SELECT * FROM notes WHERE Last_name LIKE '{mask.capitalize()}%'")
        for i in record.fetchall():
            print(Note(i[0], i[1], i[2], i[3], i[4], i[5]))

    def find_by_number(self):
        number1 = input("Enter number: ")
        num = self.table.cur.execute(f"SELECT * FROM notes WHERE Number == ?", (number1,))
        print(num.fetchall())

    def find_by_name(self):
        first_name1 = input("Enter first name: ")
        slct = self.table.cur.execute(f"SELECT * FROM notes WHERE First_name == ?", (first_name1.capitalize(),))
        records = slct.fetchall()
        records_line = []
        for item in records:
            records_line.append(item)
            if len(records_line) > 20:
                print("Too many matches, try search by number")
                break
        for i in records_line:
            print(Note(i[0], i[1], i[2], i[3], i[4], i[5]))