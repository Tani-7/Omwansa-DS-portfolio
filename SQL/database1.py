import sqlite3

#Query the DB and return all records 

def show_all():
	#connecting to database
	connection = sqlite3.connect('customer.db')

	#creating  the cursor
	c = connection.cursor()
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()
	for item in items:
		print(item)

	#committing any changes
	connection.commit()
	#closing the connection

	connection.close()

#Adding a new record to the Table
def add_one(first, last,email):
	connection = sqlite3.connect('customer.db')
	c = connection.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

	connection.commit()
	connection.close()

def add_many(list):
	connection = sqlite3.connect('customer.db')
	c = connection.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

	connection.commit()
	connection.close()

#using WHERE fuction
def email_lookup(email):
	connection = sqlite3.connect('customer.db')
	c = connection.cursor()
	c.execute("SELECT * from customers WHERE email = (?)", (email,))

	items = c.fetchall()

	for item in items:
		print(item)


	connection.commit()
	connection.close()


#to delete a record 
def delete_one(id):
	connection = sqlite3.connect('customer.db')
	c = connection.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)", id)

	connection.commit()
	connection.close()
