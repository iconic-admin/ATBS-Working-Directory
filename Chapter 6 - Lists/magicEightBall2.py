import random

outcomes = ['It is certain.',
            'It is decidedly so.', 
            'Reply hazy try again.', 
            'Ask again later.', 
            'Concentrate and ask again.', 
            'My reply is no.', 
            'Outlook not so good.', 
            'Very doubtful.']

print('Ask a yes or no question: ')
input('--|>')
print(outcomes[random.randint(0, len(outcomes) - 1)])
print(random.choice(outcomes))