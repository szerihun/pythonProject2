# Write a program that will calculate the amount of land the
# user owns. One acre of land is approximately 43,560 square feet.
# Have the user enter how much land they own and display the number
# of acres owned. (HINT: divide the user input by the 43560 to get
# the acres of land.)

ownedLand = int(input("How much land do you own (report in square feet): "))
actualOwned = str((ownedLand / 43560))

print(f"You own {actualOwned} acre.")