# Ask user for two integers from keyboard, add them together and print result

def getInteger(): # Get integer from keyboard, if invalid input, reprompt user and try again
    while True:
        x = input("What is the number ")
        try:
            y = int(x) # Only return a value when it is a guaranteed integer
            return y
        except:
            x = input("What is the number ")

x = getInteger()
y = getInteger()
z = x + y
print(f"{x} + {y} = {z}") # converts the integers to strings before printing