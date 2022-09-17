import sqlite3


class Table:
    def __init__(self):
        self.base = sqlite3.connect('Notebok.db')
        self.cur = self.base.cursor()

    def create_table(self):
        self.base.execute('CREATE TABLE IF NOT EXISTS notes'
                          '(Id INTEGER PRIMARY KEY, First_name TEXT NOT NULL, Last_name TEXT NOT NULL, '
                          'Number UNIQUE, Address TEXT, Born_data date)')
        print("Connected to table")

    def delete_table(self):
        self.base.execute('DROP TABLE IF EXISTS notes')
        self.base.commit()

    def close(self):
        self.cur.close()
        self.base.close()
        print("DB closed")


