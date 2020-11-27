import Controllers.customer_controller as cc
import Controllers.contact_person_controller as ccp
from UI.tools import int_input


def add_new_customer():
    print("----------------------")
    print("LÄGG TILL KUND")
    print("Besvara följande frågor:")

    name = input("Kundens namn: ")
    street_address = input("Gatuadress: ")
    zip_code = input("Postkod: ")
    city = input("Stad: ")
    phone = input("Telefonnummer: ")
    email = input("Email: ")
    customer_type = int_input("Kundtyp: ange 1 för privatkund och 2 för företagskund: ")
    if customer_type == 2:
        while True:
            contact_id = int_input("Kontaktpersonens id: ")
            if not ccp.find_contact_person:
                print(f"Hittade ingen kontaktperson med id {contact_id}")
            else:
                break

        customer_data = (name, street_address, zip_code, city, phone, email, customer_type, contact_id)
        customer, info_string = cc.add_business(customer_data)

    else:
        customer_data = (name, street_address, zip_code, city, phone, email, customer_type)
        customer, info_string = cc.add_private(customer_data)

    print(info_string)
    show_customer(customer)


def show_customer(chosen_customer):
    print("     KUNDBILD     ")
    print("------------------")
    print(f"Namn: {chosen_customer.name} ({chosen_customer.customer_type})")
    if chosen_customer.contact_person:
        print(f"Kontaktperson {chosen_customer.contact_person}")
    print(f"Address: {chosen_customer.street_address}")
    print(f"Postkod: {chosen_customer.zip_code}")
    print(f"Email: {chosen_customer.email}")
    print(f"Telefonnummer: {chosen_customer.phone}")
    print(f"Ordrar: {chosen_customer.orders}")
    print(f"Bilar: {chosen_customer.customer_cars}")
    show_customer_menu(chosen_customer)

    
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
                    chosen_customer = customers[customer_choice - 1]
                    show_customer(chosen_customer)
                    break
                else:
                    print("Du har gjort ett ogiltigt val. Försök igen.")

    else:
        print("Det finns ingen kund som uppfyller sökkraven.")


def show_customer_menu(chosen_customer):
    while True:
        print("------------------")
        print(f"Vad vill du göra med {chosen_customer}")
        print("1. Redigera kunden")
        print("2. Lägg till bil")
        print("3. Ta bort bil")
        print("3. Lägg till order")
        print("4. Ta bort kunden")
        print("5. Avbryt")
        selected = input("> ")
        if selected == "1":
            edit_customer(chosen_customer)
        elif selected == "2":
            add_car(chosen_customer)
        elif selected == "3":
            #TODO om en kund säljer sin bil
            pass
        elif selected == "4":
            add_order(chosen_customer)
        elif selected == "5":
            remove_customer(chosen_customer)
        elif selected == "6":
            break
        else:
            print("Felaktig inmatning")


def add_car(chosen_customer):
    pass


def edit_customer(chosen_customer):
    while True:
        print("--------------")
        print(f"REDIGERA KUND")
        print(f"1. Namn: {chosen_customer.name}")
        print(f"2. Address: {chosen_customer.store}")
        print(f"3. Postkod: {chosen_customer.phone}")
        print(f"4. Email: {chosen_customer.email}")
        print(f"5. Telefonnummer: {chosen_customer.job_title}")
        if chosen_customer.contact_person:
            print(f"6. {chosen_customer.contact_person}")
        print(f"7. Avbryt")
        print(f"Vilken rad vill du redigera?")
        selected = input("> ")

        if selected == "1":
            chosen_customer.name = input("Ange nytt namn: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "2":
            chosen_customer.name = input("Ange ny address): ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "3":
            chosen_customer.name = input("Ange ny postkod: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "4":
            chosen_customer.name = input("Ange ny mail: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "5":
            chosen_customer.name = input("Ange nytt telefonnummer: ")
            cc.save_changes(chosen_customer)
            changed_string = cc.save_changes(chosen_customer)
            print(changed_string)

        elif selected == "6":
            break
        else:
            print("Felaktig inmatning")


def remove_customer(chosen_customer):
    pass


def add_order(chosen_customer):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
