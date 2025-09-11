# walk through a folder tree
# search for files with a specific extension
# copy files to a new folder location

import os, shutil, re
from pathlib import Path

pattern = re.compile(r'.*\.py$') # checking for files with .py extension

fileObject = Path('./')
# print() # debug line
# print(fileObject) # checking validity of fileObject

for folderName, subfolders, filenames in os.walk(fileObject):
    folderName = Path(folderName) # ensures folderName is a Path object
    for filename in filenames:
        if pattern.search(filename):
            (Path.home() / 'spam').mkdir(parents=True, exist_ok=True)
            shutil.copy(folderName / filename, Path.home() / 'spam')

# shutil.copytree(fileObject, Path.home() / 'spam')