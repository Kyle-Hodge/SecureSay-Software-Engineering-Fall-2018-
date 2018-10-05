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

packets = 0
while packets < 10:
    # receives sender message and responses with acknowledgement
    # execution pauses here until something is received from the server
    # (Router.py line 35)
    message, serverAddress = clientSocket.recvfrom(1024)

    # modifies message
    response = 'Acknowledged: ' + str(packets)

    # sends the modified message back to the server
    clientSocket.send(response.encode())
    packets += 1
    
# closes the socket connection
clientSocket.close()