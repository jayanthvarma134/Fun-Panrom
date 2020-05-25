from tkinter import *
root = Tk()

e= Entry(root)
e.pack()
def myClick():
	mylabel = Label(root, text='hello'+ e.get())
	mylabel.pack()

myButton = Button(root, text='Click here', command=myClick)
myButton.pack()

root.mainloop()

