class UserInterface:
    def __init__(self):
        self.value = None

    def user_interface(self, c):
        match c:
            case "1":
                self.value = input("Enter first name: ")
            case "2":
                self.value = input("Enter last name: ")
            case "3":
                self.value = input("Enter number without +38: ")
            case "4":
                self.value = input("Enter address: ")
            case "6":
                self.value = input("Enter date born(dd.mm.yyyy): ")
            case "7":
                self.value = input("Enter user id: ")
            case "8":
                self.value = input('0 - Exit\n1 - Delete by Id\nYour choice: ')
            case "9":
                self.value = input("\nPrint table:\n0 - Exit\n1 - Order by id\n2 - Order by First name\n"
                                   "3 - Order by Last name\nYour choice: ")
            case "10":
                self.value = input("\nFind line by:\n0 - Exit\n1 - First name\n"
                                   "2 - Number\n3 - Part of last name\nYour choice: ")
            case _:
                print("Menu closed")
        return self.value

    @staticmethod
    def print_table(records):
        for i in records:
            print(i)
            text = ""
            text += f'Id= {i[0]}. First name: {i[1]}, Last_name: {i[2]}, Number: {i[3]}'
            if i[4] is None or len(i[4]) > 2:
                text += f' ,Address: {i[4]}'
            if i[5] is None or len(str(i[5])) > 5:
                text += f' ,Birth data: {i[5]}'
            print(text)
