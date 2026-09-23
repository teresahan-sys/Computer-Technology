while True:
    while True:
        try:
            number = float(input("Pick a number: "))
            another_number = float(input("Pick another number: "))
            operation = (input("Choose your operation: "))
        except ValueError:
            print("That is an invalid value.")
            break

        if operation == "+" or operation == "addition":
            print(f"Your answer is {number + another_number}")
            break
        elif operation == "-" or operation == "subtraction":
            if number > another_number:
                print(f"Your answer is {number - another_number}")
                break
            else: 
                print(f"Your answer is {another_number - number}")
                break
        elif operation == "*" or operation == "multiplication":
            print(f"Your answer is {number * another_number}")
            break
        else:
            if number > another_number:
                print(f"Your answer is {number / another_number}")
                break
            else: 
                print(f"Your answer is {another_number / number}")
                break
    
    while True:
        again = input("Do you want to continue calculating? Type 'yes' or 'no'. ")
        if again == 'yes':
            break
        elif again == 'no':
            break
        else: print("That is an invalid answer.")
    if again == 'yes':
        continue
    else: break