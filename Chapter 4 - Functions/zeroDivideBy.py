def spam(divideBy):
    try:
        return 42 / divideBy #for any non-zero input
    except:
        print('Error: Invalid argument.') #incase of non-zero or string input

print(spam(2))
print(spam("ham"))
print(spam(0))
print(spam(1))

"""    return 42 / divideBy
           ~~~^~~~~~~~~~
ZeroDivisionError: division by zero"""

