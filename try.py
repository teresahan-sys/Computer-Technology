while True:
    def getInteger():
        userInput = int(input("Enter a number "))
        return(userInput)
    try:
        print (getInteger() + 5)
    except:
        print("That is an invalid character")
    else:
        print("No errors were raised")
        break
