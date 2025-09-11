# find all files with given prefix, spam in this case
# locate gaps in file numbering
# renumber later files to fill in gaps

import os, re, shutil
from pathlib import Path

# checking for spam file name with followed by three digit
# numbering structure, then .txt
pattern = re.compile(r'(spam)(\d{3})(\.txt)$')

fileObject = Path('./')

# create a list of the files that match the pattern
files = []
for filename in os.listdir(fileObject):
    matchObject = pattern.search(filename)
    if matchObject:
        files.append((filename, int(matchObject.group(2))))

# sort the list
files.sort()
# print(files) # debug to verify expected list output

expectedNumber = 1
for filename, actualNum in files:
    matchObject = pattern.search(filename)
    prefix, number, extension = matchObject.groups()
    numberLength = len(number)

    if actualNum != expectedNumber:
        newName = prefix + str(expectedNumber).zfill(numberLength) + extension
        print(f'Renaming {filename} to {newName}...')
        shutil.move(filename, newName)
    expectedNumber += 1