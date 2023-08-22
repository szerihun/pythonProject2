while True:
    s = input("Enter a alphabetic value: ")
    print("You have entered ", s)
    if len(s) == 2:
        print("The value is too small.")
        continue
    if s == "quit" or s == "Quit" or s == "QUIT":
        break
    print("The entered value is sufficient!")

print("We have exited the loop.")