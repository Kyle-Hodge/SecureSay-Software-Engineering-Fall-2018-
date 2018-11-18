#A server that can contain multiple clients

from socket import *
from random import *
from _thread import *
import DatabasePlus

# Method to determine Login from Database
def confirm_user_DB(connection, addr):
    while True:
        try:
            # Receive a message from Client that either says "Logging_In" (which means Login method) or "Creating_Account" (which means Create Account method)
            log_or_create = connection.recv(1024).decode()
            print (log_or_create)

            # Client is logging in
            if log_or_create == "Logging_In":
                print("Logging in...")
                while log_or_create == "Logging_In":
                    # Receive username & password from client
                    username = connection.recv(1024)
                    password = connection.recv(1024)

                    print ("Received username: " + username.decode())
                    print ("Received password: " + password.decode())

                    # If True send a message that says "Correct_Information" to the client
                    if DatabasePlus.get_name(username.decode(), password.decode()):
                        print("Correct Info of User/PW")
                        connection.send("Correct_Information".encode())
                        # Set their unique id as their username
                        unique_id[username.decode()] = []
                        # add their connection as well (in a dictionary format)
                        unique_id.update({username.decode(): connection})
                        print(unique_id)
                        return sendUsernames(connection, addr, username.decode()) # go to sendUsernames() method that will help build the selection of Users

                    # ELSE, send a message to client that does NOT say "Correct_Information"
                    else:
                        print("Credentials does not match in DB")
                        connection.send("Try_Again".encode())
            # Client is creating an account
            elif log_or_create == "Creating_Account": 

                while log_or_create == "Creating_Account":
                    # Receive username & password from client
                    username = connection.recv(1024).decode()
                    password = connection.recv(1024).decode()

                    # Add to DB if successful send message to client that says "Added_Account_In_DB"
                    if DatabasePlus.add_name(username, password):
                        print("ADDED account in DB")
                        connection.send("Added_Account_In_DB".encode())
                        return confirm_user_DB(connection, addr) # Call method again to get log_or_create to contain message: Logging_In ;and go into that IF Statement
                    #ELSE, Try Again
                    else:
                        print("Cannot add account in DB")
                        connection.send("Try_Again".encode())
        except:
            break
            connection.close()

# This method will build the selection of Users that is currently in the DB. Note that ALL Users will be printed so client can message themselves as well
def sendUsernames(connection, addr, username):
    try:
        # send all names that is in the DB to client
        for x in DatabasePlus.print_name():
            message = x[0] + ","
            connection.send(message.encode())

        # Client has selected their User to start communication or wait here till they select their User
        gotUsername = connection.recv(1024).decode()
        print("GOT USERNAME: " + gotUsername)
        if gotUsername != "": # make sure it's not empty string
            # check if a table in the DB is established or not. NOTE to avoid clutter in the DB, I made the table names as their combined usernames.
                # so we must check two instances. For example: there are two users - User1 and User2. Lets say User1 started their communication so the table in DB will be User1User2.
                # For User2, we don't want to create another table called User2User1, so we must check the table backwards or 'two instances' for User1User2 table. 
            if DatabasePlus.check_table(username, gotUsername) == True or DatabasePlus.check_table(gotUsername, username) == True:
                print ("TABLE IS THERE AND READY")
                clients(connection, addr, username, gotUsername) # go to the clients() method to start the messaging between the Users
            #ELSE, create the table in DB
            else: 
                print ("TABLE IS NOT THERE BUT IS GOING TO BE ESTABLISHED")
                DatabasePlus.get_table(username, gotUsername)
                print ("Table Established in DB")

    except Exception as e:
        print(e)
        connection.close()


def clients(connection, addr, username, gotUsername):
    # check if table is in DB (Should be there already from previous method but we need to see which order the Usernames of the table are in)
    if DatabasePlus.check_table(gotUsername, username) == True or DatabasePlus.check_table(username, gotUsername) == True:
        # Check two instances since there are two ways there can be a table - First instance: 
        if DatabasePlus.check_table(gotUsername, username) == True: 
            # Go through the TUPLE list of the (username, message) from the DB and send those messages to the chat logs box.
            for x in DatabasePlus.get_store_message(gotUsername, username):
                message = "<" + x[0] + ">: " + x[1] + "\n"
                connection.send(message.encode()) # send to client

        # Second instance:
        elif DatabasePlus.check_table(username, gotUsername) == True:
            # Go through the TUPLE list of the (username, message) from the DB and send those messages to the chat logs box.
            for x in DatabasePlus.get_store_message(username, gotUsername):
                message = "<" + x[0] + ">: " + x[1] + "\n"
                connection.send(message.encode()) # send to client

    
    # Once the LOGS are done, enter while loop for the messages that the Client (Sender) will send
    while True:
        try:
            # Receive message from Client
            message = connection.recv(1024)
            if (message.decode() != ""):
                print ("Server received Message from " + username)

                # Store the message that the Client (Sender) sent along with the username if it's not the message <has went offline>
                # There is also two instances of a table in DB to save their messages:
                if message.decode() != "<has went offline>" and DatabasePlus.check_table(gotUsername, username) == True:
                    DatabasePlus.store_message(gotUsername, username, username, message.decode())
                elif message.decode() != "<has went offline>" and DatabasePlus.check_table(username, gotUsername) == True:
                    DatabasePlus.store_message(username, gotUsername, username, message.decode())

                # Send message for SYNCHRONOUS messaging in chat room
                send_oneclient(message.decode(),connection, addr, username, gotUsername)
        except:
            break
            connection.close()

def send_oneclient(message, connection, addr, username, gotUsername): 
    # create a new dictionary - to only hold the connection of who is communicating to one another
    new_dictionary = {}
    new_dictionary.clear() # clear dictionary again just in case

    # go through the list of clients and only obtain the clients who are talking to each other that are connected.
    # To confirm that we get the same corresponding client with connection together
    for client, value in unique_id.items():
        # One client to obtain
        if client == gotUsername: 
            new_dictionary.update({client: value}) # update the nenw dictionary with the client's dictionary values. Ex: 'ahsia': <socket>
        # Another client to obtain
        elif client == username:
            new_dictionary.update({client: value}) # update (add) to new dictionary
        elif client == gotUsername and client == username:
            new_dictionary.update({client: value})

    # Send messages
    # First for loop is for the usernames of the clients
    for clients in new_dictionary:
        # Second for loop is for the connection of the clients
        for value in new_dictionary.values():
            # send message to the other client instead of the one who sent the message
            if clients == gotUsername and value!=connection and clients != username: 
                try: 
                    print ("TO:" + clients)
                    # The message that the Server will send to Client (Receiver)
                    send_message = "<" + username + ">: " + message
                    # Send message to Client (Receivers)
                    value.send(send_message.encode()) 
                    print ("Server sent message from: " + username)
                    break
                except: 
                    value.close()

            # send message to the one who sent the message
            elif clients == username and value == connection and clients != gotUsername:
                try:
                    print("FROM: " + clients)
                    send_message = "<You>: " + message
                    value.send(send_message.encode()) # send message to client
                    break
                except:
                    value.close()
            elif clients == username and clients == gotUsername and value == connection: # messaging yourself
                try:
                    print("Messaging Yourself" + clients)
                    send_message = "<self_message>: " + message
                    value.send(send_message.encode()) # send message to client
                except Exception as e:
                    print (e)
    print(new_dictionary)
    new_dictionary.clear() # clear dictionary to make other clients have their own dictionary
    print(new_dictionary)

serverPort = 12000

# establish server socket as TCP on IPv4 network
server_socket = socket(AF_INET, SOCK_STREAM)

# binds socket to current host IP with given server port
server_socket.bind(('', serverPort))

# sets server to maintain 100 TCP connections
server_socket.listen(100)

# store Unique ID (username) alongside the connection in a dictionary format; example: 'ahsia': <socket connection>
    # this will help two-way communication between one user and another to identify their unique ID instead of a connection
unique_id = {}

print ("Server start. .")


while True:
    # Client joins server
    connection, addr = server_socket.accept()
  
    # Prints the address of the user that just connected on Server side
    print (addr[0] + " connected")

    # Starts a thread for each connection that connects to server, starts with the confirm_user_DB method to confirm Login credentials
    start_new_thread(confirm_user_DB,(connection,addr))  



# Closes all socket connections
connection.close()
server_socket.close()