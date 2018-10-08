from Tkinter import *
import os

#When User clicks on login button, go to userLogin
def nextPage():
	window.destroy()
	os.system('userLogin.py')

#Create the components
def login(window):
	#Login button
	btnLog = Button(window, text="Login", command = nextPage)
	btnLog.place(relx = 0.5, rely = 0.5, anchor = CENTER) #Center the button

	#SecureSay text
	txtSS = Label(window, text="SecureSay", font=("Helvetica", 24), fg="blue")
	txtSS.grid(column=1, row=1)

	#configure grid layout
	window.grid_rowconfigure(0, weight=0)
	window.grid_columnconfigure(0, weight=1)
	window.grid_rowconfigure(2, weight=1)
	window.grid_columnconfigure(2, weight=1)

window = Tk() #Initialize window
window.title("Start SecureSay")
window.geometry("500x200")
login(window)
window.mainloop() 