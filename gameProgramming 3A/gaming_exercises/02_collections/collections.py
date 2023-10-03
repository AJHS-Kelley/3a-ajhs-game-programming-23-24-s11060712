# Collections, Kloeckner Gavin, v0.1
# Adding items

playerInventory = []
while len(playerInventory) < 10:
    item = input("What would you like to add?\n")
    playerInventory.append(item)
playerInventory.sort()
# .whatever() is known as a method. It means "do this to that".
print(playerInventory)

# Removing Items
while len(playerInventory) < 5:
    item = input("Now, please select the item that you would like to remove from the inventory.\n")
    playerInventory.remove(item)
playerInventory.sort()

print(playerInventory)