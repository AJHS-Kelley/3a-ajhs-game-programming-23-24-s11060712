integers = input()
a, b, c = integers.split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
    a, b = b, a
if c < b:
    c, b = b, c
if a > b:
    a, b = b, a


order = input()
myString = ""

for i in range(len(order)):
    if order[i] == "A":
        myString += str(a) + " "
    elif order[i] == "B":
        myString += str(b) + " "
    else:
        myString += str(c) + " "
print(myString)