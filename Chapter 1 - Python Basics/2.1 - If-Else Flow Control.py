name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age <12:
    print('You are not Alice kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, granny.')
else:
    print('You are neither Alice nor a little kid.')

todayIsOppositeDay = True

# set sayItIs OppositeDay based on todayIOppositeDay
if todayIsOppositeDay == True:
    sayItIsOppositeDay = True
else:
    sayItIsOppositeDay = False

# if it is opposite day, toggle sayItIsOppositeDay
if todayIsOppositeDay == True:
    sayItIsOppositeDay = not sayItIsOppositeDay

# say what day it is
if sayItIsOppositeDay == True:
    print('Today is Opposite Day.')
else:
    print('Today is not Opposite Day')