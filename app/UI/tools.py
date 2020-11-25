import os

def int_input(user_input):
    while True:
        data = input(user_input)
        if data.isdigit():
            return int(data)
        else:
            print("Ditt svar måste vara ett heltal.")


def price_input(user_input):
    while True:
        data = input(user_input)
        try:
            return float(data)
        except ValueError:
            print("Ditt svar måste vara numeriskt.")