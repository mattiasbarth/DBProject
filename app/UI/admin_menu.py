from UI.employee_menu import employees_menu


def admin_menu():
    while True:
        print("ADMIN")
        print("----------------------")
        print("1. Butiker")
        print("2. Anställda")
        print("3. Ordrar")
        print("10. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            pass
        elif selected == "2":
            employees_menu()
        elif selected == "3":
            pass
        elif selected == "10":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")
