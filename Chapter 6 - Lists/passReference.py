def eggsFunction(someParameter):
    someParameter.append('Hello')

spamList = [1, 2, 3]
eggsFunction(spamList)
print(spamList) # this will print the origonal spamList
                # with 'Hello' appened to the end