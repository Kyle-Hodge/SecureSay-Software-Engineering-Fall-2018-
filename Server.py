from socket import *
from random import *

serverPort = 12000

# establish server socket as TCP on IPv4 network
server_socket = socket(AF_INET, SOCK_STREAM)

# binds socket to current host IP with given server port
server_socket.bind(('', serverPort))

# sets server to maintain two TCP connections
server_socket.listen(2)

print("The server is ready to receive")

# execution of Router.py pauses here until a socket connects 
# (Receiver.py line 12) 
receiver_socket, addr1 = server_socket.accept() 
print("Receiver connection established")

# execution of Router.py pauses here as well until a 2nd socket connects 
# (Sender.py line 10)
sender_socket, addr2 = server_socket.accept()
print("Sender connection established")

while True:
    # receives a message from sender client
    # execution pauses here until something is received from the sender
    # (Sender.py line 17)
    message = sender_socket.recv(1024)

    # forwards message to the receiver
    receiver_socket.send(message)

    
    break;

# closes all socket connections
receiver_socket.close()
sender_socket.close()
server_socket.close()