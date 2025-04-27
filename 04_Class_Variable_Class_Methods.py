class Bank:
    bank_name = "Default Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name  # Update the class variable

# Create instances before changing the bank name
bank1 = Bank()
bank2 = Bank()

print("Before changing bank name:")
print("Bank 1:", bank1.bank_name)
print("Bank 2:", bank2.bank_name)

# Change the bank name using the class method
Bank.change_bank_name("New Awesome Bank")

print("\nAfter changing bank name:")
print("Bank 1:", bank1.bank_name)
print("Bank 2:", bank2.bank_name)
