while True:
    try:
        user_input = int(input("Enter your integer score between 0 and 100: "))
        if user_input < 0 or user_input > 100:
            print("Invalid score!")
            continue
        elif user_input >= 90:
            print("Congratulations, you got an A grade!")
            break
        elif user_input > 79 and user_input < 90:
            print("You got a B!")
            break
        elif user_input < 80 and user_input > 69:
            print("...You got a C...")
            break
        else: 
            print("Maybe you would rather not know your grade...")
            break
    except ValueError:
        print("Invalid score! Please type a number.")
        continue