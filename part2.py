import random 
 
def main(): 
    print("Welcome to Grab Food Delivery!") 
    print("-" * 40) 
     
    user_name = input("Enter your name: ") #variable name user_name and an input that asks for user's name
    address = input("Enter your delivery address: ") #variable name address and an input that asks for user's address

    #showcase to screen the food menu 
    print("\nMenu:") 
    print("1. Nasi Goreng USA - RM11.50") 
    print("2. Burger Ayam Crispy - RM6.00") 
    print("3. Nasi Lemak Ayam - RM8.00") 
    print("4. Extra Joss Mangga - RM3.50") 
    print("5. Teh Tarik - RM2.80") 
    print("6. French Fries - RM4.80") 
    print("7. Cheese Leleh - RM12.00") 
    print("0. Finish Order") 
     
    order_list = [] #create array named order_list to store user's food ordered
    total_food_price = 0.0 #set the starting total price
    
    #initiate loop with variable choice that asks for user's food selection
    while True: 
        choice = int(input("\nSelect food item (1-5) or 0 to finish: ")) 

        #if else statement for users to select food (1-7) and 0 if they want to proceed to payment 
        if choice == 0: 
            break 
        elif choice == 1: 
            order_list.append("Nasi Goreng USA") #stores in the order_list array if pick choice 1
            total_food_price += 11.50 #sets the food price for choice 1 and add to total_food_price variable
            print("Added Nasi Goreng USA") 
        elif choice == 2: 
            order_list.append("Burger Ayam Crispy") #choice 2-7 is the same concept as choice 1
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
     
    delivery_fee = 5.00 #set the delivery fee to RM5
    total_price = total_food_price + delivery_fee #variable named total_price that adds total food price and delivery fee
     
    est_time = random.randint(20, 45) #the delivery time is set as a random time from 20-45 minutes

    #prints the order summary to screen 
    print("\nOrder Summary") 
    print("-" * 40) 
    print(f"Customer: {user_name}") 
    print(f"Address: {address}") 
    print("Items Ordered:") 
    for item in order_list: #prints all the user's food selection
        print(f"- {item}") 
    print(f"\nFood Price: RM{total_food_price:.2f}") 
    print(f"Delivery Fee: RM{delivery_fee:.2f}") 
    print(f"Total: RM{total_price:.2f}") 
    print(f"Estimated Delivery Time: {est_time} minutes") 
    print("-" * 40) 
    print("Thank you for ordering with Grab!") 
 
if __name__ == "__main__": 
    main()