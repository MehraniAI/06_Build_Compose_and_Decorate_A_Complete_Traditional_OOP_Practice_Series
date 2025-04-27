class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def get_info(self):
        return f"Employee {self.emp_id}: {self.name}"

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation - stores Employee references
    
    def add_employee(self, employee):
        """Add an existing Employee to this department"""
        self.employees.append(employee)
    
    def list_employees(self):
        """List all employees in this department"""
        print(f"Employees in {self.dept_name}:")
        for emp in self.employees:
            print(f"- {emp.get_info()}")

# Create independent Employee objects
emp1 = Employee("John Doe", "E1001")
emp2 = Employee("Jane Smith", "E1002")

# Create Department
engineering = Department("Engineering")

# Add employees to department (aggregation)
engineering.add_employee(emp1)
engineering.add_employee(emp2)

# List department employees
engineering.list_employees()

# Employees continue to exist independently
print("\nIndependent employee access:")
print(emp1.get_info())
print(emp2.get_info())