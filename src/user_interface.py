class UserInterface:
    def __init__(self):
        self.value = None

    def user_interface(self, c):
        match c:
            case "first_name":
                self.value = input("Enter first name: ")
            case "last_name":
                self.value = input("Enter last name: ")
            case "number":
                self.value = input("Enter number without +38: ")
            case "address":
                self.value = input("Enter address: ")
            case "date":
                self.value = input("Enter date born(dd.mm.yyyy): ")
            case "id":
                self.value = input("Enter user id: ")
            case "del_menu":
                self.value = input('0 - Exit\n1 - Delete by Id\nYour choice: ')
            case "order_by_menu":
                self.value = input("\nPrint table:\n0 - Exit\n1 - Order by id\n2 - Order by First name\n"
                                   "3 - Order by Last name\nYour choice: ")
            case "find_menu":
                self.value = input("\nFind line by:\n0 - Exit\n1 - First name\n"
                                   "2 - Number\n3 - Part of last name\nYour choice: ")
            case _:
                print("Menu closed")
        return self.value

    @staticmethod
    def print_table(records):
        for i in records:
            text = ""
            text += f'Id= {i[0]}. First name: {i[1]}, Last_name: {i[2]}, Number: {i[3]}'
            if i[4] is None or len(i[4]) > 2:
                text += f' ,Address: {i[4]}'
            if i[5] is None or len(str(i[5])) > 5:
                text += f' ,Birth data: {i[5]}'
            print(text)
