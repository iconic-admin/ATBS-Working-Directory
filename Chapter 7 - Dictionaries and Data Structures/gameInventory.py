stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        # my code starts here
        print(str(v) + ' ' + str(k))
        item_total += v
        # my code ends here
    print("Total number of items: " + str(item_total))

display_inventory(stuff)

def add_to_inventory(inventory, added_items):
    # Your code goes here.
    # my code starts here
    for loot in added_items: # for every item in this list
        if loot in inventory: # if it matches an existing item in the inventory
            inventory[loot] += 1 # iterate that item by one
        else:                # if it doesn't match an item in the inventory
            inventory[loot] = 1 # add it to the inventory with an initial value of 1
    return(inventory)
    # my code stops here

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)