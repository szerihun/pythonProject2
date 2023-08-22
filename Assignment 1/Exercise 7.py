# Write a program that asks the user for their weight in pounds
# and convert the value into kilograms. The conversion is
# 2.2 pounds = 1 kilogram. Display the output.

weight = float(input("Please enter your weight in pounds: "))

kilogram = str((weight/2.2))

print(f"Your weight in kilograms is {kilogram}.")