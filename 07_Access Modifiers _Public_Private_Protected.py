class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary      # Protected variable
        self.__ssn = ssn          # Private variable

# Create an instance of Employee
emp = Employee("John Doe", 50000, "123-45-6789")

# Access public variable
print("Public variable (name):", emp.name)  # Accessible

# Access protected variable (conventionally should not be accessed directly)
print("Protected variable (_salary):", emp._salary)  # Accessible but discouraged

# Attempt to access private variable (will raise an AttributeError)
try:
    print("Private variable (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable:", e)

# Access private variable using name mangling (not recommended)
print("Private variable accessed via name mangling:", emp._Employee__ssn)