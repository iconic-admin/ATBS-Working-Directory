import random

colors = ['red', 'blue', 'toupe', 'cyan', 'azul', 'yellow']

for index, color in enumerate(colors):
    print(str(index) + ' ' + color)

print(random.choice(colors))

print(colors)
random.shuffle(colors)
print(colors)