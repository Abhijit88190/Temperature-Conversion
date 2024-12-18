def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Prompt the user for input
print("Temperature Conversion Program")
temp_value = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

# Conversion logic
if unit == "C":
    converted = celsius_to_fahrenheit(temp_value)
    print(f"{temp_value}°C is equal to {converted:.2f}°F")
elif unit == "F":
    converted = fahrenheit_to_celsius(temp_value)
    print(f"{temp_value}°F is equal to {converted:.2f}°C")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
