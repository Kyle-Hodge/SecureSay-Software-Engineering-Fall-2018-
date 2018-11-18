import sqlite3


def add_name(user, pw):
	try:
		query = "INSERT INTO users (username, password) VALUES (?, ?);"

		connection = sqlite3.connect('DatabaseFile.db')
		cursor = connection.cursor()
		if(user == "" or pw == ""):
			return False
		cursor.execute(query, (user, pw))
		cursor.close()
		connection.commit()
		connection.close()

		return True
	except Exception as e:
		print("Error: " + str(e))
		return False

def get_name(user, pw):
	query = "SELECT username,password FROM users WHERE username=? AND password=?;"
	connection = sqlite3.connect('DatabaseFile.db')
	cursor = connection.cursor()
	cursor.execute(query, [user, pw])
	if(user == "" or pw == ""):
		return False
	results = cursor.fetchall()
	cursor.close()
	connection.close()

	return results

def print_name():
	query = "SELECT username FROM users;"
	connection = sqlite3.connect('DatabaseFile.db')
	cursor = connection.cursor()
	cursor.execute(query)
	results = cursor.fetchall()
	cursor.close()
	connection.close()

	return results

def check_table(sender, receiver):
	try:
		query = "SELECT username FROM " + sender + receiver + ";"
		connection = sqlite3.connect('DatabaseFile.db')
		cursor = connection.cursor()
		cursor.execute(query)
		cursor.close()
		connection.commit()
		connection.close()

		return True
	except Exception as e:
		return False

def get_table(sender, receiver):
	try:
		query = "CREATE TABLE " + sender + receiver + " ( id integer primary key autoincrement, username char(12) NOT NULL, message char(50) NOT NULL);"
		connection = sqlite3.connect('DatabaseFile.db')
		cursor = connection.cursor()
		cursor.execute(query)
		cursor.close()
		connection.commit()
		connection.close()

		return True
	except:
		return False

def store_message(sender, receiver, user, message):
	try:
		query = "INSERT INTO " + sender + receiver + " (username, message) VALUES (?, ?);"
		connection = sqlite3.connect('DatabaseFile.db')
		cursor = connection.cursor()
		cursor.execute(query, (user, message))
		cursor.close()
		connection.commit()
		connection.close()

		return True
	except Exception as e:
		return False

def get_store_message(sender, receiver):
	query = "SELECT username,message FROM " + sender + receiver + " WHERE id > 0;"
	connection = sqlite3.connect('DatabaseFile.db')
	cursor = connection.cursor()
	cursor.execute(query)
	results = cursor.fetchall()
	cursor.close()
	connection.close()

	return results


#Insert a new name

# add_name('ahsia', '123')
# add_name('xzhou', '123')

#Check it exists
#print("Username for ahsia: ", get_name('example.db', 'ahsia'))