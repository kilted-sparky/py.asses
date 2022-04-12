# Hangman

def Hangman():
    import time
    import random
    with open('Hangman_wordlist.txt', 'r') as x:
        word = x.readlines()
    answer = random.choice(word)[:-1]
    allowed_attempts = 8
    attempts = []
    finished = False
    while not finished:
        for letter in answer:
            if letter.lower() in attempts:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")

        guess = input(f"Number of attempts left {allowed_attempts}, next guess: ")
        attempts.append(guess.lower())
        if guess.lower() not in answer.lower():
            allowed_attempts -= 1
            if allowed_attempts == 0:
                break

        finished = True
        for letter in answer:
            if letter.lower() not in attempts:
                finished = False
    if finished:
        print(f"Well done you guessed the word correctly, it was {answer}")
        time.sleep(2)
        from menu import Main_menu
        Main_menu()
    else:
        print(f"Unfortunately this time you lost, the word was {answer} please try again next time.")
        time.sleep(2)
        from menu import Main_menu
        Main_menu()
Hangman()