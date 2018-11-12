from socket import *
from random import *

serverPort = 12000

# establish server socket as TCP on IPv4 network
server_socket = socket(AF_INET, SOCK_STREAM)

# binds socket to current host IP with given server port
server_socket.bind(('', serverPort))

# sets server to maintain two TCP connections
server_socket.listen(1)

print("The server is ready to receive")

chat_client_socket, addr = server_socket.accept() 
print("Chat Client connection established")


while True:
    # receives a message from chat client
    message = chat_client_socket.recv(1024)
    print("Username: " + message.decode())
    chat_client_socket.send("Username received.".encode())

    message = chat_client_socket.recv(1024)
    print("Password: " + message.decode())
    chat_client_socket.send("Password received.".encode())
    break


# closes all socket connections
chat_client_socket.close()
server_socket.close()