# Step 1: Create a custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

# Step 2: Define a function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Step 3: Use try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print("Age is valid. You can proceed.")
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
