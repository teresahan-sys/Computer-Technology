while True:
    while True:
        try:
            number = float(input("Pick your first number: "))
            another_number = float(input("Pick your second number: "))
            operation = (input("Choose your operation: "))
        except ValueError:
            print("That is an invalid value.")
            break
   
        if operation == "+" or operation == "addition":
            print(f"Your answer is {number + another_number}")
            break
        elif operation == "-" or operation == "subtraction":
            print(f"Your answer is {number - another_number}")
            break
        elif operation == "*" or operation == "multiplication":
            print(f"Your answer is {number * another_number}")
            break
        else:
            try:
                print(f"Your answer is {number / another_number}")
                break
            except ZeroDivisionError:
                print("That is an undefined request.")
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