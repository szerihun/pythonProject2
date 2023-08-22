#  Ask for the user to enter their name, age, and income.
#  The output from your program should be as follows:
# What is your name? Chris
# What is your age? 25
# What is your income? 50000
# Chris is 25 years old and earns $50000 per year.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter your income: $"))
printIncome = '{:2,.2f}'.format(income)

print(f"{name} is {age} years old and earns ${printIncome} per year.")