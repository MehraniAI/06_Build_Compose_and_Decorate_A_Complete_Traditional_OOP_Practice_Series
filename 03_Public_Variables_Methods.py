class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print(f"The {self.brand} car has started.")  # Public method

# Instantiate the class
my_car = Car("Toyota")

# Access the public variable
print("Brand:", my_car.brand)

# Call the public method
my_car.start()