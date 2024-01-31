inventories = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

def displayInventory(inventories):
    totalNumberOfItems = 0
    print('Inventory: ')
    for k, v in inventories.items():
        print(f"{v} {k}")
        totalNumberOfItems += v
    print(f"Total Number of Items: {totalNumberOfItems}")


# displayInventory(inventories)


# project 2
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)