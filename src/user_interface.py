def user_interface(c):
    value = None
    match c:
        case "1":
            value = input("Enter first name: ")
        case "2":
            value = input("Enter last name: ")
        case "3":
            value = input("Enter number without +38: ")
        case "4":
            value = input("Enter address: ")
        case "6":
            value = input("Enter date born(dd.mm.yyyy): ")
        case "7":
            value = input("Enter user id: ")
        case "8":
            value = input('0 - Exit\n1 - Delete by Id\nYour choice: ')
        case "9":
            value = input("\nPrint table:\n0 - Exit\n1 - Order by id\n2 - Order by First name\n"
                          "3 - Order by Last name\nYour choice: ")
        case "10":
            value = input("\nFind line by:\n0 - Exit\n1 - First name\n"
                          "2 - Number\n3 - Part of last name\nYour choice: ")
    return value
