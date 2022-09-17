from src.crud import Crud
from src.find import Find


def main():
    while True:
        menu = input('\n0 - Exit\n1 - Add new note\n2 - Delete note\n3 - Update none\n'
                     '4 - Find note\n5 - Print table\nYour choice: ')
        match menu:
            case "0":
                break
            case "1":
                crud.add_one_note()
            case "2":
                crud.del_note()
            case "3":
                crud.update_notes()
            case "4":
                find.find_record()
            case "5":
                crud.select_order_by()
            case _:
                pass


if __name__ == '__main__':
    find = Find()
    crud = Crud()
    main()
