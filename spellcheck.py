# Spell checker
print("Welcome to your spellcheck demonstration")
print("A structure which humans occupy?")
def spell_checker():
    import time
    guess = input()
    if guess == "Building":
        print("Well done, that is the word I was looking for!")
        time.sleep(3)
        from menu import Main_menu
        Main_menu()
    elif guess == "building":
        print("Well done, that is the word I was looking for!")
        time.sleep(3)
        from menu import Main_menu
        Main_menu()
    elif guess == 'q':
        from menu import Main_menu
        Main_menu()
    else:
        print("Not quite what I was thinking, try again or enter q to quit to Main Menu.")
    spell_checker()
spell_checker()