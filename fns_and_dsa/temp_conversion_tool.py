# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global conversion factor.
    Formula: (F - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global conversion factor.
    Formula: (C * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature
        temperature = float(input("Enter the temperature value: "))
        
        # Prompt user to specify the unit
        unit = input("Is the temperature in (C)elsius or (F)ahrenheit? ").strip().lower()

        # Perform the appropriate conversion
        if unit == 'c':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equivalent to {converted_temp:.2f}°F")
        elif unit == 'f':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equivalent to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

