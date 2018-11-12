from socket import *
from tkinter import *
import DatabasePlus
from tkinter import scrolledtext

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
    def login_press():
        entered_username = user_entry.get()
        entered_password = pwd_entry.get()
        res = ""

        #sends username and password to server
        clientSocket.send(entered_username.encode())
        clientSocket.send(entered_password.encode())

        # this conditional will need to be changed to fetch account credentials from database
        """
        if DatabasePlus.get_name(entered_username, entered_password):
            res = "Successful login!"
            window.destroy() # exits the login window
            return
        else:
            res = "Invalid credentials. Please try again."
            result_label.configure(text = res)
        result_label.configure(text = res)
"""
    # creates the button to analyze the input
    btn = Button(window, text = "Login", command = login_press)
    btn.grid(column = 2, row = 1)
    window.mainloop()


def chat_window():
    # create the main chat window
    window = Tk()
    window.title("Chat Application Screen")
    window.geometry("800x800")



    # creates all the labels on the window
    chat_log_box_label = Label(window, text = "Chat History")
    chat_log_box_label.grid(column = 0, row = 0)
    chat_log_box = scrolledtext.ScrolledText(window, width = 40, height = 10)
    chat_log_box.grid(column = 0, row = 1)
    window.mainloop()

serverName = 'localhost'
serverPort = 12000

# # establish client socket as TCP on IPv4 network
clientSocket = socket(AF_INET, SOCK_STREAM)

# # initial TCP connection to server
clientSocket.connect((serverName, serverPort))

# display login GUI
login_window()

# display chat GUI
# chat_window()

# # User input
# messageSend = input("Type in Message: ")

# if messageSend is not None: # if message is not null
#     # message must be encoded first before being sent into the socket
#     clientSocket.send(messageSend.encode())

# # closes the socket connection
clientSocket.close()
