from Controllers.store_controller import search_store


def store_menu():
    while True:
        print("BUTIKER")
        print("----------------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Adminmeny")

        selected = input("> ")
        if selected == "1":
            keyword = input("Sök butik efter namn: ")
            stores = search_store(keyword)
            for key, store in stores.items():
                print(f"{key}. {store}")

            store_selection = input("Vilken butik vill du visa? ")

        elif selected == "2":
            pass
        elif selected == "3":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")