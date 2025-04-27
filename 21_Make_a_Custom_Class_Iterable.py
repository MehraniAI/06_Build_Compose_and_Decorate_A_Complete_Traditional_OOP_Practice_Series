# Step 1: Create the Countdown class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            number = self.current
            self.current -= 1
            return number

# Step 2: Use the Countdown class in a for-loop
countdown = Countdown(5)

for number in countdown:
    print(number)
