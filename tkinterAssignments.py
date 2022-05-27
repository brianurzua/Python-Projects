# This is a tkinter learning module


from tkinter import *


# NEVER USE PACK AND GRID IN THE SAME MASTER WINDOW, IT
# WILL GIVE YOU ERRORS!!!!!!!!!!!!!!

win = Tk()
f = Frame(win)

b1 = Button(f, text = "One")
b2 = Button(f, text = "Two")
b3 = Button(f, text = "Three")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)



""" With pack() you tell your widget to pack itself on parent.
	you can also specifically tell it where you want it 
	(TOP, LEFT, RIGHT, BOTTOM)
	You can also tell it the padding
"""
# b1.pack(side=LEFT, padx = 10)
# b2.pack(side=LEFT, padx = 10)

"""Since the parent window is divided into rows and columns,
	you can use gid() to tell it what row and column you want
	it in. 
"""
# b1.grid(row=0, column=0)
# b2.grid(row=1, column=1)


""" 
You can use the label widget to add a label
when you have empty space.
"""
l = Label(win, text="This label is over all buttons")
# l.grid(row=1, column=0)

l.pack()
f.pack()


""" 
Use the configure() method to pass functions into 
a button.
"""

b1.configure(text="Uno")

def but1():
	print("Button one was pushed")

b1.configure(command=but1) # This assigns function to button