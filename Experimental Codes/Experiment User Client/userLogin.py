from Tkinter import *
from socket import *
from random import *

print "Logged in!"

serverName = 'localhost'
serverPort = 12000

# establish server socket as TCP on IPv4 network
server_socket = socket(AF_INET, SOCK_STREAM)

# binds socket to current host IP with given server port
server_socket.bind(('', serverPort))

# sets server to maintain two TCP connections
server_socket.listen(1)

print("The server is ready to receive")


def CreateMessage(window, btnCreateMessage):

	# establish client socket as TCP on IPv4 network
	clientSocket = socket(AF_INET, SOCK_STREAM)

	# initial TCP connection to server
	clientSocket.connect((serverName, serverPort))

	# execution of Router.py pauses here as well until a 2nd socket connects 
	sender_socket, addr1 = server_socket.accept()
	print("Sender connection established")

	#create message interface method
	developMessageInterface(window, btnCreateMessage)

def developMessageInterface(window, btnCreateMessage):
	window.title("Creating a Message")
	#remove previous components
	btnCreateMessage.place_forget()
	btnCreateMessage.grid_forget()

	#Message to
	lblU = Label(window, text="Message To:")
	lblU.grid(column=1, row=1)
	txtU = Entry(window,width=10)
	txtU.grid(column=2, row=1)

	#Message body
	lblP = Label(window, text="Message Body:")
	lblP.grid(column=1, row=2)
	txtP = Entry(window,width=10)
	txtP.grid(column=2, row=2)

	#configure grid layout
	window.grid_rowconfigure(0, weight=0)
	window.grid_columnconfigure(0, weight=1)
	window.grid_rowconfigure(3, weight=1)
	window.grid_columnconfigure(3, weight=1)

	#Submit button
	btnDone = Button(window, text="Done")
	btnDone.grid(column=2, row=3)


window = Tk()
window.title("Logged IN WELCOME")
window.geometry("500x100")

#create message button when user clicks goes to CreateMessage method
btnCreateMessage = Button(window, text="Create Message", command = lambda: CreateMessage(window, btnCreateMessage))
btnCreateMessage.grid(column=2, row=3)

window.mainloop()