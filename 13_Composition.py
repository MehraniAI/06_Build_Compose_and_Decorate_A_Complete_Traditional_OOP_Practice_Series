class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type
    
    def start(self):
        return f"{self.engine_type} engine started"
    
    def stop(self):
        return f"{self.engine_type} engine stopped"

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Composition - Car has an Engine
    
    def start_car(self):
        return f"{self.model}: {self.engine.start()}"
    
    def stop_car(self):
        return f"{self.model}: {self.engine.stop()}"

# Create an Engine
v8_engine = Engine("V8")

# Create a Car with the Engine
mustang = Car("Ford Mustang", v8_engine)

# Use the Car's methods which access the Engine's methods
print(mustang.start_car())  # Output: Ford Mustang: V8 engine started
print(mustang.stop_car())   # Output: Ford Mustang: V8 engine stopped