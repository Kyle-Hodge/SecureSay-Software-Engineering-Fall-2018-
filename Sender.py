from socket import *

serverName = 'localhost'
serverPort = 12000

# establish client socket as TCP on IPv4 network
clientSocket = socket(AF_INET, SOCK_STREAM)

# initial TCP connection to server
clientSocket.connect((serverName, serverPort))

# User input
messageSend = raw_input("Type in Message: ")

if messageSend is not None: # if message is not null
    # message must be encoded first before being sent into the socket
    clientSocket.send(messageSend.encode())

# closes the socket connection
clientSocket.close()