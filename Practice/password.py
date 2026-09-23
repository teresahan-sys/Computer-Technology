import string
import random

combined_strings = string.digits + string.punctuation + string.ascii_letters
empty_list = []

while True:
    try:
        user_input = int(input("How long would you like your password to be? "))
        if user_input <= 0:
            print("Please enter an appropriate length!")
            continue
    except ValueError:
        print("Please enter an integer!")
        continue
    for thing in range(user_input):
        thing = random.choice(combined_strings)
        empty_list.append(thing)
    join_my_list = "".join(empty_list)
    print(f"Your password is: {join_my_list}")
    break