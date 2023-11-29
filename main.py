import sqlite3
from inventory import Inventory
from userClass import User
from cart import Cart

#instances of the classes
Inventory = Inventory()
User = User()
Cart = Cart()


#main


if __name__ == "__main__":
    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            loginSuccess = User.login()
            if not loginSuccess:
                continue
        elif choice == "2":
            User.createAcc()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid option.")
            continue

        # Main menu after login
        while True:
            print("\nAfter Login (Main Menu):")
            print("1. Logout")
            print("2. View Account Information")
            print("3. Inventory Information")
            print("4. Cart Information")
            print("5. Go Back")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                User.logout()
                break
            elif choice == "2":
                User.viewAccInfo()
            elif choice == "3":
                # Inventory Information
                while True:
                    print("\nAfter Login (Inventory Information):")
                    print("1. Go Back")
                    print("2. View Inventory")
                    print("3. Search Inventory")
                    choice = input("Enter your choice (1-3): ")

                    if choice == "1":
                        break
                    elif choice == "2":
                        Inventory.viewInventory()
                    elif choice == "3":
                        title = input("Enter the title name you want to search: ")
                        Inventory.searchInventory(title)
                    else:
                        print("Invalid option. Please enter a valid option.")
                        continue

            elif choice == "4":
                # Cart Information
                while True:
                    print("\nAfter Login (Cart Information):")
                    print("1. Go Back")
                    print("2. View Cart")
                    print("3. Add Items to Cart")
                    print("4. Remove an Item from Cart")
                    print("5. Check Out")
                    choice = input("Enter your choice (1-5): ")

                    if choice == "1":
                        break
                    elif choice == "2":
                        Cart.viewCart(User.getUserID())
                    elif choice == "3":
                        ISBN = input("Enter the ISBN to add to cart: ")
                        Cart.addToCart(User.getUserID(), ISBN)
                    elif choice == "4":
                        ISBN = input("Enter the ISBN to remove to cart: ")
                        Cart.removeFromCart(User.getUserID(), ISBN)
                    elif choice == "5":
                        Cart.checkOut(User.getUserID())
                    else:
                        print("Invalid option. Please enter a valid option.")
                        continue

            elif choice == "5":
                break
            else:
                print("Invalid option. Please enter a valid option.")
                continue