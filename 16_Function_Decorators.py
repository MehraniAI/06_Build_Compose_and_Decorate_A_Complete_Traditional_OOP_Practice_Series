def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test the decorated function
say_hello("Alice")