import random

first_dictionary = {}
while True: 
    while True:
        user_input = input("Enter your new word or type QUIZ to enter quiz mode: ")
        if user_input == "QUIZ":
            if len(first_dictionary) == 0:
                print("No words to quiz yet!")
                continue
            else:
                break
        else:
            user_input2 = input("Enter the word's meaning: ")
            first_dictionary[user_input] = user_input2

    print("\033[1;31mYou have entered quiz mode.")

    while True: 
        choose_word = random.choice(list(first_dictionary))
        user_input3 = input(f"\033[36mEnter the meaning of the word '{choose_word}': ")
        get_meaning = first_dictionary.get(choose_word)
        if user_input3.lower() == get_meaning.lower():
            print("Congratulations, you got that right!")
            user4 = input("Type QUIZ to continue or NEW WORD to go back: ")
            if user4 == "QUIZ":
                print("\033[H\033[J", end="")
                continue
            elif user4 == "NEW WORD":
                break
            else:
                print("That is an invalid option!")
                print("\033[H\033[J", end="")
        else:
            print("Incorrect!")
