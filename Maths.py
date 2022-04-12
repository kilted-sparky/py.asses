# Calculator

def calculator():

    print("Welcome to your very own calculator!")
    print("The functions available are: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Return to Main Menu")

    def add(x, y):
        total = x + y
        print("Total = ", total)

    def minus(x, y):
        total = x - y
        print("Total = ", total)

    def division(x, y):
        total = x/y
        print("Total = ", total)

    def multiply(x, y):
        total = x*y
        print("Total = ", total)

    print("")
    while True:
        func = int(input("Which function would you like to use?"))
        if func == 5:
            from menu import Main_menu
            Main_menu()
        first = (float(input("Please enter your first number: ")))
        second = (float(input("Please enter your second number: ")))
        if func == 1:
            print(add(first, second))
        elif func == 2:
            print(minus(first, second))
        elif func == 3:
            print(multiply(first, second))
        elif func == 4:
            print(division(first, second))
    else:
        print("Invalid entry")
calculator()

