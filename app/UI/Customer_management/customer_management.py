from UI.tools import int_input
import Controllers.customer_controller as cc


def add_new_customer():
    pass


def find_customer_menu():
    while True:
        print("----------------------")
        print("SÖK UPP BEFINTLIG KUND")
        print("1. Sök efter namn")
        print("2. Sök efter id")
        print("3. Sök efter telefonnummer")
        print("4. Avbryt")

        choice = input("> ")

        if choice == "1":
            keyword = input("Ange namn: ")
            customers = cc.find_customer_by_name(keyword)
            choose_customer(customers)
            break

        elif choice == "2":
            keyword = int_input("Ange id: ")
            customer = cc.find_customer_by_id(keyword)
            if customer:
                print(customer)
                show_customer(customer)
            else:
                print("Det finns ingen kund som uppfyller sökkraven.")
            break

        elif choice == "3":
            keyword = input("Ange telefonnumer: ")
            customers = cc.find_customer_by_phone(keyword)
            choose_customer(customers)
            break

        elif choice == "4":
            break

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def choose_customer(customers):
    if customers:
        if len(customers) == 1:
            print(customers[0])
            show_customer(customers[0])

        else:
            print("Matchande sökningar:")
            for i, customer in enumerate(customers):
                print(f"{i + 1}. {customer}")

            while True:
                customer_choice = int_input("Vilken kund vill du visa?")
                if 1 <= customer_choice <= len(customers):
                    customer = customers[customer_choice - 1]
                    show_customer(customer)
                    break
                else:
                    print("Du har gjort ett ogiltigt val. Försök igen.")

    else:
        print("Det finns ingen kund som uppfyller sökkraven.")



def show_customer(customer):
    # Kontaktuppgifter
    # Ordrar
    # Bilar
    pass


def show_customer_menu():
    while True:
        find_customer()
        add_new_customer()
    pass


def add_car():
    pass


def edit_customer():
    pass


def remove_customer():
    pass


def add_order():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
