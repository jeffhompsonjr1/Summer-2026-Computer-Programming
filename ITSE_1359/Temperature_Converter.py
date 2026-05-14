#Create a script that converts a temperature from Celsius to Fahrenheit.

"""Display a welcome message for your temperature converter
Ask the user to enter a temperature in Celsius
Convert the input to a float
Convert the temperature to Fahrenheit using the formula: F = (C × 9/5) + 32
Display the result with 2 decimal places using f-string formatting
Include the degree symbol (°) in your output"""

print("Try my home made thermometer, without the mercury of course :)")

C=float(input("Enter the temperature in Celcius: "))
F=((C * 9/5)+32)
print(f"{C:.2f}°C is equal to {F:.2f}°F")
