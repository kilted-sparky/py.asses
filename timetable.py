# Timetable

def main_option():
    print("Welcome to your timetable menu.")
    print("1. View Timetable")
    print("2. Amend classes (Admin ONLY)")
    print("3. Return to Main menu.")
    strChoice = int(input("What option would you like to choose?"))
    if strChoice == 1:
        print("What day would you like to show")
        if input() == "Monday":
            with open('Monday_Timetable.txt') as f:
                line = f.read()
            print(line)
            main_option()
        elif input() == "Tuesday":
            with open('Tuesday_Timetable.txt') as x:
                line1 = x.read()
            print(line1)
            main_option()
        elif input() == "Wednesday":
            with open('Wednesday_Timetable.txt') as g:
                line2 = g.read()
            print(line2)
            main_option()
        elif input() == "Thursday":
            with open('Thursday_Timetable.txt') as d:
                line3 = d.read()
            print(line3)
            main_option()
        elif input() == "Friday":
            with open('Friday_Timetable.txt') as r:
                line4 = r.read()
            print(line4)
            main_option()
        else:
            main_option()
    elif strChoice == 2:
        print("What day would you like to amend?")
        x = input("")
        print("Please enter your amendment: ")
        change = input("")
        if x == 'Monday':
            with open('Monday_Timetable.txt', 'a') as f:
                f.write('\n' + "***" + change + "***")
                f.close()
                main_option()
        elif x == 'Tuesday':
            with open('Tuesday_Timetable.txt', 'a') as f:
                f.write('\n' + "***" + change + "***")
                f.close()
                main_option()
        elif x == 'Wednesday':
            with open('Wednesday_Timetable.txt', 'a') as f:
                f.write('\n' + "***" + change + "***")
                f.close()
                main_option()
        elif x == 'Thursday':
            with open('Thursday_Timetable.txt', 'a') as f:
                f.write('\n' + "***" + change + "***")
                f.close()
                main_option()
        elif x == 'Friday':
            with open('Friday_Timetable.txt', 'a') as f:
                f.write('\n' + "***" + change + "***")
                f.close()
                main_option()
        else:
            main_option()
    elif strChoice == 3:
        from menu import Main_menu
        Main_menu()
    else:
        main_option()
main_option()
