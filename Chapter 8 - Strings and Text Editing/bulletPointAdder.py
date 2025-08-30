# takes seperate lines of text (not a paragraph)
# and adds bullet points to all lines

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
# Loop through all indexes in the "lines" list.
for i in range(len(lines)): 
    # Add a star to each string in the "lines" list.
    lines[i] = '* ' + lines[i] 
text = '\n'.join(lines)
pyperclip.copy(text)