from UI.Customer_management.customer_management import find_customer_menu, add_new_customer


def customer_management_menu():
    while True:
        print("     KUNDHANTERING    ")
        print("----------------------")
        print("1. Sök upp befintlig kund")
        print("2. Lägg till ny kund")
        print("3. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            find_customer_menu()
        elif selected == "2":
            add_new_customer()
        elif selected == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")