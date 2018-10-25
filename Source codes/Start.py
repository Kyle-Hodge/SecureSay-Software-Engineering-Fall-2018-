from Tkinter import *
import os

#When User clicks on login button, go to userLogin
def nextPage():
	window.destroy()
	os.system('python userLogin.py')

#Create the components
def login(window):


	#SecureSay text
	txtSS = Label(window, text="SecureSay", font=("Helvetica", 24), fg="blue")
	txtSS.grid(column=1, row=1)

	#Login button
	btnLog = Button(window, text="Login", command = lambda: loginUser(window, btnLog, txtSS))
	btnLog.place(relx = 0.5, rely = 0.5, anchor = CENTER) #Center the button

	#configure grid layout
	window.grid_rowconfigure(0, weight=0)
	window.grid_columnconfigure(0, weight=1)
	window.grid_rowconfigure(2, weight=1)
	window.grid_columnconfigure(2, weight=1)
	

#Log in interface
def loginUser(window, btnLog, txtSS):
	print "Logging in.."
	window.title("Provide credentials to Log in")
	#remove previous placed components
	txtSS.grid_forget() #remove label
	btnLog.place_forget() #remove button
	
	#Username
	lblU = Label(window, text="Username:")
	lblU.grid(column=1, row=1)
	txtU = Entry(window,width=10)
	txtU.grid(column=2, row=1)
	#Password
	lblP = Label(window, text="Password:")
	lblP.grid(column=1, row=2)
	txtP = Entry(window,width=10)
	txtP.grid(column=2, row=2)

	#configure grid layout
	window.grid_rowconfigure(0, weight=0)
	window.grid_columnconfigure(0, weight=1)
	window.grid_rowconfigure(3, weight=1)
	window.grid_columnconfigure(3, weight=1)

	#Submit button
	btnDone = Button(window, text="Done", command = lambda: nextPage())
	btnDone.grid(column=2, row=3)


window = Tk() #Initialize window
window.title("Start SecureSay")
window.geometry("500x200")



login(window)
window.mainloop() 