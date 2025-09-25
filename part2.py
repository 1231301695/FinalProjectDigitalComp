import random

def main():
    print("Welcome to Grab Food!")
    print("-"*40)

    user_name = input("Name: ")
    address = input("Address: ")

    menu = {
        1: ("Nasi Goreng USA", 11.50),
        2: ("Burger Ayam Crispy", 6.00),
        3: ("Nasi Lemak Ayam", 8.00),
        4: ("Extra Joss Mangga", 3.50),
        5: ("Teh Tarik", 2.80),
        6: ("French Fries", 4.80),
        7: ("Cheese Leleh", 12.00)
    }
    