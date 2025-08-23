def getUserGeneratedList():
    # first build a list from user input
    print('Enter list items, enter nothing to continue: ')
    userInput = 'a'
    userGeneratedList = []
    while userInput != '':
            userInput = input('--|>')
            if userInput != '':
                userGeneratedList.append(userInput)
    return userGeneratedList

userGeneratedList = getUserGeneratedList()

while len(userGeneratedList) == 0:
     print('You must enter at least one list item.')
     userGeneratedList = getUserGeneratedList()

# place a check here such that if the userGeneratedList is of
# length 0 or empty, it starts over.

# print(userGeneratedList)

# build a string form the list
outputString = ''
for i in range(len(userGeneratedList)):
    if i == 0:
         outputString = userGeneratedList[i]
    elif i == len(userGeneratedList) - 1:
         outputString = outputString + ', and ' + userGeneratedList[i]
    else:
        outputString = outputString + ', ' + userGeneratedList[i]

# print final output
print(outputString)