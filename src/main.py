from src.notebook import Notebook


def main(notebook: Notebook):
    while True:
        menu = input('\n0 - Exit\n1 - Add new note\n2 - Delete note\n3 - Update none\n'
                     '4 - Find note\n5 - Print table\nYour choice: ')
        match menu:
            case "0":
                break
            case "1":
                notebook.add_one_note()
            case "2":
                notebook.del_note()
            case "3":
                notebook.update_notes()
            case "4":
                notebook.find_record()
            case "5":
                notebook.select_order_by()
            case _:
                print('Bye')


if __name__ == '__main__':
    nb = Notebook()
    main(nb)
