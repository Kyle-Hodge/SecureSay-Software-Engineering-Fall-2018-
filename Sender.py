from socket import *

serverName = 'localhost'
serverPort = 12000

# establish client socket as TCP on IPv4 network
clientSocket = socket(AF_INET, SOCK_STREAM)

# initial TCP connection to server
clientSocket.connect((serverName, serverPort))

packets = 0
while packets < 10:
    message = '0'

    # message must be encoded first before being sent into the socket
    clientSocket.send(message.encode())

    # execution pauses here until something is received from the server
    # (Server.py line 43)
    response, serverAddress = clientSocket.recvfrom(1024)

    # message response must be decoded before it can be printed
    print(response.decode())
    packets += 1

# closes the socket connection
clientSocket.close()