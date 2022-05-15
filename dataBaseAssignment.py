import sqlite3

# The connect method is assigned to var conn,
# this allows us to connect and create the db
conn = sqlite3.connect('files.db')

with conn:
	# the cur variable will let us operate within the db,
	# using the cursor command.
	cur = conn.cursor()

	# This creates 2 fields in the table
	cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
				col_fileName TEXT\
				)")

	conn.commit()

conn = sqlite3.connect('files.db')

# tuple of names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
			'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# A for loop to loop through each object in the fileList and 
# find the .txt files
for x in fileList:
	if x.endswith('.txt'):
		with conn:
			cur = conn.cursor()
			# The value for each row will be one name out of the file list (x,)
			# will denote a one element tuple for each file ending in .txt
			cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (x,))
			print(x)

conn.close()

