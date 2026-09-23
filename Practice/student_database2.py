data = {
    "Alice": [85, 90, 78],
    "Bob": [60, 70, 65],
    "Sophia": [10, 40, 99],
}

while True:
    empty_list = []
    user_input = input("Would you like to calculate a student's average or identify the student with the highest mark in a subject? TYPE 1 OR 2: ")
    if user_input == "1":
        INPUT = input("Type name of the student whose average is desired: ")
        if INPUT in data:
            GET = data[INPUT]
            average = sum(GET)/ len(GET)
            print(f"{INPUT}'s average was {average:.2f}.")
            break
        else:
            print("That is an invalid name!")
            continue
    elif user_input == "2":
        another_input = input("For which subject would you like to identify the top student? TYPE 1, 2 OR 3: ")
        if another_input == "1":
            for student in data:
                first_mark = data[student][0]
                empty_list.append(first_mark)
            highest_mark = empty_list.index(max(empty_list))
            turn_to_list = list(data)[highest_mark]
            print(f"The student with the highest mark was {turn_to_list}!")
            break
        elif another_input == "2":
            for student in data:
                first_mark = data[student][1]
                empty_list.append(first_mark)
            highest_mark = empty_list.index(max(empty_list))
            turn_to_list = list(data)[highest_mark]
            print(f"The student with the highest mark was {turn_to_list}!")
            break
        elif another_input == "3":
            for student in data:
                first_mark = data[student][2]
                empty_list.append(first_mark)
            highest_mark = empty_list.index(max(empty_list))
            turn_to_list = list(data)[highest_mark]
            print(f"The student with the highest mark was {turn_to_list}!")
            break
        else:
            print("Invalid subject number!")
            continue
    else:
        print("Invalid option entered!")
        continue