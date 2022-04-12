# Help function


def help_func():
    import time
    print("===Welcome to the Help menu===")
    print(" What would you like help with:")
    choice = int(input("""
    1. Calculator
    2. Spell Checker
    3. Timetable
    4. Game - Hangman
    5. Game - Higher Lower
    6. Diary/Notes
    7. House point checker
    8. Return to Main Menu
    
    Please choose:  """))

    if choice == 1:
        with open("calc_help.txt") as f:
            line = f.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 2:
        with open("spell_help.txt") as x:
            line = x.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 3:
        with open("time_help.txt") as b:
            line = b.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 4:
        with open("hangman_help.txt") as c:
            line = c.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 5:
        with open("higher_help.txt") as d:
            line = d.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 6:
        with open("diary_help.txt") as e:
            line = e.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 7:
        with open("house_help") as g:
            line = g.read()
            print(line)
            time.sleep(5)
            help_func()
    elif choice == 8:
            from menu import Main_menu
            Main_menu()
    else:
        print("Please enter a number between 1 and 8")
help_func()

