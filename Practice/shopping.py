shop_items = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.80
}

user_input = input("Enter an item name: ")
if user_input.lower() in shop_items:
    item = shop_items.get(user_input.lower())
    print(f"The cost of {user_input} is ${item:.2f}.")
else:
    shop_items[user_input] = 0.00