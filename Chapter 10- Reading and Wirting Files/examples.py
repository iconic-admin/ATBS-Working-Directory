from pathlib import Path

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(Path(r'C:/Users/Al', filename))

Path('spam') / 'bacon' / 'eggs'
Path('spam') / Path('bacon/eggs')
Path('spam') / Path('bacon', 'eggs')