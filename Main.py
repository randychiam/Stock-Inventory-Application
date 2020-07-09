from StockInventory import *


def menu():
    while True:
        print("Welcome to the Stock Inventory Application")
        print("1 - Add a new product")
        print("2 - Remove an existing product")
        print("3 - Display all existing products")
        choice = input("Please select an option (1-3): ")
        if choice == "1":
            add_product()
            break
        elif choice == "2":
            remove_product()
            break
        elif choice == "3":
            display_product()
            break
        else:
            print("Please select a valid option from 1 to 3!")
            continue


menu()
