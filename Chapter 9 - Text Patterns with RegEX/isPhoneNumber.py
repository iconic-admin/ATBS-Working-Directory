def isPhoneNumber(text):
    # phone numbers have 12 characters
    if len(text) != 12:
        return False
    
    # the first three characters must be numbers
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        
    # fourth character must be a dash
    if text[3] != '-':
        return False
    
    # next three characters must be numbers
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        
    # eighth character must be a dash
    if text[7] != '-':
        return False
    
    # last four characters must be numbers
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    # if no disqaulifiers found, return True
    return True

print('Is 415-555-4242 a phone number?', isPhoneNumber('415-555-4242'))
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?', isPhoneNumber('Moshi moshi'))
print(isPhoneNumber('Moshi moshi'))