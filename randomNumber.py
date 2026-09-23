import random
while True:
    number = random.randint(1, 10)
    count = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10! "))
            count = count + 1
            if guess == number:
                print("Congratulations, you win!")
                print(f"It took you {count} tries!")
                break
            elif guess < number and guess > 0:
                print("Your guess is too low")
            elif guess > number and guess <= 10:
                print("Your guess is too high")
            else:
                print("That is an invalid value")
                continue
        except ValueError:
            print("That is an invalid value")
            continue

    while True:
        again = input("Do you want to play again? Yes or no? ")
        if again != "yes" and again != "Yes":
            break
        elif again == "yes" or again =="Yes":
            break
    if again == "yes" or again == "Yes":
        continue
    else: break