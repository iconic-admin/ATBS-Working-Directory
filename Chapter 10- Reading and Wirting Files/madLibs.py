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

# in my abandonned script, I tried to build a list of words
# from the madlib sentence, then replace them one at a time
# with a loop... I now see that in this exercise it is easier
# to walk through the sentence once and replace each word
# as it is found, on the spot.

# note after finishing this exercise: I used chatGPT and had 
# to look at the solution in the end to get this one

import re, os
from pathlib import Path

scriptDirectory = Path(__file__).resolve().parent # ChatGPT helped me with this line
os.chdir(scriptDirectory)

#TODO read the input text file
# print(Path.cwd()) # debugging line
inputFile = open('./madlibinput.txt', 'r')
inputFileContent = inputFile.read()
inputFile.close() 
# print(inputFileContent) # used to verify that file is read correctly

pattern = re.compile(r'\b(ADJECTIVE|ADVERB|NOUN|VERB)\b')

#TODO scan input for pattern matches and replace them

while True:
    madWord = pattern.search(inputFileContent)
    if madWord is None:
        break
    wordToReplace = madWord.group(0) # extracts the string from the madWord object
    if wordToReplace == 'ADJECTIVE' or wordToReplace == 'ADVERB':
        userInputWord = input(f'Enter an {wordToReplace}:')
    else:
        userInputWord = input(f'Enter a {wordToReplace}:')
    inputFileContent = pattern.sub(userInputWord, inputFileContent, 1)

# prints final output and also saves to a new
# .txt file created by the script
print(inputFileContent)
outputFileObject = open('madOutput.txt', 'w', encoding='utf-8')
outputFileObject.write(inputFileContent)
outputFileObject.close()