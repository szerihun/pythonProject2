print("***Using a continue statement inside a while loop.***")

value = 1
print(f"The current value is {value}.")
print("The loop skipped the value when it is equal to 3.")

while value < 5:
    value += 1
    print(f"The value is {value}.")
    if value == 3:
        continue
    print("The loop is still going.")

print("We are out of the loop.")