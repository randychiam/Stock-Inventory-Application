from StockInventory import *

from datetime import datetime as dt

import math

import statistics as stats

price_list = []
quantity_list = []

# Format the date and time.
now = dt.now()
datetime = now.strftime("%d/%m/%Y, %H:%M:%S")


def report():
    stock_db = shelve.open('stock_db')
    for product in stock_db:
        products = stock_db[product]
        quantity_list.append(products[2])
        price_list.append(products[1] * products[2])
        total_price = sum(price_list)
        average_price = stats.mean(price_list)
        median_price = stats.median(price_list)
        mode_price = stats.mode(price_list)
        total_quantity = sum(quantity_list)
        average_quantity = stats.mean(quantity_list)
        median_quantity = stats.median(quantity_list)
        mode_quantity = stats.mode(quantity_list)
    print("Statistical report for stock inventory")
    print("Total Inventory Price: ${:.2f}".format(total_price))
    print("Average Inventory Price: ${:.2f}".format(average_price))
    print("Median Inventory Price: ${:.2f}".format(median_price))
    print("Mode Inventory Price: ${:.2f}".format(mode_price))
    print("Total Stock Quantity: {}".format(total_quantity))
    print("Average Stock Quantity: {}".format(math.floor(average_quantity)))
    print("Median Stock Quantity: {}".format(median_quantity))
    print("Mode Stock Quantity: {}".format(mode_quantity))
    print("Price per quantity: ${:.2f}".format(total_price / total_quantity))
    print("Report generated on: {}".format(datetime))
    stock_db.close()
    return "Statistical report for stock inventory" + "\nTotal Inventory Price: ${:.2f}".format(
        total_price) + "\nAverage Inventory Price: ${:.2f}".format(
        average_price) + "\nMedian Inventory Price: ${:.2f}".format(
        median_price) + "\nMode Inventory Price: ${:.2f}".format(mode_price) + "\nTotal Stock Quantity: {}".format(
        total_quantity) + "\nAverage Stock Quantity: {}".format(
        math.floor(average_quantity)) + "\nMedian Stock Quantity: {}".format(
        median_quantity) + "\nMode Stock Quantity: {}".format(mode_quantity) + "\nPrice per quantity: ${:.2f}".format(
        total_price / total_quantity) + "\nReport generated on: {}".format(datetime)


# Save output into a .txt file.
output = report()
while True:
    print("Would you like to save the report into a .txt file?")
    print("y - Yes")
    print("n - No")
    choice = input("Yes or No? ")
    if choice.lower() == "y":
        filename = input("Please enter a file name to save the report (do not need to enter .txt): ")
        file = open(filename + ".txt", "w")
        file.write(output)
        file.close()
        break
    elif choice.lower() == "n":
        print("Thank You!")
        break
    else:
        continue
