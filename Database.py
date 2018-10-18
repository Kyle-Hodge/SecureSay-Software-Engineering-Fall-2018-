#MySQL database
import mysql.connector
from mysql.connector import errorcode


try:
	#connecting to the database
  connection = mysql.connector.connect(user='root', password='abcd',  host='127.0.0.1', database='example')

  	#errors
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Incorrect username or password.")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist.")
  else:
    print(err)


#interact with database
mycursor = connection.cursor()

print("\n Databases: ")
mycursor.execute("SHOW databases")

for database in mycursor:
  print(database)


print("\n Tables: ")
mycursor.execute("SHOW tables")

for table in mycursor:
  print(table)

print("\n Print table: ")
mycursor.execute("select * from lol")

for data in mycursor:
  print(data)


connection.close()