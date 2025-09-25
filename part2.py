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
    total_food_price = 0.0

    while True:
            choice = int(input("\nSelect food item (1-5) or 0 to finish: "))

            if choice == 0:
                break
            elif choice == 1:
                order_list.append("Nasi Goreng USA")
                total_food_price += 11.50
                print("Added Nasi Goreng USA")
            elif choice == 2:
                order_list.append("Burger Ayam Crispy")
                total_food_price += 6.00
                print("Added Burger Ayam Crispy")
            elif choice == 3:
                order_list.append("Nasi Lemak Ayam")
                total_food_price += 8.00
                print("Added Nasi Lemak Ayam")
            elif choice == 4:
                order_list.append("Extra Joss Mangga")
                total_food_price += 3.50
                print("Added Extra Joss Mangga")
            elif choice == 5:
                order_list.append("Teh Tarik")
                total_food_price += 2.80
                print("Added Teh Tarik")
            elif choice == 6:
                order_list.append("French Fries")
                total_food_price += 4.80
                print("Added French Fries")
            elif choice == 7:
                order_list.append("Cheese Leleh")
                total_food_price += 12.00
                print("Added Cheese Leleh")
            else:
                print("Invalid choice, please try again.")

    delivery_fee = 5.00
    total_price = total_food_price + delivery_fee

    est_time = random.randint(20, 45)