def getInteger():
    while True:
        try:
            x = input ("What is the number")
            y = int(x)
            return y
        except:
            print("Error!")

print(getInteger() + 5)