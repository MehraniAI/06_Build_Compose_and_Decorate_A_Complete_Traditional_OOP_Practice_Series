class Counter:
    count = 0  # Class variable to keep track of the number of objects

    def __init__(self):
        Counter.count += 1  # Increment the count each time an object is created

    @classmethod
    def get_count(cls):
        return cls.count  # Return the current count using cls

# Example usage:
# obj1 = Counter()
# obj2 = Counter()
# print(Counter.get_count())  # Output: 2