""" 1. Allow the user to browse and choose a specific folder that will contain the files to be checked daily.

	2. Allow the user to browse and choose a specific folder that will receive the copied files.

	3. Allow the user to manually initiate the 'file check' process that is performed by the script.

	4. Add comments throughout your Python explaining your code. """

import tkinter
from tkinter import *
from tkinter import filedialog
import ShutilAssignment2


class ParentWindow(Frame):
	def __init__ (self, master):
		Frame.__init__ (self)

		self.master = master
		self.master.resizable(width=False, height=False)
		self.master.geometry('{}x{}'.format(500,200))
		self.master.title('File Transfer')
		self.master.config(bg = 'gray87')

		# buttons for folder finding
		self.btnMoveFrom = Button(self.master, text='Move from', width=12, height=1, command=self.findDir)
		self.btnMoveFrom.grid(row=0, column=0, padx=(15,0), pady=(15,15), sticky=NW)

		self.btnMoveTo = Button(self.master, text='Move to', width=12, height=1, command=self.findDir2)
		self.btnMoveTo.grid(row=1, column=0, padx=(15,0), pady=(15,15), sticky=W)

		# Input boxes to find
		self.txtBrowse_1 = Entry(self.master, text=" ", font=('Helvetica', 12), fg='black', bg='white', width=38)
		self.txtBrowse_1.grid(row=0, column=1, columnspan=2, padx=(15,0), pady=(15,15), sticky=NW)

		self.txtBrowse_2 = Entry(self.master, text=" ", font=('Helvetica', 12), fg='black', bg='white', width=38)
		self.txtBrowse_2.grid(row=1, column=1, columnspan=2, padx=(15,0), pady=(15,15), sticky=NW)

		# Buttons for moving files and closing program
		self.btnMoveFile = Button(self.master, text='Move Files...', width=12, height=2)
		self.btnMoveFile.grid(row=2, column=0, padx=(15,0), pady=(15,15), sticky=SW)

		self.btnClose = Button(self.master, text='Close Program', width=12, height=2, command=self.closeProg)
		self.btnClose.grid(row=2, column=1, padx=(267), pady=(15,15), sticky=SE)

	def findDir(self):
	    userInp1 = self.txtBrowse_1.get()
	    directory = filedialog.askdirectory(initialdir="C:/Users/{}".format(userInp1))
	    self.txtBrowse_1.insert(0,directory)
	    return
	def findDir2(self):
	    userInp2 = self.txtBrowse_2.get()
	    directory = filedialog.askdirectory(initialdir="C:/Users/{}".format(userInp2))
	    self.txtBrowse_2.insert(0,directory)
	    return

	def closeProg(self):
		self.master.destroy()







if __name__ == '__main__':
	root = Tk()
	App = ParentWindow(root)
	root.mainloop()