# Program testing known word against encrypted file to find the encryption key and decrypt whole program

print("----Start of Output ---------------------------\n")

while True:
    final_decrypted_message = [] # Empty list to store the final message

    # Asks for encrypted file name, removes trailing spaces and quotation marks
    user_file_input = input("\nEnter encrypted file's name or press x to exit ").strip().strip('"')
    try:
        if user_file_input == "x":
            break # Exits program
        else: 
            with open(user_file_input, 'r', encoding='utf-8') as file:
                content = file.read() # Open and read the file
    except FileNotFoundError: # If user entered invalid/nonexistent file name
        print("Invalid file")
        continue
    file_output = input("Enter name of file to output information into ").strip().strip('"')
    clear_file = input("\nWould you like to clear the output file? YES/NO ")
    if clear_file == "YES" or clear_file == "yes" or clear_file == "Yes":
        open(file_output, 'w').close() # Opens file for writing to clear it, then closes file
    else: pass
    known_word = input("Enter your known word ")
    if known_word == "":
        print("That is an invalid word.")
        continue
    elif len(known_word) == 1:
        print("Known word contains too few letters and decryption may return nonsense")
        proceed_or_not = str(input("Do you wish to proceed? YES/NO "))
        if proceed_or_not == "YES":
            pass
        else: break
    else: pass
    for string in str(content): # Loop cycling through letters in encrypted file
        empty_string = "" # String to store possible decrypted message

        # Finds a possible key by taking the difference between first known letter and letter in encrypted file
        possible_key = ord(string) - ord(known_word[0])

        # Loop applying possible key to all characters in the cycle
        for character in str(content):
            decryption = ord(character) - (possible_key) # Applies key to encrypted character
            if decryption < 0: # Ignore potential keys that are less than zero
                pass
            else:
                empty_string = empty_string + chr(decryption) # Converts possibly decrypted character to English and adds to empty string
        if known_word in empty_string: # If known word appears in possible decrypted character list
            print("Key has been found! \nDecrypting file now. ")

            # Loop cycling through letters in encrypted file and decrypting them
            for letter in str(content):
                ASCII = ord(letter) # Convert letter to ASCII
                new_letter_value = ASCII - (possible_key) # Apply key to encrypted letter
                new_letter = chr(new_letter_value) # Convert decrypted letter back to English
                final_decrypted_message.append("".join(new_letter)) # Remove spaces and add letter to list holding final message
            with open(file_output, 'a', encoding='utf-8') as file:
                file.write("".join(final_decrypted_message)) # Open file, converts list to string and adds string to file
            print("\nYour message has been decrypted.")
            break
        else: # If known word does not appear in decrypted character list
            print("Encryption key not found. Continuing the search...")
            continue
    if known_word not in empty_string: # If the user's known word cannot be found in encrypted file using every possible key
        print("Known word is not in encryped file.")
        continue
print("\n----End of Output -----------------------------")