def main_menu():
    while True:
        print("Huvudmeny")
        print("----------------------")
        print("1. Admin")
        print("2. Kundhantering")
        print("3. Avsluta")

        selected = input("> ")
        if selected == "1":
            admin_menu()
        elif selected == "2":
            customer_management()
        elif selected == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")
