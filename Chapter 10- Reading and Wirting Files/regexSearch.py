"""

Write a program that opens all .txt ﬁles in a folder and searches for any line that matches a user-supplied regular expression, then prints the results to the screen.

"""

# get a regex pattern from the user
# for file in thisDirectory:
#   open file and scan for matching regex pattern
#   print any matches found

import re, os
from pathlib import Path

print('Input a regular expression: ')
inputString = input()
pattern = re.compile(inputString)

thisDir = Path(__file__).parent

for file in thisDir.glob('*.txt'): # loops through .txt files in the same dir and the script
    fileToRead = file.open()
    # print(fileToRead.read()) # testing for expected output
    fileText = fileToRead.read()
    print(pattern.findall(fileText))
    fileToRead.close()