"""

Create a Mad Libs program that reads in text ﬁles and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text ﬁle. For example, a text ﬁle may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN wasunaffected by these events.

The program would ﬁnd these occurrences and prompt theuser to replace them:

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamedEnter a noun:
pickup truck

It would then create the following text ﬁle:
The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.

The program should print the results to the screen in addition to saving them to a new text ﬁle.

"""

import re, os
from pathlib import Path

scriptDirectory = Path(__file__).resolve().parent # ChatGPT helped me with this line
os.chdir(scriptDirectory)

#TODO read the input text file
# print(Path.cwd()) - debugging line
inputFile = open('./madlibinput.txt', 'r')
inputFileContent = inputFile.read()
# print(inputFileContent) - used to verify that file is read correctly

#TODO create a list of user input words, ADJECTIVE, NOUN, etc.
pattern = re.compile(r'\b(ADJECTIVE|NOUN|VERB)\b')
madWordList = list(pattern.findall(inputFileContent))
# print(madWordList) - testing for correct word list

#TODO get user input one word at a time, creating a new list 
#TODO of input words
userMadWords = []
for word in madWordList:
    if word == 'ADJECTIVE' or 'ADVERB':
        print(f'Enter an {word}: ')
        userInput = input()
        userMadWords.append(userInput)
    else:
        print(f'Enter a {word}: ')
        userInput = input()
        userMadWords.append(userInput)
# print(userMadWords) - testing correct user input list

#TODO make the output string with spaces for user input words
#TODO point python to the replacement words

#TODO print output string as an f string, inserting the 
#TODO user input words