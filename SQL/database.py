import sqlite3 

connection = sqlite3.connect('customer.db')

#creating cursor
c = connection.cursor()

#c.execute("""CREATE TABLE  customers(
#		first_name text,
#		last_name text,
#		email text
#
#	)""")

#available dtypes:
#NULL
#INTEGER
#REAL
#TEXT
#BLOB

#c.execute("INSERT INTO customers VALUES ('Jim', 'Proudfoot','Jim@proudfoot.com')")
#many_customers = [
#					('Lennox','Magara','lexohmonesir@gmail.com'),
#					('Origin','Onchwari','Onchwari@gmail.com'),
#					('Holyfield','Omwansa','holymoh@outlook.com'),
#					('Magara','Omwansa','linoks@outlook.com'),
#					('Andre','Rieu','rieu@andrerieu.com'),
#					('Andrea','Bocelli','Andrea@Bocelli.com'),
#					('Bertha','Benz','Bertha@daimlerag.com'),
#
#				] 
#print("Inserting values....")


#c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

#print("Inserted successfully...")

#querying database
#c.execute("SELECT * FROM customers WHERE email LIKE '%look.com'")
#c.fetchone()
#c.fetchmany(3)
#print(c.fetchall())


#UPDATING RECORDS

#c.execute("""UPDATE customers SET first_name = 'Robert'
#				WHERE last_name ='Proudfoot'
#				""")

#c.execute("""UPDATE customers SET first_name = 'Robert'
#				WHERE rowid = 4
#				""")

#DELETING RECORDS

#c.execute("DELETE from customers WHERE rowid = 5")

 

#ORDERING RESULTS

#c.execute("SELECT rowid, * FROM customers ORDER BY rowid")

#c.execute("SELECT * FROM customers ORDER BY last_name ")

# AND/OR OPERATORS

#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Dru%' OR rowid = 3")

#LIMITING RESULTS 
#c.execute("SELECT rowid, * FROM customers LIMIT 3")
#c.execute("SELECT rowid, * FROM customers ORDER BY last_name LIMIT 3") 

#DROPPING A TABLE 

#c.execute("DROP TABLE customers")

#commiting changes 
connection.commit()
#c.execute("SELECT rowid, * FROM customers") 

#items = c.fetchall()
#for item in items:
#	print(item[0] + " "+ item[1] + "\t" + item[2])

#items = c.fetchall()
##for item in items:
#	print(items)

#close the connection
connection.close()