def snippet1():
    print("This is snippet 1")

def snippet2():
    print("This is snippet 2")

def snippet3():
    print("This is snippet 3")

def switch_snippet(choice):
    if choice == 1:
        snippet1()
    elif choice == 2:
        snippet2()
    elif choice == 3:
        snippet3()
    else:
        print("Invalid choice")

# User input
choice = int(input("Enter the snippet number to execute (1, 2, or 3): "))
switch_snippet(choice)
