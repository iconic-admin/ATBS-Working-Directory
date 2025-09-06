"""

Write a function that takes a string and does the same
thing as the strip() string method. If no other arguments
are passed other than the string to strip, then the function
should remove whitespace characters from the beginning
and end of the string. Otherwise, the function should
remove the characters speciﬁed in the second argument to
the function.

"""

import re

def regularStrip(text, removeThis=None):
    if removeThis is None:
        beginningWhiteSpace = re.compile(r'^\s+')
        endingWhiteSpace = re.compile(r'\s+$')
        outputText = beginningWhiteSpace.sub('', text)
        outputText = endingWhiteSpace.sub('', outputText)
        return(outputText)
    else:
        regexToRemove = re.compile(removeThis)
        outputText = regexToRemove.sub('', text)
        return(outputText)

testText = '       Test text goes here.        '
print(testText)
print(regularStrip(testText))
print(regularStrip(testText, 'x'))