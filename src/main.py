from src.crud import Crud
from src.find import Find
from src.bd_table import Table


def main():
    # bk.delete_table()
    table.create_table()
    while True:
        menu = input('\n0 - Exit\n1 - Add new note\n2 - Delete note\n3 - Update none\n'
                     '4 - Find note\n5 - Print table\nYour choice: ')
        match menu:
            case "0":
                break
            case "1":
                print(crud.add_one_note())
            case "2":
                crud.del_note()
            case "3":
                crud.update_notes()
            case "4":
                find.find_record()
            case "5":
                table.select_table()
            case _:
                pass


if __name__ == '__main__':
    table = Table()
    find = Find(table)
    crud = Crud(table)
    main()
