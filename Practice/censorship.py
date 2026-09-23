while True:
    empty_string = ""
    user_input = input("Enter a sentence: ").lower()
    empty_string = empty_string + user_input
    input2 = input("Which word would you like to ban? ").lower()
    if input2 in empty_string:
        asterixes = len(input2)
        total_asterixes = asterixes*"*"
        happiness = empty_string.replace(input2, total_asterixes)
        print(f"Your censored sentence is: {happiness}.")
        break
    else: 
        print("Invalid word!")
        continue