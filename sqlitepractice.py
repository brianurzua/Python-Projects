# SQLite3 practice 

import sqlite3

""" 
This will connect to database and if it doesn't exist yet,
then it will create a database.

"""
# connection = sqlite3.connect('test_database.db')

# This instantiates a cursor object that enables us to operate the database
# c = connection.cursor()

# This creates a table named People
# c.execute("Create Table People(FirstName TEXT, LastName TEXT, Age INT)")

# c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)") ''' Already in table '''

# This checks if table People exists, and if it does it deletes it with DROP
# c.execute("DROP TABLE IF EXISTS People")

# connection.commit()

# This command disconnects the database.
# connection.close()

""" 
You can use the 'with' statement to connect to you database.
using the 'with' statement also allows you to commit changes 
automatically without using 'commit()'

Keep in mind, however, that you will still need to commit() a change 
if you want to see the result of that change immediately 
(before closing the connection).
"""

""" 
The executescript() method allows you to run more than 1 line of SQL at a
time. BUT you do have to separate by semicolons.
"""

with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	# c.executescript(""" DROP TABLE IF EXISTS People;
	# 				CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT);
	# 				INSERT INTO People VALUES('Ron', 'Obvious', '42');
	# 				 """)



""" 
We can use the executemany() method, just supply a tuple of tuples
where each inner tuple supplies the information for a single command
"""

peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)