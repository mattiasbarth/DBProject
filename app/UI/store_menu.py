import Controllers.store_controller as cs
from UI.tools import int_input


def store_menu():
    while True:
        print("BUTIKER")
        print("----------------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Gå tillbaka till adminmeny")

        selected = input("> ")
        if selected == "1":
            search_and_choose()

        elif selected == "2":
            add_store()

        elif selected == "3":
            break

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def search_and_choose():
    while True:
        keyword = input("Sök butik efter namn: ")
        stores = cs.find_store(keyword)

        if len(stores) == 0:
            print("Det finns ingen butik som upfyller sökkraven.")
        else:
            print("Matchande sökningar:")
            for i, store in enumerate(stores):
                print(f"{i + 1}. {store}")

            while True:
                choice = int_input("Vilken butik vill du visa? ")
                if 1 <= choice <= len(stores):
                    store = stores[choice - 1]
                    break
                else:
                    print("Du har gjort ett ogiltigt val. Försök igen.")

            edit_remove_menu(store)
            break


def edit_remove_menu(store):
    while True:
        print(f"Vad vill du göra med butiken {store}")
        print("1. Redigera")
        print("2. Ta bort")
        print("3. Avbryt")

        action = input("> ")

        if action == "1":
            edit_store(store)
        elif action == "2":
            remove_store(store)
            break
        elif action == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def edit_store(store):
    while True:
        print("----------------------")
        print("REDIGERA BUTIK")
        print(f"1. Namn: {store.name}")
        print(f"2. Gatuadress: {store.street_address}")
        print(f"3. Postkod: {store.zip_code}")
        print(f"4. Stad: {store.city}")
        print(f"5. Telefonnummer: {store.phone}")
        print(f"6. Email: {store.email}")
        print("Vilken rad vill du redigera?")

        edit_line = input("> ")

        if edit_line == "1":
            new_value = input("Ange nytt namn: ")
            store.name = new_value
            cs.store_changes(store)

        elif edit_line == "2":
            new_value = input("Ange ny gatuadress: ")
            store.street_address = new_value
            cs.store_changes(store)

        elif edit_line == "3":
            new_value = input("Ange ny postkod: ")
            store.zip_code = new_value
            cs.store_changes(store)

        elif edit_line == "4":
            new_value = input("Ange ny stad: ")
            store.city = new_value
            cs.store_changes(store)

        elif edit_line == "5":
            new_value = input("Ange nytt telefonnummer: ")
            store.phone = new_value
            cs.store_changes(store)

        elif edit_line == "6":
            new_value = input("Ange ny email: ")
            store.email = new_value
            cs.store_changes(store)

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def remove_store(store):
    while True:
        print("----------------------")
        print("TA BORT BUTIK")
        action = input(f"Är du säker på att du vill ta bort {store}? J/N > ")

        if action.lower() == "j":
            if not store.employees:
                cs.remove_store(store)
            else:
                print(f"Du får inte ta bort butiken {store} eftersom det finns tillhörande anställda. "
                      f"Ta bort eller flytta dessa innan du försöker igen.")

        elif action.lower() == "n":
            print("Butiken har inte tagits bort.")
            break

        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def add_store():
    print("----------------------")
    print("LÄGG TILL BUTIK")
    print("Besvara följande frågor:")
    name = input("Butikens namn: ")
    street_address = input("Gatuadress: ")
    zip_code = input("Postkod: ")
    city = input("Stad: ")
    phone = input("Telefonnummer: ")
    email = input("Emailadress: ")

    store_data = (name, street_address, zip_code, city, phone, email)
    cs.add_store(store_data)


def main():
    store_menu()


if __name__ == "__main__":
    main()
