def admin_menu():
    while True:
        print("Admin")
        print("----------------------")
        print("1. Butiker")
        print("2. Anställda")
        print("3. Ordrar")
        print("10. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            store_menu()
        elif selected == "2":
            employee_menu()
        elif selected == "3":
            order_menu()
        elif selected == "10":
            main_menu()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")