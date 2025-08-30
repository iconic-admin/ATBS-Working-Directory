import pyperclip

text = pyperclip.paste() # get text off of the clipboard
altText = '' # string to hold alternate case
makeUppercase = False

for character in text:
    # add each character to altText
    if makeUppercase:
        altText += character.upper()
    else:
        altText += character.lower()

    # set makeUppercase to its alternate value
    makeUppercase = not makeUppercase
pyperclip.copy(altText) # put result in clipboard
print(altText) # print result on screen also