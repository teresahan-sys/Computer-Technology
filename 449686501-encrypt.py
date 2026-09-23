# Program encrypting message in user file using their provided offset key

print("----Start of Output ---------------------------\n")
        print("This encryption program shifts the letters in your input by however much you wish")
        empty_list = "" # Prepares empty list to store letters in
        while True:
            user_file_input = input("\nEnter file name ").strip().strip('"') # Asks for an existing file with desired message, removes spaces and characters that cause Python to crash
            try:
                with open(user_file_input, 'r', encoding='utf-8') as file: # Try to open and read user's file
                    content = file.read()
            except FileNotFoundError: # If file user entered does not exist
                print("Invalid file")
                continue
            file_output = input("Enter name of file to output information into ").strip().strip('"')
            clear_file = input("\nWould you like to clear the output file? YES/NO ")
            if clear_file == "YES" or clear_file == "yes" or clear_file == "Yes":
                open(file_output, 'w')
            elif clear_file == "NO":
                pass
            output_key = int(input("\nEnter desired encryption key "))
            for string in str(content): # For letter in user's file
                ASCII = ord(string) # Convert letter to ASCII
                if 32 <= ASCII <= 126:
                    new_letter_value = ASCII + output_key # Add user's desired encryption key onto the letter's value
                    new_letter = chr(new_letter_value) # Turn new letter's value back to English
                    add_letter_to_list = empty_list + new_letter # Add encrypted letter to empty list
                    with open(file_output, 'a', encoding='utf-8') as file:
                        file.write(add_letter_to_list) # Add letter to file
                else: # Ignore special characters with ASCII numbering of less than 32
                    pass
            print("\nYour message has been encrypted.")
            break
        print("\n----End of Output -----------------------------")