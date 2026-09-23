# Menu allowing the user to select specific options and run the code.

import os
import platform
import sys

# Function that clears the terminal
def clear_terminal():     
    # Check the operating system
    if platform.system() == "Windows":
        # Command for Windows
        os.system('cls')
    else:
        # Command for macOS and Linux
        os.system('clear')

def menu_print(): # Function prints the menu options
    print("""
 ------------------------------------------------
|                                                |
|    9CT Task 4                                  |
|    Name : Teresa Han                           |
|    Version : 01.1                              |
|                                                |
 ------------------------------------------------
\x1b[31m
1. Hello World
2. Goodbye World
3. Goodbye Person
4. Good Teacher
\x1b[0m5. forLoop
5.5. forLoop2
6. whileLoop
7. string Loop
8. Convert to ascii
9. Encode a string
10. Decode a string
x. To Exit""")

# Loop infinitely running through menu code
while True:
    clear_terminal()
    menu_print()

    def enter(): # Function which asks user to press "enter" to continue
        enter = input("Press Enter to continue")

    def helloWorld(): # Prints "Start of Output", "Hello World", and "End of Output"
        print("----Start of Output ---------------------------")
        print("")
        print("Hello World")
        print("")
        print("----End of Output -----------------------------\n\n\n")
        enter()
    
    def goodbye_world(): # Displays "Hello World" before pausing and prompting user to continue
        print("----Start of Output ---------------------------")
        print("")
        print("Hello World")

        # Collects input to finish running program
        userInput = input("------> Program paused - press enter to continue")

        # Program continues after waiting for user to input anything
        print("Goodbye World")
        print("")
        print("----End of Output -----------------------------\n\n\n")
        enter()
    
    def goodbye_person(): # Prints "Hello World" before prompting user for their name and saying "Goodbye" to them.
        print("----Start of Output ---------------------------")
        print("")
        print("Hello World")

        # Asks for user's name to personalise "goodbye" statement
        userInput = input("What is your name ? ")

        # Prints personalised statement saying goodbye to user
        print(f"Goodbye {userInput}")
        print("")
        print("----End of Output -----------------------------\n\n\n")
        enter()
    
    def good_teacher(): # Requests input for teacher's name and tells user if the teacher is great or okay.
        print("----Start of Output ---------------------------")
        print("")

        # User enters teacher's name to determine if they are good in a personalised message.
        userInput = input("Teacher's name (try Mr Horan) ")
        if userInput == "Mr Horan": # If the user entered "Mr Horan"
            print("You are lucky, he is a great teacher.")
            print("")
        else: # If user entered the name of any other teacher
            print(f"{userInput} is an ok teacher")
            print("")
        print("----End of Output -----------------------------\n\n\n")
        enter()

    def for_loop(): # Prints the numbers 1 to 499 inclusive
        print("----Start of Output ---------------------------")
        print("")

        # Loop cycling through all numbers between 1 and 500 (excluding 500)
        for number in range (1, 500): 
            print(number) # Prints every number in the sequence
        print("")
        print("----End of Output -----------------------------\n\n\n")
        enter()

    def for_loop_two(): # Cycles through numbers from 10 to 1 four times, each time the numbers appear under heading of run time number.
        print("----Start of Output ---------------------------")
        print()

        # Loop cycling through numbers 1-4 inclusive for run time headings
        for number in range (1, 5):
            print(number) # Prints run time heading

            # Loop within this loop cycling through numbers from 10 backwards
            for NUMBER in range (10, 0, -1):
                print(f"Test - {NUMBER}") # Prints each number from 10 to one
        print()
        print("----End of Output -----------------------------\n\n\n")
        enter()

    def whileLoop(): # Congratulates user only if they correctly name the subject
        print("----Start of Output ---------------------------")
        print()
        while True:
            userInput = input("What is the name of this subject ")
            if userInput == "Computing Technology":
                print("\n\n Congratulations!!")
                print("\n\n\n----End of Output -----------------------------\n\n\n")
                break
            else: # If user did not enter "Computing Technology"
                print("Not Correct - try again")
            continue
        enter()

    def string_loop(): # Prints user's string as one letter per line
        print("----Start of Output ---------------------------\n")
        userInput = str(input("What is your string? "))
        for string in str(userInput): # Loop cycling through all letters in user's input and printing them each on different lines
            print(string)
        print("\n----End of Output -----------------------------\n\n\n")
        enter()

    def convert_ascii(): # Converts user's string to ASCII numbers
        print("----Start of Output ---------------------------\n")
        userInput = str(input("What is your string? "))
        for string in str(userInput): # Loop cycling through characters entered by user
            ASCII = ord(string) # Converts character to ASCII number
            print(f"{string} = {ASCII}") 
        print("\n----End of Output -----------------------------\n\n\n")
        enter()

    def encode_string(): # Encodes user's string by shifting all letters up one in the alphabet
        print("----Start of Output ---------------------------\n")
        empty_list = [] # Creates empty list to store numbers in
        userInput = str(input("What is your string? "))
        for string in str(userInput): # Loop running through letters in user's input
            ASCII = ord(string) # Converts character to ASCII
            new_letter_value = ASCII + 1 # Shifts ASCII value one up
            new_letter = chr(new_letter_value) # Convert new ASCII value back to English
            empty_list.append(new_letter) # Add new character to empty list
            print(f"{string}={new_letter}") 
            print("".join(empty_list)) # Print letters in list without spaces
        print("\n----End of Output -----------------------------\n\n\n")
        enter()

    def decode_string(): # Decodes user's string by shifting all letters down one in the alphabet
        print("----Start of Output ---------------------------\n")
        empty_list = [] # Creates empty list to store numbers in
        userInput = str(input("What is your string? "))
        for string in str(userInput): # Loop running through letters in user's input
            ASCII = ord(string) # Converts character to ASCII
            new_letter_value = ASCII - 1 # Shifts ASCII value one down
            new_letter = chr(new_letter_value) # Convert new ASCII value back to English
            empty_list.append(new_letter) # Add new character to empty list
            print(f"{string}={new_letter}")
            print("".join(empty_list)) # Print letters in list without spaces
        print("\n----End of Output -----------------------------\n\n\n")
        enter()

    def invalid_option(): # Function tells user they have entered an invalid character and reprompts them
        print("----Start of Output ---------------------------\n")
        print("invalid option\n")
        print("----End of Output -----------------------------\n\n\n")
        enter()

    userINPUT = input("Enter an option ")
    print()
    if userINPUT == "1":
        helloWorld()
    elif userINPUT == "x" or userINPUT == "X":
        sys.exit() # Function that terminates menu
    elif userINPUT == "2":
        goodbye_world()
    elif userINPUT == "3":
        goodbye_person()
    elif userINPUT == "4":
        good_teacher()
    elif userINPUT == "5":
        for_loop()
    elif userINPUT == "5.5":
        for_loop_two()
    elif userINPUT == "6":
        whileLoop()
    elif userINPUT == "7":
        string_loop()
    elif userINPUT == "8":
        convert_ascii()
    elif userINPUT == "9":
        encode_string()
    elif userINPUT == "10":
        decode_string()
    else: 
        invalid_option()