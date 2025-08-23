print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)

# it is concatenating them as a string
# not adding them as a number

print('Enter the first number to add:')
first = int(input())
print('Enter the second number to add:')
second = int(input())
print('Enter the third number to add:')
third = int(input())
sum = first + second + third
print('The sum is ' + str(sum))

# this way it forces the input to be an integer
# then adds them together correctly
# the concatenates the sum with the rest of the output