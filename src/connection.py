import sqlite3


def cur():
    with sqlite3.connect('Notebok.db', isolation_level=None) as base:
        cursor = base.cursor()
        return cursor
