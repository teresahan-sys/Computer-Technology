from datetime import date
today = date.today()
empty_list = []

print(f"Date: {today.strftime("%d/%m/%y")}")

while True: 
    user_input = int(input("How many people are attending from each class? "))
    if user_input == -1:
        break
    else: 
        empty_list.append(user_input)

average = sum(empty_list) / len(empty_list)
highest_score = max(empty_list)
lowest_score = min(empty_list)
print(f"Your average is {average:.1f}, highest attendance is {highest_score}, lowest attendance is {lowest_score}.")
relevant_classes = [num for num in empty_list if num > 25]
count = len(relevant_classes)
if count == 1:
    print(f"There is 1 class with more than 25 students in attendance.")
else:
    print(f"There are {count} classes with more than 25 students in attendance.")