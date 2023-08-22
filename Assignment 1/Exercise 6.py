# Write a program that Wille execute some arithmetic expressions.
# Have the user enter 3 numbers and call them num1, num2, and num3.
# Using these three values, output the result with the following
# expressions:
#
# addition
# subtraction
# multiplication
# average of the three values

num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter first number: "))

addition = num1 + num2 + num3
subtraction = num1 + num2 + num3
multiplication = num1 * num2 * num3
average = (num1 + num2 + num3)/3

print(f"The sum of the three numbers is {addition}.")
print(f"The difference of the three numbers is {subtraction}.")
print(f"The product of the three numbers is {multiplication}.")
print(f"The average of the three numbers is {average}.")