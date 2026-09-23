# Program decrypting user file using their provided encryption offset key

print("----Start of Output ---------------------------\n")
print("This decryption program shifts the letters in your input to determine the original message")
empty_list = "" # Empty list for storing letters
while True:
    user_file_input = input("\nEnter encrypted file's name ").strip().strip('"') # Asks for file name, removes spaces and characters that cause a crash
    try:
        with open(user_file_input, 'r', encoding='utf-8') as file:
            content = file.read() # Try to open and read user's file
    except FileNotFoundError: # If file does not exist
        print("Invalid file")
        continue
    file_output = input("Enter name of file to output decryption into ").strip().strip('"')
    clear_file = input("\nWould you like to clear the output file? YES/NO ") # In case user types an existing file that is not blank
    if clear_file == "YES" or clear_file == "yes" or clear_file == "Yes":
        open(file_output, 'w') # Opens file in writing mode which deletes previous contents in file
    elif clear_file == "NO":
        pass
    output_key = int(input("\nEnter encryption key "))
    decryption_number = -(output_key) # Inverses encryption key to shift encrypted letters backward 
    for string in str(content): # For letter in user's file
        ASCII = ord(string) # Convert letter to ASCII
        if 32 <= ASCII <= 126:
            new_letter_value = ASCII + decryption_number # Finds ASCII of letter before it was encoded
            new_letter = chr(new_letter_value) # Converts new ASCII value back to English
            add_letter_to_list = empty_list + new_letter # Adds decrypted English character to the empty list storing the word
            with open(file_output, 'a', encoding='utf-8') as file:
                file.write(add_letter_to_list) # Add letter to desired decryption file
    print("\nYour message has been decrypted.")
    break
print("\n----End of Output -----------------------------")