def customer_management_menu():
    while True:
        print("Kundhantering")
        print("----------------------")
        print("1. Sök upp befintlig kund")
        print("2. Lägg till ny kund")
        print("3. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            find_customer()
        elif selected == "2":
            add_new_customer()
        elif selected == "3":
            main_menu()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")