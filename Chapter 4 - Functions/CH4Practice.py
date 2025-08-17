"""Write a function named collatz() that has one parameter
named number. If number is even, then collatz() should print
number // 2 and return this value. If number is odd, then
collatz() should print and return 3 * number + 1."""

def collatz(number):
    if (number % 2) == 0:
        number = number //2
    else:
        number = 3 * number + 1
    print(number, end=' ')
    return number

print('Enter number: ')

while True:
    try:
        userNumber = int(input('>'))
        break
    except ValueError:
        print('Input must be an integer value.')

while userNumber != 1:
    userNumber = collatz(userNumber)

"""Then, write a program that lets the user enter an
integer and that keeps calling collatz() on that number until
the function returns the value 1. (Amazingly enough, this
sequence actually works for any integer; sooner or later,
using this sequence, you'll arrive at 1! Even
mathematicians aren't sure why. Your program is
exploring what's called the Collatz sequence, sometimes
called “the simplest impossible math problem.”)
Remember to convert the return value from input() to
an integer with the int() function; otherwise, it will be a
string value. To make the output more compact, the print()
calls that print the numbers should have a sep=' ' named
parameter to print all values on one line.
The output of this program could look something like
this:
Enter number:
3
3 10 5 16 8 4 2 1
Hint: An integer number is even if number % 2 == 0, and it's
odd if number % 2 == 1."""

"""Input Validation
Add try and except statements to the previous project to
detect whether the user entered a non-integer string.
Normally, the int() function will raise a ValueError error if it
is passed a non-integer string, as in int('puppy'). In the except
clause, print a message to the user saying they must enter
an integer."""