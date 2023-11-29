import sqlite3
from inventory import Inventory
from userClass import User
from cart import Cart


#main
if __name__ == "__main__":
    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            User.login()
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
                        print("view inventory")
                        # view_inventory()
                    elif choice == "3":
                        print("search inventory")
                        # search_inventory()
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
                        Cart.view_cart()
                    elif choice == "3":
                        Cart.add_to_cart()
                    elif choice == "4":
                        Cart.remove_from_cart()
                    elif choice == "5":
                        Cart.check_out()
                    else:
                        print("Invalid option. Please enter a valid option.")
                        continue

            elif choice == "5":
                break
            else:
                print("Invalid option. Please enter a valid option.")
                continue