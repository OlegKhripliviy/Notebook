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
        self.table.print_table(record)

    def find_by_number(self):
        number1 = input("Enter number: ")
        record = self.table.cur.execute(f"SELECT * FROM notes WHERE Number == ?", (number1,)).fetchall()
        self.table.print_table(record)

    def find_by_name(self):
        first_name1 = input("Enter first name: ")
        slct = self.table.cur.execute(f"SELECT * FROM notes WHERE First_name == ?", (first_name1.capitalize(),))
        records = slct.fetchall()
        self.table.print_table(records)