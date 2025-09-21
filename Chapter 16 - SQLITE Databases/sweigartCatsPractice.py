import sqlite3

dbConnection = sqlite3.connect('sweigartcats.db', isolation_level=None)
for row in dbConnection.execute('SELECT * FROM cats'):
    print('Row data: ', row)
    print(row[0], 'is one of my favorite cats.')

"""

The for loop can iterate over the tuples of row data
returned by conn.execute() without calling fetchall(), and the
code in the body of the for loop can operate on each row
individually, because the row variable populates with a
tuple of row data from the query. The code can then access
the columns using the tuple’s integer index: index 0 for the
name, index 1 for the birthdate, and so on.

"""