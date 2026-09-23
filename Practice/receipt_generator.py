import sys

total = 0

while True:
        user_input = input("Enter an item price or type 'DONE' if finished: ")
        if user_input.upper() == "DONE":
            print(f"Your Receipt Total: ${total + 0.1*total: .2f}")
            print("Thank you for using this service!")
            sys.exit()
        else: 
            try:
                price = float(user_input)
                total = total + price
            except ValueError:
                print("Enter numbers only!")
                continue

