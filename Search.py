from StockInventory import *

product_list = []


def binary_search():
    while True:
        print("Search for items in stock inventory (Binary Search)")
        print("1 - Search by product name")
        print("2 - Search by product description")
        print("3 - Search by product price")
        print("4 - Search by product quantity")
        print("5 - Search by product brand")
        print("6 - Search by product country of origin")
        choice = input("Please select how you want to search the stock inventory (1-6): ")
        stock_db = shelve.open('stock_db')
        if choice == "1":
            search = input("Enter your search query (Name): ")
            for product in stock_db:
                items = product
                product_list.append(items)
                n = len(product_list)
        elif choice == "2":
            search = input("Enter your search query (Description): ")
            for product in stock_db:
                products = stock_db[product]
                items = products[0]
                product_list.append(items)
                n = len(product_list)
        elif choice == "3":
            search = float(input("Enter your search query (Price): "))
            for product in stock_db:
                products = stock_db[product]
                items = products[1]
                product_list.append(items)
                n = len(product_list)
        elif choice == "4":
            search = int(input("Enter your search query (Quantity): "))
            for product in stock_db:
                products = stock_db[product]
                items = products[2]
                product_list.append(items)
                n = len(product_list)
        elif choice == "5":
            search = input("Enter your search query (Brand): ")
            for product in stock_db:
                products = stock_db[product]
                items = products[3]
                product_list.append(items)
                n = len(product_list)
        elif choice == "6":
            search = input("Enter your search query (Country): ")
            for product in stock_db:
                products = stock_db[product]
                items = products[4]
                product_list.append(items)
                n = len(product_list)
        else:
            product_list.clear()
            print("Please select a valid option from 1 to 6!")
            continue
        # product_list must be sorted for binary search to work.
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if product_list[j] > product_list[j + 1]:
                    tmp = product_list[j]
                    product_list[j] = product_list[j + 1]
                    product_list[j + 1] = tmp
        low = 0
        high = len(product_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if product_list[mid] == search:
                first_occurrence = mid
                last_occurrence = mid
                cont = True
                while first_occurrence > 0 and cont:
                    if product_list[first_occurrence - 1] == search:
                        first_occurrence -= 1
                    else:
                        cont = False
                cont = True
                while last_occurrence > 0 and cont:
                    if product_list[last_occurrence - 1] == search:
                        last_occurrence += 1
                    else:
                        cont = False
            # For loop for i in range of first occurrence of search results until the last occurrence of search results.
                if choice == "1":
                    for i in range(first_occurrence, last_occurrence + 1):
                        for product in stock_db:
                            products = stock_db[product]
                            # Print the search results in the format below.
                            if product_list[i] in product:
                                print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | "
                                      "Country: {} | ".format(product, products[0], products[1], products[2],
                                                              products[3], products[4]))
                        break
                    break
                else:
                    for i in range(first_occurrence, last_occurrence + 1):
                        for product in stock_db:
                            products = stock_db[product]
                            # Print the search results in the format below.
                            if product_list[i] in products:
                                print(
                                    "| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: "
                                    "{} | "
                                        .format(product, products[0], products[1], products[2], products[3],
                                                products[4]))
                        break
                    break
            elif search < product_list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        stock_db.close()


binary_search()
