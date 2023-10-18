# Functions, 10-18-23, Gavin Kloeckner, v0.2

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


#happyBirthday(10, 36)

def functionWithReturn(num1, num2):
    sum = num1 + num2
    quotient = sum / 5
    return quotient # returns immediately exits a function

def functionWithReturn(num1, num2):
    sum = num1 + num2
    quotient = sum / 5
    print(quotient)

example = functionWithReturn(4, 17)
print(example)

