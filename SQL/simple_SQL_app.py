import database1

#adding records to db
#database1.add_one("Bruno","Fernandez","fernandez@manutd.com")

#To delete record rememnder to pass rowid as a str because py won't remember

#database1.delete_one('9')

#adding many records at once 

new_clients = [
	('Andrew','Nguyen','nguyen@stanford.edu'),
	('Lisa','Manning','useless@human.com')
	]

#database1.add_many(new_clients)

database1.email_lookup("nguyen@stanford.edu")


#show all records
database1.show_all()

