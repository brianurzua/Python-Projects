"""
For this assignment, you will write a script that creates a GUI with a button widget and a text widget. 
We recommend using the GUI from the previous assignment, though this is not required. Your script will 
also include a function that, when it is called, will invoke a dialog modal which will allow users the 
ability to select a folder directory from their system. Finally, your script will show the user’s 
selected directory path in the text field.

1. Your script will need to use the askdirectory( ) method from the Tkinter module.

2. Your script will need to have a function linked to the button widget so that once the button has been 
clicked, the user’s selected file path will be retained by the askdirectory( ) method and printed 
within your GUI’s text widget.

"""
import tkinter
from tkinter import *

class ParentWindow(Frame):
	def __init__ (self, master):
		Frame.__init__ (self)

		self.master = master
		self.master.resizable(width=False, height=False)
		self.master.geometry('{}x{}'.format(500,200))
		self.master.title('Check Files')
		self.master.config(bg = 'gray87')

		self.varFileName = StringVar()

		# Label for file name and just adding blank space for columnspan method
		self.lblFileName = Label(self.master, text='File Name: ', font=('Helvetica', 14), fg='black', bg = 'gray87')
		self.lblFileName.grid(row=1, column=0, padx=(15,0), pady=(30,0))

		# Text box for file name 
		self.txtFileName = Entry(self.master, text=self.varFileName, font=('Helvetica', 14), fg='black', bg='white', width=30)
		self.txtFileName.grid(row=1, column=1, columnspan=2, padx=(5), pady=(32,0), sticky=NW)

		# Buttons for checking and exiting program
		self.btnCheck = Button(self.master, text='Check for File...', width=12, height=2, command=self.check_File)
		self.btnCheck.grid(row=2, column=0, padx=(16,0), pady=(30), sticky=SW)

		self.btnClose = Button(self.master, text='Close Program', width=12, height=2, command=self.closeProg)
		self.btnClose.grid(row=2, column=2, padx=(250), pady=(30), sticky=SE)

		self.lblDisplay = Label(self.master, text='', font=('Helvetica', 12), fg='black', bg='gray87')
		self.lblDisplay.grid(row=3, column=1, padx=(0), pady=(0))

			# Function for Check file button
	def check_File(self):
		fn = self.varFileName.get()
		self.lblDisplay.config(text='Searching for {} ...'.format(fn))


	# Function for closing program	
	def closeProg(self):
		self.master.destroy()



if __name__ == '__main__':
	root = Tk()
	App = ParentWindow(root)
	root.mainloop()