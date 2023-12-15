import myModule

x = 0
y = 0

xStart = myModule.getTime()
while x < 1000:
    myModule.dispDice(1, 20)
    x += 2
xStop = myModule.getTime()

yStart = myModule.getTime()
while y > -1000:
    myModule.rollDice(1, 20)
    y += -2
yStop = myModule.getTime()

print(f'The X loop required {myModule.execTime(xStart, xStop)}.\n')
print(f'The Y loop required {myModule.execTime(yStart, yStop)}.\n')