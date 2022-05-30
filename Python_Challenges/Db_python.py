"""
Actions to complete:

1. Create a database table in RAM named Roster that includes the fields ‘Name’, ‘Species’ and ‘IQ.’

2. Populate your new table with the following values:
	1 Jean-Baptiste Zorg, Human, 122
	2 Korben Dallas, Meat Popsicle, 100
	3 Ak'not, Mangalore, -5

3. Update the Species of Korben Dallas to be Human.

4. Display the names and IQs of everyone in the table who is classified as Human.

"""

import sqlite3

# I am establishing a connection to my database. Using :memory: so it is stored in RAM
connection = sqlite3.connect(':memory:')

#  instantiate a cursor object that enables us to operate the database.
c = connection.cursor()

c.execute("DROP TABLE IF EXISTS Roster")
c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
c.execute("INSERT INTO Roster VALUES ('Jean-Baptiste Zorg', 'Human', '122')")
c.execute("INSERT INTO Roster VALUES ('Korben Dallas', 'Meat Popsicle', '100')")
c.execute("INSERT INTO Roster VALUES ('Ak''not', 'Manglore', '-5')")

c.execute("UPDATE Roster SET Species='Human' WHERE Species='Meat Popsicle'") # Update satemement, changes species from meat popsicle to human


print('IQ of humans:')
data = c.execute("SELECT Name, IQ FROM Roster WHERE Species='Human'")
for i in data: # iterates through data and prints information
	print(i)




