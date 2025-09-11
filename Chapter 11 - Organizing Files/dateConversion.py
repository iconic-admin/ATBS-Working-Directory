# detect U.S. style dating in files and change file
# names to EU style dating, all files are presumed to
# have dating of the style MM-DD-YYYY for thie exercise

import os, re, shutil
from pathlib import Path

# regex to detect the filename pattern
# I dislike regex
pattern = re.compile(r'(.*?)(\d{2})-(\d{2})-(\d{4})\.txt$')

currentDir = Path('./')

for folderName, subfolders, filenames in os.walk(currentDir):
    folderName = Path(folderName) # ensures folderName is a Path object
    for filename in filenames:
        match = pattern.search(filename)
        if match:
            prefix = match.group(1)
            month = match.group(2)
            day = match.group(3)
            year = match.group(4)

            newName = f'{prefix}{day}-{month}-{year}.txt'
            oldPath = folderName / filename
            newPath = folderName / newName
            
            print(f'Renaming {oldPath} to {newPath}.')
            shutil.move(oldPath, newPath)