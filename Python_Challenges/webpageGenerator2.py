"""
Now that you have created a tool that can automatically create a basic HTML web page, 
the content on the page is hard-coded as "Stay tuned for our amazing summer sale!"

Users have now asked you to create an option for them to set the body of the text themselves.

Your task is to create a GUI with Tkinter that will enable the users to set the body text for a newly-created web page. 
There should also be a control in the GUI that initiates the process of making the new web page.

Set a new body text of your choice.

The GUI should open the html file in a new tab within your browser that displays the newly added text from the user.
"""

import tkinter
from tkinter import *
import webbrowser as wb

class ParentWindow(Frame):
	def __init__ (self, master):
		Frame.__init__ (self)

		self.master = master
		self.master.resizable(width=False, height=False)
		self.master.geometry('{}x{}'.format(500,200))
		self.master.title('Update Website Body')
		self.master.config(bg = 'gray87')

		self.varInput = StringVar()

		# Label for the body
		self.lblFileName = Label(self.master, text='Body: ', font=('Helvetica', 14), fg='black', bg = 'gray87')
		self.lblFileName.grid(row=0, column=0, padx=(30,0), pady=(30), sticky=W)

		# input text box
		self.txtBody = Entry(self.master, text=self.varInput, font=('Helvetica', 14), fg='black', bg='white', width=33)
		self.txtBody.grid(row=0, column=1, padx=(0,30), sticky=W)

		#Buttons for 
		self.btnChange = Button(self.master, text='Change', width=10, height=2, command=self.submit)
		self.btnChange.grid(row=1, column=0, columnspan=1, padx=15)
		
		self.btnClose = Button(self.master, text='Close', width=10, height=2, command=self.closeProg)
		self.btnClose.grid(row=1, column=1, sticky=NS, padx=(0,15))


	# func that changes the body of text and launches it
	def submit(self):
		usertxt = self.txtBody.get()
		html = "<html> <body>" +usertxt +"</html> </body>"
		f = open('amazing.html', 'w')
		f.write(html)
		f.close()
		wb.open('amazing.html')	

	def closeProg(self):
		self.master.destroy()


if __name__ == '__main__':
	root = Tk()
	App = ParentWindow(root)
	root.mainloop()

