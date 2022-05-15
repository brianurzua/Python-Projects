import sqlite3

conn = sqlite3.connect('test.db') 	# This will allow us to connect and
									# create db

with conn:
	cur = conn.cursor()  	# cursor method allows us to operate 
							# the db when commands are given
	cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
			ID INTEGER PRIMARY KEY AUTOINCREMENT,\
			col_fname TEXT, \
			col_lname TEXT, \
			col_email TEXT\
			)")

	conn.commit()


conn.close()

conn = sqlite3.connect('test.db')

with conn:
	cur = conn.cursor()
	cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)",\
				('Brian', 'Urzua', 'burzua@gmail.com'))
	cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)",\
				('Mikasa', 'Ackerman', 'mackerman@gmail.com'))
	cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)",\
				('Eren', 'Jaeger', 'ejaeger@hotmail.com'))

	conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

# with conn:
# 	cur = conn.cursor()
# 	cur.execute("SELECT col_fname, col_lname, col_email FROM \
# 				tbl_persons WHERE col_fname = 'Mikasa'")
# 	varPerson = cur.fetchall()
# 	for item in varPerson:
# 		msg = "First Name: {} \nLast Name: {} \nEmail: {}".format(item[0], item[1], item[2])
# 	print(msg)



