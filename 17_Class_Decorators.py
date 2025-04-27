def add_greeting(cls):
    """Class decorator that adds a greet method"""
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Add the new method to the class
    return cls  # Return the modified class

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of the decorated class
person = Person("Alice")

# Call the original method
print(f"Name: {person.name}")  # Output: Name: Alice

# Call the added method
print(person.greet())  # Output: Hello from Decorator!