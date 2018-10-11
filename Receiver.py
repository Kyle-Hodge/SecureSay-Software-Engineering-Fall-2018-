# Receiver prints out the message from Sender

from socket import *

serverName = 'localhost'
serverPort = 12000

# establish client socket as TCP on IPv4 network
clientSocket = socket(AF_INET, SOCK_STREAM)

# initial TCP connection to server
# execution of Receiver.py pauses here until it connects to a server
# (Router.py line 19)
clientSocket.connect((serverName, serverPort))

print("Ready to receive.")
while True:
    # execution pauses here until message is received from the server
    # (Server.py line 34)
    response, serverAddress = clientSocket.recvfrom(1024)

    # message response must be decoded before it can be printed
    print("You got mail: " + "'" + response.decode() + "'")
    break;
    
# closes the socket connection
clientSocket.close()