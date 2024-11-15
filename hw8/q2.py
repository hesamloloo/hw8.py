class Product:
    def __init__(self, name, price, stock):
    
    def check_stock(quantity):
            pass
    def update_stock(quantity):
            pass

class Cart:
    def __init__(self):
        pass
    def add_product(product, quantity):
        pass
    def remove_product(product, quantity):
        pass
    def set_discount(discount):
        pass
    def calculate_total():
        pass
    def total_items():
        pass

class Customer:
    def __init__(self, name, customer_id):
        pass
    def view_cart():
        pass
    def add_to_cart(product, quantity):
        pass
    def remove_from_cart(product, quantity):
        pass
    def checkout():
        pass

class Store:
    products = []
    carts = []
    total_quantity_in_carts = 0 

    def __init__(self):
        pass
    def add_product(name, price, stock):
        pass

    def get_product_by_id(product_id):
        pass

    def create_cart():
        pass

    @staticmethod
    def total_items_in_all_carts():
        pass
