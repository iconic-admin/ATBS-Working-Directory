message = 'It was a dark warm day in December, and the clocks were not working because they where on a union mandated break.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)