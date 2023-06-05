def display_menu():
    print("Welcome to the Liquor Store")
    print("Please select the number for your preference:")
    print("1. Hard Liquor")
    print("2. Red Wine")
    print("3. White Wine")
    print("4. Beer")
    print("5. Reset")

def calculate_total(price, quantity):
    return price * quantity

def place_order():
    name = input("Please enter your name: ")
    phone_number = input("Please enter your phone number: ")
    address = input("Please enter your address: ")
    id_number = input("Please enter your ID card number for age verification: ")

    print("Thank you for your order, " + name + "!")
    print("One of our delivery agents will contact you at " + phone_number + " for order confirmation.")
    print("Once we receive order confirmation from you, we will deliver your order to " + address + ".")
    print("Your ID card number " + id_number + " is under age verification process.")
    print("We will contact you within 30 minutes for further verification.")
    print("Thank you for your order!")

def liquor_store():
    while True:
        display_menu()
        user_input = int(input("Please enter a number: "))

        if user_input == 1:
            print("You have chosen Hard Liquor")
            print("Below are our options:")
            print("1. Vodka 750ml ($20)")
            print("2. Red Label 750ml ($25)")
            print("3. Jack Daniels 750ml ($30)")

            selection = int(input("Please enter a number: "))
            if selection == 1:
                print("You have chosen Vodka 750ml")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(20, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 2:
                print("You have chosen Red Label 750ml")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(25, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 3:
                print("You have chosen Jack Daniels 750ml")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(30, quantity)
                print("Your total is: $", total)
                place_order()
                
            else:
                print("Invalid selection")

        elif user_input == 2:
            print("You have chosen Red Wine")
            print("Below are our options:")
            print("1. Cabernet Sauvignon ($30)")
            print("2. Merlot ($25)")
            print("3. Pinot Noir ($35)")

            selection = int(input("Please enter a number: "))
            if selection == 1:
                print("You have chosen Cabernet Sauvignon")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(30, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 2:
                print("You have chosen Merlot")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(25, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 3:
                print("You have chosen Pinot Noir")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(35, quantity)
                print("Your total is: $", total)
                place_order()
                
            else:
                print("Invalid selection")

        elif user_input == 3:
            print("You have chosen White Wine")
            print("Below are our options:")
            print("1. Chardonnay ($30)")
            print("2. Sauvignon Blanc ($25)")
            print("3. Riesling ($35)")

            selection = int(input("Please enter a number: "))
            if selection == 1:
                print("You have chosen Chardonnay")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(30, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 2:
                print("You have chosen Sauvignon Blanc")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(25, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 3:
                print("You have chosen Riesling")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(35, quantity)
                print("Your total is: $", total)
                place_order()
                

        elif user_input == 4:
            print("You have chosen Beer")
            print("Below are our options:")
            print("1. Carlsberg ($10)")
            print("2. Heineken ($8)")
            print("3. Corona ($5)")

            selection = int(input("Please enter a number: "))
            if selection == 1:
                print("You have chosen Carlsberg")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(10, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 2:
                print("You have chosen Heineken")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(8, quantity)
                print("Your total is: $", total)
                place_order()
                
            elif selection == 3:
                print("You have chosen Corona")
                quantity = int(input("Please enter the quantity: "))
                total = calculate_total(5, quantity)
                print("Your total is: $", total)
                place_order()
                
        else:
            print("Invalid Number")

# Call the functions
if __name__ == "__main__":
    liquor_store()


