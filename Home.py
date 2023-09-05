def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def feet_to_centimeters(feet):
    return feet * 30.48

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
feet = float(input("Enter length in feet: "))

print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C")
print(f"{feet}ft is equal to {feet_to_centimeters(feet)}cm")