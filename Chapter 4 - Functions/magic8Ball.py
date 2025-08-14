import random

def getAnswer(answerNumber):
    # returns a fortune answer based on what int answer_number is,
    #  1 to 9
    if answerNumber == 1:
        return 'It is certain.'
    elif answerNumber == 2:
        return 'It is decidedly so.'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'Reply hazy try again.'
    elif answerNumber == 5:
        return 'Ask again later.'
    elif answerNumber == 6:
        return 'Concentrate and ask again.'
    elif answerNumber == 7:
        return 'My reply is no.'
    elif answerNumber == 8:
        return 'Outlook not so good.'
    elif answerNumber == 9:
        return 'Very doubtful.'
    
print('Ask a yes or no question: ')
input('-->')

r = random.randint(1, 9)

fortune = getAnswer(r)

print(fortune)