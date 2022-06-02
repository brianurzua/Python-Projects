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

		# Buttons for the GUI
		self.btnSubmit = Button(self.master, text='Browse...', width=12, height=1)
		self.btnSubmit.grid(row=3, column=1, padx=(10,0), pady=(50,0), sticky=NW)

		self.btnSubmit = Button(self.master, text='Browse...', width=12, height=1)
		self.btnSubmit.grid(row=4, column=1, padx=(10,0), pady=(15,0), sticky=W)

		self.btnSubmit = Button(self.master, text='Check for Files...', width=12, height=2)
		self.btnSubmit.grid(row=5, column=1, padx=(10,0), pady=(15,15), sticky=SW)

		self.btnSubmit = Button(self.master, text='Close Program', width=12, height=2)
		self.btnSubmit.grid(row=5, column=2, padx=(290), pady=(15,15), sticky=SE)

		# Text box for the GUI
		self.txtFname = Entry(self.master, text=self.varFileName, font=('Helvetica', 16), fg='black', bg='white', width=30)
		self.txtFname.grid(row=3, column=2, columnspan=2, padx=(20,0), pady=(50,0), sticky=NW)

		self.txtFname = Entry(self.master, text=self.varFileName, font=('Helvetica', 16), fg='black', bg='white', width=30	)
		self.txtFname.grid(row=4, column=2, columnspan=2, padx=(20,0), pady=(15,0), sticky=NW)



if __name__ == '__main__':
	root = Tk()
	App = ParentWindow(root)
	root.mainloop()