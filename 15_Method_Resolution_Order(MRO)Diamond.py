class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):
    pass  # Inherits from both B and C

# Create instance of D
d = D()

# Call show() - demonstrates MRO
d.show()  # Output depends on MRO

# Print the Method Resolution Order
print("Method Resolution Order (MRO) for class D:", D.__mro__)