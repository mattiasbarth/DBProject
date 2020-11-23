from Controllers.employee_controller import *

def employees_menu():
    while True:
        print("ANSTÄLLDA".rjust(13))
        print("-----------------")
        print("1. Redigera/ta bort")
        print("2. Lägg till")
        print("3. Huvudmeny")

        selected = input("> ")
        if selected == "1":
            search = input("Sök: ")
            find_employee(search)
        elif selected == "2":
            print("Ange uppgifter på den anställda du vill lägga till")
            e_store = input("Butik: ")
            e_name = input("Namn: ")
            e_phone = input("Telefon: ")
            e_email = input("Email: ")
            e_job_title = input("Job title: ")
            e = (e_store, e_name, e_phone, e_email, e_job_title)
            add_employee(e)
        elif selected == "3":
            pass
            #main_menu()
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")

employees_menu()