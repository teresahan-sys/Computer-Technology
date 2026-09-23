def calculate_final_price():
    while True:
        a = float(input("Enter the original price "))
        b = float(input("Enter the discount as a decimal "))
        if b > 1 or b < 0:
            print("That is invalid.")
            continue
        else: 
            break
    discount = a - (a*b)
    return discount    
    
print(f"Your discounted price is ${calculate_final_price()}")