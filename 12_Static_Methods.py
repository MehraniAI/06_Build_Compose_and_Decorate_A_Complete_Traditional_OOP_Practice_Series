class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """Convert Celsius to Fahrenheit"""
        return (c * 9/5) + 32

# Using the static method without creating an instance
print("32°C is", TemperatureConverter.celsius_to_fahrenheit(32), "°F")  # 32°C is 89.6 °F
print("0°C is", TemperatureConverter.celsius_to_fahrenheit(0), "°F")    # 0°C is 32.0 °F
print("-40°C is", TemperatureConverter.celsius_to_fahrenheit(-40), "°F") # -40°C is -40.0 °F