# Used with ServerPlus.py
""" This file will   - send info of Username/Password to ServerPlus.py, and see if info in DB (ServerPlus.py will do this)
                     - Use synchronous messaging by using Thread (Message pops up in both chats when both ONLINE)
                     - As well as Asynchronous messaging - if a User is offline and comes back Online, retreive HISTORY from DB (ServerPlus.py will do this)
                     
                     NEW 
                     - Added Create Account button (No back button so you must create an account in order to go to LOGIN GUI)
                     	- No back button for Login GUI as well
                     - Added a contacts GUI that will print out ALL users in DB (so client can also message themselves)
                     - This now ONLY supports two-way communication and does NOT support a 'chat room' style anymore.
"""
from socket import *
from tkinter import *
from tkinter import scrolledtext
from threading import Thread
import time
import datetime

def login_window():
    # create the main login window
    window = Tk()
    window.title("Login/Create Account Screen")
    window.geometry("800x800")
    window.configure(background = '#ECD875')

    # create account method
    def create_account():
	    btnLogin.grid_remove()
	    btnCreate.grid_remove()
	    window.title("Create Account Screen")
	    # Differentiate when user is creating account or logging in
	    clientSocket.send("Creating_Account".encode())

		# creates all the labels on the window
	    user_label = Label(window, text = "Enter a Username: ", bg = 'black', fg = 'white')
	    user_label.grid(column = 0, row = 0)
	    pwd_label = Label(window, text = "Enter a Password: ")
	    pwd_label.grid(column = 0, row = 1)
	    status_label = Label(window, text = "Status: ")
	    status_label.grid(column = 0, row = 2)
	    result_label = Label(window, text = "Create credentials")
	    result_label.grid(column = 1, row = 2)

	    # Display creation label when successfully created an account 
	    result_label_CREATION = Label(window, text = "", bg = "#ECD875")
	    result_label_CREATION.grid(column = 1, row = 4)

	    # creates the username and password entry boxes
	    user_entry = Entry(window, width = 10)
	    user_entry.grid(column = 1, row = 0)
	    pwd_entry = Entry(window, width = 10)
	    pwd_entry.grid(column = 1, row = 1)

	    # checks if username is available
	    def create_press():
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
	            # Receive a message from Server that either says "Added_Account_In_DB" or "Try_Again"
	            correct_statement = clientSocket.recv(1024)

	            # Enter if statement when message from server equals to 'Added_Account_In_DB'
	            if correct_statement.decode() == "Added_Account_In_DB": # Username & Password is created in Database
	                print("Created Account!")
	                res = "Successful Account Creation!"
	                result_label_CREATION.configure(text = res)
	                Login() # Goes to Login GUI when successfully created an account

	                # Remove components from the create_press GUI so there won't be any clutter in the next GUI
	                btn.grid_remove();
	                result_label.grid_remove()
	                status_label.grid_remove()
	                pwd_label.grid_remove()
	                user_label.grid_remove()

	            # ELSE, Username is taken - Try Again
	            else:
	                print("Cannot add account. Username Taken")
	                res = "Username Taken."
	                result_label.configure(text = res)

	    btn = Button(window, text = "Submit", command = create_press)
	    btn.grid(column = 3, row = 3)

	# Login method
    def Login():
	    btnLogin.grid_remove()
	    btnCreate.grid_remove()
	    window.title("Login Screen")
	    # Differentiate when user is creating account or logging in
	    clientSocket.send("Logging_In".encode())

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
	            # Receive a message from Server that either says "Correct_Information" or "Try_Again"
	            correct_statement = clientSocket.recv(1024)

	            # Enter if statement when message from server equals to 'Correct_Information'
	            if correct_statement.decode() == "Correct_Information": # Username & Password is confirmed in Database
	                res = "Successful login!"
	                result_label.configure(text = res)
	                window.destroy() # exits the login window
	                clients_window() # Display chat GUI
	            # ELSE, Username/Password is incorrect - Try Again
	            else:
	                print("Incorrect username/password")
	                res = "Invalid credentials. Please try again."
	                result_label.configure(text = res)
	        

	    btn = Button(window, text = "Submit", command = login_press)
	    btn.grid(column = 2, row = 3)

    btnLogin = Button(window, text = "Login", command = Login, bg = "blue", fg="white")
    btnLogin.grid(column = 2, row = 1)

    btnCreate = Button(window, text = "Create", command = create_account, bg = "blue", fg="white")
    btnCreate.grid(column = 2, row = 2)

    window.mainloop()

# list of clients to select to start messaging
def clients_window():
    window = Tk()
    window.title("Select User Screen")
    window.geometry("800x800")

    # Create a Tkinter variable
    tkvar = StringVar(window)
 	# Receive the list of Users
    choices = clientSocket.recv(1024).decode()

    # The list of users will be received as a ONE LONG STRING
    user_string = choices
    # Create a list
    user_list = []
    # split the string and put into list
    user_list = (user_string.split(','))

    # create a dropdown to select a User 
    dropdown = OptionMenu(window, tkvar, *user_list)

    Label(window, text="Select a User to start messaging").grid(row = 1, column = 1)
    dropdown.grid(row = 2, column =1)
 
    # displays the selected User in terminal
    def change_dropdown(*args):
        print( tkvar.get() )
 
    # See the selected User in terminal
    # 'w' means to 'write' from options - RWUA
    tkvar.trace('w', change_dropdown)

    # When User wants to message a certain somebody
    def clicked_message():
    	if tkvar.get() != "":
    		clientSocket.send(tkvar.get().encode())
    		print("Sent to Server!")
    		window.destroy()
    		chat_window()
    	else:
    		print("It is empty. Select a User from the dropdown")


    btn = Button(window, text = "message", command = clicked_message).grid(column = 2, row = 2)


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
            clientSocket.send((msg + " [" + datetime.datetime.now().strftime('%I:%M%p') + "]").encode())
            # Make chat_log_box enabled to input text
            chat_log_box.configure(state = NORMAL)
            # Make scrollbar auto scroll to most recent message
            chat_log_box.see(END)
            # Make chat_log_box disabled to prohibit user input
            chat_log_box.configure(state = DISABLED)

        # typing {quit} in chat input will exit the client
        if msg == "{quit}":
            clientSocket.send(("<has went offline>").encode())
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