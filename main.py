#main
def main():
    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            login()
        elif choice == "2":
            createAcc()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid option.")

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
                logout()
                break
            elif choice == "2":
                viewAccInfo()
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
                        view_inventory()
                    elif choice == "3":
                        search_inventory()
                    else:
                        print("Invalid option. Please enter a valid option.")

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
                        view_cart()
                    elif choice == "3":
                        add_to_cart()
                    elif choice == "4":
                        remove_from_cart()
                    elif choice == "5":
                        check_out()
                    else:
                        print("Invalid option. Please enter a valid option.")

            elif choice == "5":
                break
            else:
                print("Invalid option. Please enter a valid option.")
