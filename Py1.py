# Day 1: Variables and Input/Output

# Program 1: Simple greeting
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are {age} years old!")

# Program 2: Temperature converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

# Program 3: Simple math
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")