# Step 1: Create the Multiplier class
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Step 2: Create an instance of Multiplier
multiply_by_3 = Multiplier(3)

# Step 3: Test with callable()
print("Is multiply_by_3 callable?", callable(multiply_by_3))  # Should print True

# Step 4: Call the object like a function
result = multiply_by_3(10)  # 10 * 3 = 30
print("Result of multiply_by_3(10):", result)
