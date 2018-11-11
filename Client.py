# Used with ServerPlus.py
""" This file will   - send info of Username/Password to ServerPlus.py, and see if info in DB (ServerPlus.py will do this)
                     - Use synchronous messaging by using Thread
                     - As well as Asynchronous messaging - if a User is offline and comes back Online, retreive HISTORY from DB (ServerPlus.py will do this)
"""
from socket import *
from tkinter import *
from tkinter import scrolledtext
from threading import Thread

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
    pwd_entry = Entry(window, show="*", width = 10)
    pwd_entry.grid(column = 1, row = 1)

    # checks if the credentials are correct
    def login_press():
        entered_username = user_entry.get()
        entered_password = pwd_entry.get()
        res = ""

        get_bool = False

        # When user input is not empty, send username/password to server
        if entered_username and entered_password != "":
            get_bool = True
            # send username and password to server
            clientSocket.send(entered_username.encode())
            clientSocket.send(entered_password.encode())
        # else when one input is empty, Try Again
        else:
            print("Enter more info in username/password")
            res = "Fill in a username and password"
            get_bool = False
            result_label.configure(text = res)

        # Enter if statement when sent username/password to server
        if get_bool is True:
            # Receive a message from Server that either says "Correct_Information" or "bad"
            correct_statement = clientSocket.recv(1024)

            # Enter if statement when message from server equals to 'Correct_Information'
            if correct_statement.decode() == "Correct_Information": # Username & Password is confirmed in Database
                res = "Successful login!"
                result_label.configure(text = res)
                window.destroy() # exits the login window
                chat_window() # Display chat GUI
            # ELSE, Username/Password is incorrect - Try Again
            else:
                print("Incorrect username/password")
                res = "Invalid credentials. Please try again."
                result_label.configure(text = res)
        

    btn = Button(window, text = "Login", command = login_press)
    btn.grid(column = 2, row = 1)
    window.mainloop()


# Chat GUI
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
    # make the log box disabled to not allow user input
    chat_log_box.configure(state = DISABLED)

    chat_input_label = Label(window, text = "Chat Input")
    chat_input_label.grid(column = 0, row = 2)
    chat_input_box = Entry(window, width = 50)
    chat_input_box.grid(column = 0, row = 3)

    def send():
        # get user input
        msg = chat_input_box.get()

        # reset input box to empty string
        chat_input_box.delete(0, END)
        
        if msg != "" and msg != "{quit}":
            # send user input to server
            clientSocket.send(msg.encode())
            # Make chat_log_box enabled to input text
            chat_log_box.configure(state = NORMAL)
            # Make scrollbar auto scroll to most recent message
            chat_log_box.see(END)
            # Make chat_log_box disabled to prohibit user input
            chat_log_box.configure(state = DISABLED)

        # typing {quit} in chat input will exit the client
        if msg == "{quit}":
            clientSocket.send("<has went offline>".encode())
            clientSocket.close()
            window.destroy()

    btn_send = Button(window, text = "send", command = send)
    btn_send.grid(column = 1, row = 3)

    # Receive method that will receive message from server and input into chat log
    def receive():
        while True:
            try:
                # Receive message from server
                msg = clientSocket.recv(1024)
                # Make chat_log_box enabled to input text
                chat_log_box.configure(state = NORMAL)
                # insert message that was sent from another User into chat log
                chat_log_box.insert(END, msg.decode() + "\n")
                # Make scrollbar auto scroll to most recent message
                chat_log_box.see(END)
                # Make chat_log_box disabled to prohibit user input
                chat_log_box.configure(state = DISABLED)
            except:
                print("Client exited")
                break

    # Start thread for SYNCHRONOUS messaging between one another
    receive_thread = Thread(target = receive)
    receive_thread.start()

    window.mainloop()
    clientSocket.close()

serverName = 'localhost'
serverPort = 12000

# # establish client socket as TCP on IPv4 network
clientSocket = socket(AF_INET, SOCK_STREAM)

# # initial TCP connection to server
clientSocket.connect((serverName, serverPort))

# display login GUI
login_window()

clientSocket.close()