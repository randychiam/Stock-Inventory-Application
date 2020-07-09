from StockInventory import *

product_list = []


def bubble_sort():
    while True:
        print("Sorting for stock inventory (Bubble Sort)")
        print("1 - Sort by product name")
        print("2 - Sort by product description")
        print("3 - Sort by product price")
        print("4 - Sort by product quantity")
        print("5 - Sort by product brand")
        print("6 - Sort by product country of origin")
        choice = input("Please select how you want the stock inventory to be sorted (1-6): ")
        stock_db = shelve.open('stock_db')
        # Depending on the user's choice, items[0] is how product_list will be sorted.
        if choice == "1":
            for product in stock_db:
                products = stock_db[product]
                items = [product, products[0], products[1], products[2], products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "2":
            for product in stock_db:
                products = stock_db[product]
                items = [products[0], product, products[1], products[2], products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "3":
            for product in stock_db:
                products = stock_db[product]
                items = [products[1], products[0], product, products[2], products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "4":
            for product in stock_db:
                products = stock_db[product]
                items = [products[2], products[0], products[1], product, products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "5":
            for product in stock_db:
                products = stock_db[product]
                items = [products[3], products[0], products[1], products[2], product, products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "6":
            for product in stock_db:
                products = stock_db[product]
                items = [products[4], products[0], products[1], products[2], products[3], product]
                product_list.append(items)
                n = len(product_list)
        else:
            product_list.clear()
            print("Please select a valid option from 1 to 6!")
            continue
        order = input("Select 'a' for ascending order and 'd' for descending order: ")
        # Bubble Sort algorithm for ascending order
        if order.lower() == "a":
            for i in range(n - 1, 0, -1):
                for j in range(i):
                    if product_list[j] > product_list[j + 1]:
                        tmp = product_list[j]
                        product_list[j] = product_list[j + 1]
                        product_list[j + 1] = tmp
        # Bubble Sort algorithm for descending order
        elif order.lower() == "d":
            for i in range(n - 1, 0, -1):
                for j in range(i):
                    if product_list[j] < product_list[j + 1]:
                        tmp = product_list[j]
                        product_list[j] = product_list[j + 1]
                        product_list[j + 1] = tmp
        else:
            product_list.clear()
            print("Please select a valid order ('a' or 'd')!")
            continue
        # After product_list has been sorted in the chosen order, it will be displayed in the format below.
        if choice == "1":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[0], product[1],
                    product[2], product[3], product[4], product[5]))
            break
        elif choice == "2":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[1], product[0],
                    product[2], product[3], product[4], product[5]))
            break
        elif choice == "3":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[2], product[1],
                    product[0], product[3], product[4], product[5]))
            break
        elif choice == "4":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[3], product[1],
                    product[2], product[0], product[4], product[5]))
            break
        elif choice == "5":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[4], product[1],
                    product[2], product[3], product[0], product[5]))
            break
        elif choice == "6":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[5], product[1],
                    product[2], product[3], product[4], product[0]))
            break
        stock_db.close()


def insertion_sort():
    while True:
        print("Sorting for stock inventory (Insertion Sort)")
        print("1 - Sort by product name")
        print("2 - Sort by product description")
        print("3 - Sort by product price")
        print("4 - Sort by product quantity")
        print("5 - Sort by product brand")
        print("6 - Sort by product country of origin")
        choice = input("Please select how you want the stock inventory to be sorted (1-6): ")
        stock_db = shelve.open('stock_db')
        # Depending on the user's choice, items[0] is how product_list will be sorted.
        if choice == "1":
            for product in stock_db:
                products = stock_db[product]
                items = [product, products[0], products[1], products[2], products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "2":
            for product in stock_db:
                products = stock_db[product]
                items = [products[0], product, products[1], products[2], products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "3":
            for product in stock_db:
                products = stock_db[product]
                items = [products[1], products[0], product, products[2], products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "4":
            for product in stock_db:
                products = stock_db[product]
                items = [products[2], products[0], products[1], product, products[3], products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "5":
            for product in stock_db:
                products = stock_db[product]
                items = [products[3], products[0], products[1], products[2], product, products[4]]
                product_list.append(items)
                n = len(product_list)
        elif choice == "6":
            for product in stock_db:
                products = stock_db[product]
                items = [products[4], products[0], products[1], products[2], products[3], product]
                product_list.append(items)
                n = len(product_list)
        else:
            product_list.clear()
            print("Please select a valid option from 1 to 6!")
            continue
        order = input("Select 'a' for ascending order and 'd' for descending order: ")
        # Insertion Sort algorithm for ascending order
        if order.lower() == "a":
            for i in range(1, n):
                value = product_list[i]
                pos = i
                while pos > 0 and value < product_list[pos - 1]:
                    product_list[pos] = product_list[pos - 1]
                    pos -= 1
                    product_list[pos] = value
        # Insertion Sort algorithm for descending order
        elif order.lower() == "d":
            for i in range(1, n):
                value = product_list[i]
                pos = i
                while pos > 0 and value > product_list[pos - 1]:
                    product_list[pos] = product_list[pos - 1]
                    pos -= 1
                    product_list[pos] = value
        else:
            product_list.clear()
            print("Please select a valid order ('a' or 'd')!")
            continue
        # After product_list has been sorted in the chosen order, it will be displayed in the format below.
        if choice == "1":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[0], product[1],
                    product[2], product[3], product[4], product[5]))
            break
        elif choice == "2":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[1], product[0],
                    product[2], product[3], product[4], product[5]))
            break
        elif choice == "3":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[2], product[1],
                    product[0], product[3], product[4], product[5]))
            break
        elif choice == "4":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[3], product[1],
                    product[2], product[0], product[4], product[5]))
            break
        elif choice == "5":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[4], product[1],
                    product[2], product[3], product[0], product[5]))
            break
        elif choice == "6":
            for product in product_list:
                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(
                    product[5], product[1],
                    product[2], product[3], product[4], product[0]))
            break
        stock_db.close()


def sort_algorithms():
    while True:
        print("Select the sorting algorithm you wish to use")
        print("a - Bubble Sort")
        print("b - Insertion Sort")
        choice = input("Please select a sorting algorithm to use ('a' or 'b'): ")
        if choice.lower() == "a":
            bubble_sort()
            break
        elif choice.lower() == "b":
            insertion_sort()
            break
        else:
            print("Please select a valid option ('a' or 'b')!")
            continue


sort_algorithms()
