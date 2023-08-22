while True:
    s = input("Enter any characters from the alphabet: ")
    if s == "quit" or s == "Quit" or s == "QUIT":
        break
    print("The length of the string is ", len(s))

print("The loop has exited.")