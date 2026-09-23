dictionary = {
    "Bob": [4, 5],
    "Sophia": [10, 4],
    "Pencil": [3, 0],
}

print(dictionary)
dictionary["Hello"] = [1, 2]
print(dictionary)

practice_getting_stuff = dictionary["Bob"]
print(practice_getting_stuff)

print(list(dictionary))