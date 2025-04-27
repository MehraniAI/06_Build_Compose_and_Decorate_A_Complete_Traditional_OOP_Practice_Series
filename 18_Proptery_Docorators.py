class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute with underscore convention

    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, new_price):
        """Setter for price with validation"""
        print("Setting new price...")
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price

# Create a product
product = Product("Laptop", 999.99)

# Use the property getter
print(f"{product.name} price: ${product.price}")  # Uses @property

# Use the property setter
product.price = 899.99  # Uses @price.setter
print(f"New price: ${product.price}")

# Try setting invalid price
try:
    product.price = -100
except ValueError as e:
    print(f"Error: {e}")

# Use the deleter
del product.price  # Uses @price.deleter

# Attempt to access deleted price
try:
    print(product.price)
except AttributeError as e:
    print(f"Error: {e}")