# Diary

import datetime

def diary():
    print("Whats been happening today?")
    entry = str(input(""))
    f = open('diary.txt', 'a') # a = append
    r = open('diary.txt', 'r') # r = read
    date = str(datetime.datetime.now())
    f.write(date + '\n')
    f.write('----' + '\n')
    f.write(entry + '\n')
    x = str(input("You can enter more by typing yes, open your Notes by typing open or return to Main Menu by typing no (yes/no/open)"))
    while True:
        if x == 'yes':
            diary()
        elif x == 'no':
            print("See you soon!")
            from menu import Main_menu
            Main_menu()
        elif x == 'open':
            with open('diary.txt') as a:
                lines = a.read()
                print(lines)
                diary()
        else:
            print("Not quite sure what happened there.")
            x = str(input("Anything else to enter? (yes/no)"))
diary()