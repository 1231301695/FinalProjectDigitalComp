import random

def main():
    print("Welcome to Grab Food Delivery!")
    print("-" * 40)
    
    user_name = input("Enter your name: ")
    address = input("Enter your delivery address: ")

    print("\nMenu:")
    print("1. Nasi Goreng USA - RM11.50")
    print("2. Burger Ayam Crispy - RM6.00")
    print("3. Nasi Lemak Ayam - RM8.00")
    print("4. Extra Joss Mangga - RM3.50")
    print("5. Teh Tarik - RM2.80")
    print("6. French Fries - RM4.80")
    print("7. Cheese Leleh - RM12.00")
    print("0. Finish Order")

    order_list = []

    while True:
            choice = int(input("\nSelect food item (1-5) or 0 to finish: "))

            if choice == 0:
                break
            elif choice == 1:
                order_list.append("Nasi Goreng USA")
                print("Added Nasi Goreng USA")
            elif choice == 2:
                order_list.append("Burger Ayam Crispy")
                print("Added Burger Ayam Crispy")
            elif choice == 3:
                order_list.append("Nasi Lemak Ayam")
                print("Added Nasi Lemak Ayam")
            elif choice == 4:
                order_list.append("Extra Joss Mangga")
                print("Added Extra Joss Mangga")
            elif choice == 5:
                order_list.append("Teh Tarik")
                print("Added Teh Tarik")
            elif choice == 6:
                order_list.append("French Fries")
                print("Added French Fries")
            elif choice == 7:
                order_list.append("Cheese Leleh")
                print("Added Cheese Leleh")
            else:
                print("Invalid choice, please try again.")