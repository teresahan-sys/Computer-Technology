import random
count = 0
print("Let's play scissors, paper, rock!")
while True:
    winning_symbol = random.choice(["scissors", "paper", "rock"])
    guess = input("Pick one ")
    count = count + 1
    if guess == winning_symbol:
        print(f"I picked {winning_symbol} so...")
        print("We tied!")
        print("Have another go! Or type 'quit' to quit!")
    elif guess == "scissors" and winning_symbol == "paper":
        print(f"I picked {winning_symbol} so...")
        print("You win!")
        print(f"It took you {count} rounds!")
        break
    elif guess == "paper" and winning_symbol == "rock":
        print(f"I picked {winning_symbol} so...")
        print("You win!")
        print(f"It took you {count} rounds!")
        break
    elif guess == "rock" and winning_symbol == "scissors":
        print(f"I picked {winning_symbol} so...")
        print("You win!")
        print(f"It took you {count} rounds!")
        break
    elif guess == "quit":
        break
    else:
        print(f"I picked {winning_symbol} so...")
        print("You lose!")
        print("Have another go! Or type 'quit' to quit!")