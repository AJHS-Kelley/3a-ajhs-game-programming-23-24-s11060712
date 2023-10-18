# Functions, 10-18-23, Gavin Kloeckner, v0.1

def functionName(): # Function Signature 
    print("What is your name?\n")
    name = input("Please type your name in the space below.\n")
    print(f"Hello there {name}!\n")

# Call The Function
functionName()

def happyBirthday(numTimes, age):
    count = 0
    while count < numTimes:
        print("Happy Birthday!\n")
    count += 1
    print(f"Congratulations on turning {age}-years-old!\n")


happyBirthday(10, 36)
happyBirthday(5, 17)
happyBirthday(16, 15)
happyBirthday(6, 14)