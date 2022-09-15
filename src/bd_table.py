import sqlite3

from src.note import Note


class Table:
    def __init__(self):
        self.base = sqlite3.connect('Notebok.db', isolation_level=None)
        self.cur = self.base.cursor()

    def create_table(self):
        self.base.execute('CREATE TABLE IF NOT EXISTS notes'
                          '(Id INTEGER PRIMARY KEY, First_name TEXT NOT NULL, Last_name TEXT NOT NULL, '
                          'Number UNIQUE, Address TEXT, Born_data date)')
        self.base.commit()
        print("Connected to table")
        print(f'Numbers columns: {self.amaunt_notes()}')

    def amaunt_notes(self):
        count = self.cur.execute('SELECT COUNT(*) FROM notes')
        return count.fetchone()[0]

    def delete_table(self):
        self.base.execute('DROP TABLE IF EXISTS notes')
        self.base.commit()

    def select_table(self):
        answ = input("\nPrint table:\n1 - Order by id\n2 - Order by First name\n"
                     "3 - Order by Last name\nAny key - Exit\nYour choice: ")
        order_by_set = {1: "Id", 2: "First_name", 3: "Last_name"}
        records = self.cur.execute(f"SELECT * FROM notes ORDER BY {order_by_set[int(answ)]}")
        self.print_table(records)

    def close(self):
        self.cur.close()
        self.base.close()
        print("DB closed")
        
    @staticmethod
    def print_table(records):
        for i in records:
            print(Note(i[0], i[1], i[2], i[3], i[4], i[5]))

