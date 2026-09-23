def get_integer():
    while True:
        try:
            userInput = float(input("Pick a number "))
            user_input = float(input("Pick another number "))
            break
        except ValueError:
            print("That is an invalid number.")
            continue
    sum_num = userInput + user_input
    return sum_num

print("I will add two numbers for you.")
print(get_integer())