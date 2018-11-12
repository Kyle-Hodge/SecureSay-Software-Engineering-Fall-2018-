#A server that can contain multiple clients

from socket import *
from random import *
from _thread import *
import DatabasePlus

# Method to determine Login from Database
def confirm_user_DB(connection, addr):
    while True:
        try:
            # Receive username & password from client
            username = connection.recv(1024)
            password = connection.recv(1024)

            print ("Received username: " + username.decode())
            print ("Received password: " + password.decode())

            # If True send a message that says "Correct_Information" to the client
            if DatabasePlus.get_name(username.decode(), password.decode()):
                print("Correct Info of User/PW")
                connection.send("Correct_Information".encode())
                # include username.decode() as a parameter to save the username
                return clients(connection, addr, username.decode()) # Exit the confirm_user_DB method and go to clients() method for the start of messages
            # ELSE, send a message to client that does NOT say "Correct_Information"
            else:
                print("Credentials does not match in DB")
                connection.send("Try_Again".encode())
        except:
            break
            connection.close()

def clients(connection, addr, username):
    # When a client successfully logs in, they would be brought to the messaging GUI - try and receive the HISTORY first and place it in the chat logs box.
    # If get_table from DB is false, it means that there is already a table that exists in DB
    if DatabasePlus.get_table() == False:
        # Go through the TUPLE list of the (username, message) from the DB and send those messages to the chat logs box.
        for x in DatabasePlus.get_store_message():
            message = "<" + x[0] + ">: " + x[1] + "\n"
            connection.send(message.encode())
    # ELSE, create table in DB
    else:
        DatabasePlus.get_table()
        print("Created table in DB")

    # Once the LOGS are done, enter while loop for the messages that the Client (Sender) will send
    while True:
        try:
            # Receive message from Client
            message = connection.recv(1024)
            if (message.decode() != ""):
                print ("Server received Message from " + username)

                # Store the message that the Client (Sender) sent along with the username if it's not the message <has went offline>
                if message.decode() != "<has went offline>":
                    DatabasePlus.store_message(username, message.decode())
                # Send message for SYNCHRONOUS messaging in chat room
                sendAll(message.decode(),connection, addr, username)
        except:
            break

def sendAll(message, connection, addr, username): 
    # go through the list of clients
    for clients in list_of_clients: 
        # send message to other clients instead of the one who sent the message
        if clients!=connection: 
            try: 
                # The message that the Server will send to Client (Receiver)
                send_message = "<" + username + ">: " + message
                # Send message to Client (Receivers)
                clients.send(send_message.encode()) 
                print ("Server sent message from: " + username)
            except: 
                clients.close()
        # send message to the one who sent the message
        else:
            try:
                send_message = "<You>: " + message
                clients.send(send_message.encode())
            except:
                clients.close()

serverPort = 12000

# establish server socket as TCP on IPv4 network
server_socket = socket(AF_INET, SOCK_STREAM)

# binds socket to current host IP with given server port
server_socket.bind(('', serverPort))

# sets server to maintain 100 TCP connections
server_socket.listen(100)

# store Clients here
list_of_clients = []

print ("Server start. .")


while True:
    # Client joins server
    connection, addr = server_socket.accept()
    # Put connection in list
    list_of_clients.append(connection)
  
    # Prints the address of the user that just connected on Server side
    print (addr[0] + " connected")

    # Starts a thread for each connection that connects to server, starts with the confirm_user_DB method to confirm Login credentials
    start_new_thread(confirm_user_DB,(connection,addr))  



# Closes all socket connections
connection.close()
server_socket.close()
