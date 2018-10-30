from socket import *
from tkinter import *

def login_window():
    # create the main login window
    window = Tk()
    window.title("Sender Login Screen")
    window.geometry("800x800")

    # creates all the labels on the window
    user_label = Label(window, text = "Username: ")
    user_label.grid(column = 0, row = 0)
    pwd_label = Label(window, text = "Password: ")
    pwd_label.grid(column = 0, row = 1)
    status_label = Label(window, text = "Status: ")
    status_label.grid(column = 0, row = 2)
    result_label = Label(window, text = "Enter credentials")
    result_label.grid(column = 1, row = 2)

    # creates the username and password entry boxes
    user_entry = Entry(window, width = 10)
    user_entry.grid(column = 1, row = 0)
    pwd_entry = Entry(window, width = 10)
    pwd_entry.grid(column = 1, row = 1)

    # checks if the credentials are correct
    def clicked():
        entered_username = user_entry.get()
        entered_password = pwd_entry.get()
        res = ""

        if entered_username != "test" or entered_password != "12345":
            res = "Invalid credentials."
            result_label.configure(text = res)
        else:
            res = "Successful login!"
            window.quit() # exits the login window
            return
        result_label.configure(text = res)

    # creates the button to analyze the input
    btn = Button(window, text = "Login", command = clicked)
    btn.grid(column = 2, row = 1)

    window.mainloop()

serverName = 'localhost'
serverPort = 12000

# establish client socket as TCP on IPv4 network
clientSocket = socket(AF_INET, SOCK_STREAM)

# initial TCP connection to server
clientSocket.connect((serverName, serverPort))

# display login GUI
login_window()

# User input
messageSend = input("Type in Message: ")

if messageSend is not None: # if message is not null
    # message must be encoded first before being sent into the socket
    clientSocket.send(messageSend.encode())

# closes the socket connection
clientSocket.close()
