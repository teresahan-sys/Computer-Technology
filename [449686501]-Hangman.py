# This program plays Hangman with the user by choosing a random word and giving the user 7 chances to guess it

import random
import sys
import os
import platform
import time

try:
        with open('words_for_hangman.txt', 'r', encoding='utf-8') as file:
                find_words = file.read().lower().splitlines() # Open and read the words in the Hangman wordlist
except FileNotFoundError: # Runs if text file not found to prevent program crashing
        find_words = ['apple', 'blizzard', 'turmoil', 'suggestion', 'transport']

def clear_screen(): # Function that clears the screen
        if platform.system() == "Windows":
                os.system('cls')
        else:
                os.system('clear')

def you_lost(): # Function that tells the user they lost and exits the program.
        print("YOU LOST! ")
        print(f"The word was: {word}")
        print("""
                                |    >    <   |
                                 \\           /
                                  \\    ﹏   /
                                     ------""")
        print("It was nice playing. Goodbye!")
        sys.exit()

def zero(): # Prints the gallows Hangman graphic
        print("""
 ___________________
|                   |
|                   |
|
|
|
|
|
|
""")

def one(): # Prints the head
        print("""
 ___________________
|                   |
|                   |
|                   O
|
|
|
|
|
""")

def two(): # Prints head and body
        print("""
 ___________________
|                   |
|                   |
|                   O
|                   |
|
|
|
|
""")

def three(): # Prints head, body and arms
        print("""
 ___________________
|                   |
|                   |
|                   O
|                   |\\
|
|
|
|
""")

def four(): # Prints both arms, head and body
        print("""
 ___________________
|                   |
|                   |
|                   O
|                  /|\\
|
|
|
|
""")

def five(): # Prints arms, head, body and a leg
        print("""
 ___________________
|                   |
|                   |
|                   O
|                  /|\\
|                    \\
|
|
|
""")

def six(): # Prints head, body, arms, legs
        print("""
 ___________________
|                   |
|                   |
|                   O
|                  /|\\
|                  / \\
|
|
|
""")

# Dictionary holding all the Hangman drawings for each stage so they can be called upon
graphics_dictionary = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: you_lost,
}

while True:
    word = random.choice(find_words) # Choose a random word from the Hangman wordlist
    number_of_underscores = len(word) # Count the letters in chosen word
    UNDERSCORES = list("_" * number_of_underscores) # Turns word into corresponding list of underscores that can be replaced with letters throughout the game
    count = 0
    empty_list = []
    start_the_clock = time.time() # Notes the current time in seconds since January 1, 1970
    while True:
        clear_screen()
        graphics_dictionary.get(count)() # Executes the function in the dictionary that corresponds to the number of errors the user has made
        print(f"Secret word = {''.join(UNDERSCORES)}\n")
        print(f"Wrong letters: {empty_list}") # Prints list with user's incorrect letters
        if 7 - count != 1: # If number of lives remaining is more than one
                print(f"You have {7 - count} lives remaining.")
        else: print("You have 1 life remaining.")
        user_input = input("Enter your guess: ").lower() # Prompts user to guess a letter or word, turns it into lowercase
        if user_input in empty_list: # If the guess is in the list of incorrect letters user guessed
                print("Already guessed!")
                input("Press enter to continue ")
                continue
        if not user_input.isalpha(): # User input is not a letter
                print("Invalid character entered! ")
                input("Press enter to continue ")
                continue
        convert_to_list = list(user_input) # Convert user input to a list to replace underscore with a letter if user's guess is correct
        if user_input in word: # If the inputted letter or word is in the secret word
                for string in convert_to_list: # Loop cycling through letters in user's guess
                        if string in word: # If the letter is in the secret word
                                for index in range(number_of_underscores): # Loop cycling through position of each underscore
                                        position = word[index] # Identify position of the letter in the original secret word
                                        if position == string:
                                                UNDERSCORES[index] = string # Replace the underscore at the specific position with user's guess
        else:
                if user_input not in empty_list: # User guessed a new but incorrect letter
                        empty_list.append(user_input) # Adds incorrect letter to list
                        count = count + 1 # Increases life count by 1
        if "".join(UNDERSCORES) == word: # If converting underscores to a string results in the secret word
                print(f"Secret word = {''.join(UNDERSCORES)}\n")
                print("You won!")
                print("")
                print(f"You made {count} mistakes!")
                stop_the_clock = time.time()
                how_long_user_took = round(stop_the_clock - start_the_clock, 1) # Subtract start time from finish time and round to 1 decimal place
                print(f"You took {how_long_user_took} seconds to beat this Hangman!")
                while True:
                        replay_or_not = input("Do you want to replay? YES/NO ").upper()
                        if replay_or_not == "NO":
                                sys.exit() # Exits the program
                        elif replay_or_not == "YES":
                                break
                        else:
                                print("Invalid input! ")
                break # Break out of this loop and return to main gameplay loop
        else: pass