def printTable(tableInput):
    # make the list of lists into a single list for comparison
    lengthCompareList = []
    for subList in tableInput:
        for item in subList:
            lengthCompareList.append(item)
    
    # find the longest string in the input data, using the
    # single list from above
    longestLength = 0
    for datum in lengthCompareList:
        if len(datum) > longestLength:
            longestLength = len(datum)

    # now we have the correct length to right justify the
    # text output
    for row in range(len(tableInput[0])):
        for col in range(len(tableInput)):
            print(tableInput[col][row].rjust(longestLength), end=' ')
        print()

    # debug prints, I know I'm supposed to use debug statements
    # but they take too long to setup for a program of 
    # this length
    # print(lengthCompareList)
    # print(longestLength)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'David', 'Samwise', 'MrMan'],
             ['dogs', 'cows', 'mice', 'goblins']]

printTable(tableData)