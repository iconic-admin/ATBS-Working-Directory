import random
for i in range(100): # perform 100 coin flips
    if random.randint(0, 1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print() # prints one new line at the end