class Person:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject  # Initialize the subject attribute

# Create an instance of Teacher
teacher = Teacher("Mr. Smith", "Mathematics")

# Print the attributes
print("Name:", teacher.name)
print("Subject:", teacher.subject)