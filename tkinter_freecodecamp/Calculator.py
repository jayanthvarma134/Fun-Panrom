from tkinter import *


root = Tk()
root.title('Boring_Calculator_App')

e= Entry(root,width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady= 10)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, current + str(number))
	
def operation(op):
	global first_num
	first_num = int(e.get())
	global math

	if op == '+':
		math = 'add'
	elif op == '-':
		math = 'sub'
	elif op == '*':
		math = 'mul'
	elif op == '/':
		math = 'div'

	e.delete(0, END)


def equal():
	global second_num
	second_num = int(e.get())
	e.delete(0, END)
	if math == 'add':
		e.insert(0, first_num + second_num)
	elif math == 'sub':
		e.insert(0, first_num - second_num)
	elif math == 'mul':
		e.insert(0, first_num * second_num)
	elif math == 'div':
		e.insert(0, first_num / second_num)


def clear():
	e.delete(0, END)


#defining buttons
button_1 = Button(root, text='1', padx=20, pady=10, borderwidth=3, command=lambda:button_click(1))
button_2 = Button(root, text='2', padx=20, pady=10, borderwidth=3, command=lambda:button_click(2))
button_3 = Button(root, text='3', padx=20, pady=10, borderwidth=3, command=lambda:button_click(3))
button_4 = Button(root, text='4', padx=20, pady=10, borderwidth=3, command=lambda:button_click(4))
button_5 = Button(root, text='5', padx=20, pady=10, borderwidth=3, command=lambda:button_click(5))
button_6 = Button(root, text='6', padx=20, pady=10, borderwidth=3, command=lambda:button_click(6))
button_7 = Button(root, text='7', padx=20, pady=10, borderwidth=3, command=lambda:button_click(7))
button_8 = Button(root, text='8', padx=20, pady=10, borderwidth=3, command=lambda:button_click(8))
button_9 = Button(root, text='9', padx=20, pady=10, borderwidth=3, command=lambda:button_click(9))
button_0 = Button(root, text='0', padx=20, pady=10, borderwidth=3, command=lambda:button_click(0))
button_add = Button(root, text='+', padx=19, pady=10, borderwidth=3, fg= 'blue', command=lambda:operation('+'))
button_sub = Button(root, text='-', padx=20, pady=10, borderwidth=3,fg='blue', command=lambda:operation('-'))
button_mul = Button(root, text='*', padx=20, pady=10, borderwidth=3,fg='blue', command=lambda:operation('*'))
button_div = Button(root, text='/', padx=20, pady=10, borderwidth=3,fg='blue', command=lambda:operation('/'))
button_equal = Button(root, text='=', padx=19, pady=10, borderwidth=3,fg='green', command=equal)
button_clear = Button(root, text='clr', padx=17, pady=10, borderwidth=3,fg='red', command=clear)

#packing buttons as a grid on the output screen 
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)

button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_mul.grid(row=3, column=4)
button_div.grid(row=4, column=4)


root.mainloop()