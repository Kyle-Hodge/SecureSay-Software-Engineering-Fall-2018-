from Tkinter import *

def login(window):
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
	btnDone = Button(window, text="Done")
	btnDone.grid(column=2, row=3)


window = Tk()
window.title("Login")
window.geometry("500x100")
login(window)
window.mainloop()