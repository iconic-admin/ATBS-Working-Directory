"""

Write a function that uses regular expressions to make
sure the password string it is passed is strong. A strong
password has several rules: it must be at least eight
characters long, contain both uppercase and lowercase
characters, and have at least one digit. Hint: It’s easier to
test the string against multiple regex patterns than to try to
come up with a single regex that can validate all the rules.

"""

import re

def strongPasswordDectector(password):
    detectUpperCase = re.compile(r'[A-Z]')
    detectLowerCase = re.compile(r'[a-z]')
    detectDigit = re.compile(r'\d')
    if len(password) < 8:
        print('Password must be longer than 7 characters.')
    elif detectLowerCase.search(password) == None:
        print('Password must contain at least one lower case letter.')
    elif detectUpperCase.search(password) == None:
        print('Password must contain at least one uppercase letter.')
    elif detectDigit.search(password) == None:
        print('Password must contain at least one digit.')
    else:
        print('Password is strong.')

print('adhsydhnf9')
strongPasswordDectector('adhsydhnf9')
print()
print('aD9')
strongPasswordDectector('aD9')
print()
print('CHAGDTDYSU9')
strongPasswordDectector('CHAGDTDYSU9')
print()
print('adhsydAhnf')
strongPasswordDectector('adhsydAhnf')
print()
print('adhsydAhnf9')
strongPasswordDectector('adhsydAhnf9')