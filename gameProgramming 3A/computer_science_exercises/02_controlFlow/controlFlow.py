# Gavin Kloeckner, Control Flow, v0.6

# DECLORATIONS
favColor = "Green"
luckyNum = 6
myGPA = 4.0
myAge = 17
pineappleOnPizza = False

# if Statement
if luckyNum > 30: # luckyNumber > 30 is a Conditional Expression
    print("Good choice!")
if myGPA >= 3.8:
    print("Great job! You get a cookie")

# if-else Statement
if myAge < 21:
    print("You are not old enough to legally drink yet.")
else:
    print("You are at the legal age to drink")

if pineappleOnPizza != False:
    print("You have poor taste.")
else:
    print("You actually have common sense.")

# if - elif - else Statement
if favColor == "Green":
    print("Nice choice of color!")
elif favColor == "Blue":
    print("Still not as cool as green!")
elif favColor == "Red":
    print("That's my second favorite color!")
else:
    print("Okay, cool.")
# 99% of the time, check for the highest value first!

# Nested if / elif / else statements
if myAge > 50:
    print("What was it like riding to school on a dinosaur?")
    if myAge < 40:
        print("You look older than your age.")
    else:
        print("Ok, you're young enough to be cool.")
else:
    print("Ok, cool.")

if myGPA < 3.0:
    print("You are almost there to get the honor roll!.")
    if myGPA < 2.7:
        print("Are you even trying? Come on, dude.")
    else:
        print("Okay, you're on the right track.")
else:
    print("Great job! you're apart of the honor roll!")


# while Loop -- think of Musical Chairs -- Best used when you do not know how many times the loop must run.
# loopCounter = 0
# while loopCounter < 100:    
#     print(f"The current loop count is {loopCounter}.")
#     loopCounter += 1
# # loopCounter is equal to 99 after finishing!
# while loopCounter >= 0:
#     print(f"The nuke will launch in {loopCounter} second(s).")
#     loopCounter -= 1

# loopCounter = 0
# while loopCounter < 101:    
#     print(f"The current loop count is {loopCounter}.")
#     if loopCounter % 2 == 0:
#         print(f"{loopCounter} is even.")
#     else:
#         print(f"{loopCounter} is odd.")
#     loopCounter += 1

# for Loop -- Think of Go Fish! -- Used when you know the number of iterations needed.
for eachNumber in range(10):
    # eachNumber is known as the 'iterable variable'
    # range(x) specifies the numbers from 0 to x, Not Inclusive
    print(eachNumber)