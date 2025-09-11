# walk through a folder tree
# indentify files over 100mb size
# print file names

# os.path.getsize()

import os
from pathlib import Path

fileObject = Path('./')
# print() # debug line
# print(fileObject) # checking validity of fileObject

for folderName, subfolders, filenames in os.walk(fileObject):
    folderName = Path(folderName) 
    # ensures folderName is a Path object
    for filename in filenames:
        if os.path.getsize(folderName / filename) > 105000000: 
            # 105000000 bytes is slightly over 100mb
            print(filename)