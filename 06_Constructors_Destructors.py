class Logger:
    def __init__(self):
        print("Logger object created.")  # Constructor message

    def __del__(self):
        print("Logger object destroyed.")  # Destructor message

# Create an instance of Logger
logger = Logger()

# Delete the object to trigger the destructor
del logger