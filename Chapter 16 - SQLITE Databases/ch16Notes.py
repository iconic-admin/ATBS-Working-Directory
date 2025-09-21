import sqlite3

conn = sqlite3.connect('example.db', isolation_level=None)
conn.execute('CREATE TABLE IF NOT EXISTS cats (name TEXT NOT NULL,birthdate TEXT, fur TEXT, weight_kg REAL) STRICT')
# <sqlite3.Cursor object at 0x00000201B2399540>

"""

NULL Analogous to Python’s None

INT or INTEGER Analogous to Python’s int type

REAL A reference to the mathematics term real number; analogous to Python’s float type

TEXT Analogous to Python’s str type

BLOB Short for Binary Large Object; analogous to Python’s bytes type and useful for storing entire ﬁles in a database

SQLITE does not have a Boolean type or a date/time data type

"""

sqlite3.sqlite_version
# '3.xx.xx'

conn.execute('PRAGMA TABLE_INFO(cats)').fetchall()
# [(0, 'name', 'TEXT', 1, None, 0), (1, 'birthdate', 'TEXT', 0, None, 0), (2, 'fur', 'TEXT', 0, None, 0), (3, 'weight_kg', 'REAL', 0, None, 0)]

# CRUD create (data), read, udpdate, delete

"""

• INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)
• SELECT rowid, * FROM cats ORDER BY fur
• UPDATE cats SET fur = "gray tabby" WHERE rowid = 1
• DELETE FROM cats WHERE rowid = 1

"""

conn.execute('INSERT INTO cats VALUES ("Zophie", "2021-01-24", "black", 5.6)')
# <sqlite3.Cursor object at 0x00000162842E78C0>

# Transactions: a unit of work in a database

"""

ACID
Atomic The transaction is carried out either
completely or not at all.
Consistent The transaction doesn’t violate
constraints, such as NOT NULL rules for columns.
Isolated One transaction doesn’t aﬀect other
transactions.
Durable If committed, the transaction results are
written to persistent storage, such as the hard drive.

"""

cat_name = 'Zophie'
cat_bday = '2021-01-24'
fur_color = 'black'
cat_weight = 5.6
conn.execute('INSERT INTO cats VALUES (?, ?, ?, ?)', [cat_name, cat_bday, fur_color, cat_weight])

# use ?,?,? notation to format insert execute() in programs
# to prevent SQL injection attacks

conn.execute('SELECT * FROM cats').fetchall()
# [('Zophie', '2021-01-24', 'black', 5.6)]

"""

The execute() method call for the SELECT query returns a
Cursor object. To obtain the actual data, we call the fetchall()
method on this Cursor object.

"""

"""

The example SELECT query has four
parts:
• The SELECT keyword
• The columns you want to retrieve, where * means “all
columns except rowid”
• The FROM keyword
• The table to retrieve data from; in this case, the cats
table
If you wanted just the rowid and name columns of records
in the cats table, your query would look like this:

"""

conn.execute('SELECT rowid, name FROM cats').fetchall()
# [(1, 'Zophie')]

