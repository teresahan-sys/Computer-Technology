# Program testing encrypted file against common English words to attempt brute force decryption

print("----Start of Output ---------------------------\n")

import sys

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
    english_dictionary = input("\nEnter dictionary file name ").strip().strip('"')
    try:
        with open(english_dictionary, 'r', encoding='utf-8') as file:
            find_words = file.read().splitlines() # Read file with top 1000 words, turn it into a list
    except FileNotFoundError:
        print("Invalid file")
        continue

    for possible_key in range(256): # Loop cycling through letters in encrypted file
        empty_string = "" # String to store possible decrypted messasge

        # Loop applying possible key to all characters in the cycle
        for character in str(content):
            decryption = (ord(character) - (possible_key)) % 256 # Applies key to encrypted character
            empty_string = empty_string + chr(decryption) # Converts possibly decrypted character to English and adds to empty string
        if any(word in empty_string for word in find_words if len(word) > 3): # If known word appears in possible decrypted character list
            print("Key has been found! \nDecrypting file now. ")

            # Loop cycling through letters in encrypted file and decrypting them
            for letter in str(content):
                ASCII = ord(letter) # Convert letter to ASCII
                new_letter_value = (ASCII - possible_key) % 256 # Apply key to encrypted letter
                new_letter = chr(new_letter_value) # Convert decrypted letter back to English
                final_decrypted_message.append("".join(new_letter)) # Remove spaces and add letter to list holding final message
            with open(file_output, 'a', encoding='utf-8') as file:
                file.write("".join(final_decrypted_message)) # Open file, converts list to string and adds string to file
            print("\nYour message has been decrypted.")
            sys.exit()
        else: # If known word does not appear in decrypted character list
            print("Encryption key not found. Continuing the search...")
            continue
    else: # If the user's known word cannot be found in encrypted file using every possible key
        print("""Top words are not in encrypted file.
Decryption failed.""")
        continue
print("\n----End of Output -----------------------------")