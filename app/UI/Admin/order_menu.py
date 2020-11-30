from Controllers import order_controller


# admin / order
def order_menu():
    while True:
        print("Ordrar")
        print("-" * 12)
        print("1. Lägg till")
        print("2. Sök")
        print("3. Redigera/ta bort")
        print("4. Adminmeny")

        selected = input("> ")
        if selected == "1":
            create_order()
        elif selected == "2":
            find_order()
        elif selected == "3":
            edit_order()
        elif selected == "4":
            break
        else:
            print("Du har gjort ett ogiltigt val. Försök igen.")


def create_order():
    print('-' * 12)
    print('Lägg till order')
    order_data = {}
    while True:
        order_data['customer_id'] = int(input('Kund-id: '))
        order_data['employee_id'] = int(input('Medarbetar-id: '))
        order_data['store_id'] = int(input('Butiks-id: '))
        order_data['status'] = 'active'  # TODO: Use enum and default?
        order_data['comment'] = input('Kommentar: ')
        order = order_controller.create(**order_data)
        if order:
            print('Lägg till produkter')
            print('-' * 12)
            while True:
                product_id = int(input('Produkt-id: '))
                product_amount_str = input('Antal (1 är förvalt): ').strip()
                product_amount = (1 if not product_amount_str.isdigit()
                                  else int(product_amount_str))
                try:
                    # Try to add product to order.
                    order_controller.add_product(order, (product_id, product_amount))
                except Exception as e:
                    print(e)
                # products.append((product_id, product_amount))  # TODO: Enable user to search products
                if input('Lägg till fler produkter? j/n ').lower() == 'j':
                    continue
                break
            break
        print('Kunde inte skapa order. Försök igen.')
    print('Ny order skapad: ')


def edit_order():
    pass


def find_order():
    while True:
        order_id = int(input('\nAnge ordernummer: '))
        order = order_controller.find(order_id)
        if order:
            print(order)
        else:
            print(f'Kunde inte hitta order med ordernummer {order_id}')
        if input('\nSök igen? j/n ').lower() != 'j':
            break
    print('')


def remove_order():
    while True:
        order_id = int(input('\nAnge ordernummer: '))
        order = order_controller.find(order_id)
        print(order, end='\n\n')
        if input(f'Bekräfta borttagning av order? j/n ').lower() == 'j':
            is_removed = order_controller.remove(order_id)
            if is_removed:
                print(f'Order med ordernummer {order_id} har tagits bort.')
            else:
                print(f'Kunde inte hitta order med ordernummer {order_id}')
        else:
            print('Åtgärden avbruten.')
        if input('\nTa bort annan order? j/n ').lower() != 'j':
            break
    print('')
    return order_controller.remove(order_id)
