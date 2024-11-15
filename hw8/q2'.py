class Product:
    def __init__(self, name, price, stock):
        self.id = generate_unique_id()
        self.name = name
        self.price = price
        self.stock = stock

    def check_stock(self, quantity):
        return self.stock >= quantity

    def update_stock(self, quantity):
        self.stock -= quantity

class Cart:
    def __init__(self):
        self.items = {}
        self.discount = 0

    def add_product(self, product, quantity):
        if product.check_stock(quantity):
            if product.id in self.items:
                self.items[product.id]['quantity'] += quantity
            else:
                self.items[product.id] = {'product': product, 'quantity': quantity}
            product.update_stock(quantity)
        else:
            raise ValueError("Not enough stock available.")

    def remove_product(self, product, quantity):
        if product.id in self.items:
            if self.items[product.id]['quantity'] >= quantity:
                self.items[product.id]['quantity'] -= quantity
                product.update_stock(-quantity)
                if self.items[product.id]['quantity'] == 0:
                    del self.items[product.id]
            else:
                raise ValueError("Not enough quantity to remove.")
        else:
            raise ValueError("Product not found in cart.")

    def set_discount(self, discount):
        self.discount = discount

    def calculate_total(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        return total * (1 - self.discount / 100)

    def total_items(self):
        return sum(item['quantity'] for item in self.items.values())

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.cart = Cart()

    def view_cart(self):
        return self.cart.items

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.cart.remove_product(product, quantity)

    def checkout(self):
        return self.cart.calculate_total()

class Store:
    products = []
    carts = []
    total_quantity_in_carts = 0

    def __init__(self):
        pass

    def add_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)
        return product

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def create_cart(self):
        cart = Cart()
        self.carts.append(cart)
        return cart

    @staticmethod
    def total_items_in_all_carts():
        total = sum(cart.total_items() for cart in Store.carts)
        return total