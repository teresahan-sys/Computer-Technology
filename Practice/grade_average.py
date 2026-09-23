empty_list = []

while True:
    try: 
        user_input = int(input("What was your maths score? "))
        if user_input < 0 or user_input > 100:
            print("Enter a number between 0 and 100 only!")
            continue
        user_input2 = int(input("What was your science score? "))
        if user_input2 < 0 or user_input > 100:
            print("Enter a number between 0 and 100 only!")
            continue
        user_input3 = int(input("What was your English score? "))
        if user_input3 < 0 or user_input > 100:
            print("Enter a number between 0 and 100 only!")
            continue
        empty_list.extend([user_input, user_input2, user_input3])
        for number in empty_list:
            print(f"Score: {number}.")
        print(f"Average score was {(sum(empty_list))/3}")
        break
    except ValueError:
        print("Enter an integer between 0 and 100!")
        continue