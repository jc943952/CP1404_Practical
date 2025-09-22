"""
writing a program for the user to input a character and decide what the codes
next step is using Q for Quit, G for Goodbye and H for hello
"""
MENU = """
    (H)ello, How are you?
    (Q)uit
    (G)oodbye  
"""
print(MENU)
choice = input("Enter your choice: ")
while choice != 'Q':
    if choice == 'H':
        print("Hello, How are you?")
    elif choice == 'G':
        print("Goodbye")
    else:
        print("Invalid choice, please try again")
    print(MENU)
    choice = input("Enter your choice: ")

print("see you later")