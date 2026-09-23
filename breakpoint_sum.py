def calculate_sum(numbers):
    total = 0
    for i in range(0, len(numbers) - 1, 2):
        val = numbers[i]
        total = total + val
    return total

my_list = [10, 20, 30, 4, 1, 2]
result = calculate_sum(my_list)
print(f"Total is: {result}")