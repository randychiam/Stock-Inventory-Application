import shelve


class StockInventory:
    def __init__(self, name, description, price, quantity, brand, country):
        stock_db = shelve.open('stock_db')
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.brand = brand
        self.country = country
        stock_db.close()

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_brand(self, brand):
        self.brand = brand

    def set_country(self, country):
        self.country = country

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_brand(self):
        return self.brand

    def get_country(self):
        return self.country


def add_product():
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    while True:
        try:
            price = float(input("Enter the product price ($): "))
            if price <= 0:
                print("Price cannot be lesser or equal to $0!")
            else:
                break
        except ValueError:
            print("Please enter a valid price! (eg: 10.00)")
    while True:
        try:
            quantity = int(input("Enter the product quantity: "))
            if quantity <= 0:
                print("Quantity cannot be lesser or equal to 0!")
            else:
                break
        except ValueError:
            print("Please enter a valid quantity! (eg: 100)")
    brand = input("Enter the brand of the product: ")
    country = input("Enter the country of origin of the product: ")
    product = StockInventory(name, description, price, quantity, brand, country)
    stock_db = shelve.open('stock_db')
    stock_db[product.get_name()] = [product.get_description(), product.get_price(), product.get_quantity(),
                                    product.get_brand(), product.get_country()]
    stock_db.close()


def remove_product():
    stock_db = shelve.open('stock_db')
    name = input("Enter the product name: ")
    if name in stock_db:
        del stock_db[name]
        print("Product has been successfully removed!")
    else:
        print("Product not found!")
    stock_db.close()


def display_product():
    stock_db = shelve.open('stock_db')
    for product in stock_db:
        products = stock_db[product]
        print("| Name: {} | Description: {} | Price: ${} | Quantity: {} | Brand: {} | Country: {} |".format(product,
                                                                                                            products[
                                                                                                                0],
                                                                                                            products[
                                                                                                                1],
                                                                                                            products[
                                                                                                                2],
                                                                                                            products[
                                                                                                                3],
                                                                                                            products[
                                                                                                                4]))
    stock_db.close()
