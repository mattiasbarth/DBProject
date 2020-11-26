import Controllers.customer_controller as cc
from UI.tools import int_input


def add_new_customer():
    pass


def find_customer():
    pass


def show_customer(chosen_customer):
    print("     KUNDBILD     ")
    print("------------------")
    print(f"Namn: {chosen_customer.name} ({chosen_customer.customer_type})")
    if chosen_customer.contact_person:
        print(f"Kontaktperson{chosen_customer.contact_person}")
    print(f"Address: {chosen_customer.street_addres}")
    print(f"Postkod: {chosen_customer.zip_code}")
    print(f"Email: {chosen_customer.email}")
    print(f"Telefonnummer: {chosen_customer.phone}")
    print(f"Ordrar: {chosen_customer.orders}")
    print(f"Bilar: {chosen_customer.customer_cars}")
    show_customer_menu(chosen_customer)


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
