class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):         # Instance method
        print(f"{self.name} the {self.breed} says Woof!")

# Create instances of Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Call the bark method on each instance
dog1.bark()  # Output: Buddy the Golden Retriever says Woof!
dog2.bark()  # Output: Max the Beagle says Woof!