def doMaths(int1, int2):
    if int1 % 2 == 0 and int2 % 2 == 0:
        print("both numbers are even")
    int3 = int1/int2
    if (int1 % int2 == 0):
        print(f"{int2} is divisible by {int1}")
    
    for i in range(5):
        int1 += i
    
    print(f"new int 1 is {int1}")


doMaths(4,2)