import random
numberOfStreaks = 0
for experimentNumber in range(100000): # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    flipList = []
    for flip in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            flipList.append('H')
        else:
            flipList.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(flipList)):
        if flipList[i:i+6] == ['H', 'H', 'H', 'H', 'H', 'H']:
            numberOfStreaks += 1
            break
        if flipList[i:i+6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            numberOfStreaks += 1
            break

# print(numberOfStreaks)
print('Chance of streak: ' + str((numberOfStreaks/100000) * 100) + '%%')