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
		print("Error")
		return False

def get_name(user, pw):
	query = "SELECT username,password FROM users WHERE username=? AND password=?;"
	connection = sqlite3.connect('DatabaseFile.db')
	cursor = connection.cursor()
	cursor.execute(query, [user, pw])
	results = cursor.fetchall()
	cursor.close()
	connection.close()

	return results

def get_table():
	try:
		query = "CREATE TABLE messages (id integer primary key autoincrement, username char(12) NOT NULL, message char(50) NOT NULL);"
		connection = sqlite3.connect('DatabaseFile.db')
		cursor = connection.cursor()
		cursor.execute(query)
		cursor.close()
		connection.commit()
		connection.close()

		return True
	except:
		return False

def store_message(user, message):
	try:
		query = "INSERT INTO messages (username, message) VALUES (?, ?);"
		connection = sqlite3.connect('DatabaseFile.db')
		cursor = connection.cursor()
		cursor.execute(query, (user, message))
		cursor.close()
		connection.commit()
		connection.close()

		return True
	except Exception as e:
		return False

def get_store_message():
	query = "SELECT username,message FROM messages WHERE id > 0;"
	connection = sqlite3.connect('DatabaseFile.db')
	cursor = connection.cursor()
	cursor.execute(query)
	results = cursor.fetchall()
	cursor.close()
	connection.close()

	return results


#Insert a new name

#add_name('example.db', ('ahsia', '123'))

#Check it exists
#print("Username for ahsia: ", get_name('example.db', 'ahsia'))