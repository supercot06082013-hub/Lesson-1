class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def get_info(self):
        return f"{self.name} - ${self.price} - In stock: {self.in_stock}"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product.in_stock > 0:
            self.items.append(product)
            product.in_stock -= 1

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
            product.in_stock += 1

    def get_total(self):
        return sum(p.price for p in self.items)

    def get_cart_info(self):
        return [p.get_info() for p in self.items]