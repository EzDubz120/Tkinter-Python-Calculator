import cmath
import math
from tkinter import *

window = Tk()
window.title("Calculator")

e = Entry(window, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	#math
	
	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))
	
	if math == "squared":
		e.insert(0, f_num * f_num)

	if math == "cubed":
		e.insert(0, f_num * f_num * f_num)

	if math == "to_the_power_of":
		e.insert(0, f_num ** int(second_number))

	if math == "square_root":
		e.insert(0, f_num ** 0.5)

def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

def button_squared():
	first_number = e.get()
	global f_num
	global math
	math = "squared"
	f_num = int(first_number)
	e.delete(0, END)

def button_cubed():
	first_number = e.get()
	global f_num
	global math
	math = "cubed"
	f_num = int(first_number)
	e.delete(0, END)

def button_to_the_power_of():
	first_number = e.get()
	global f_num
	global math
	math = "to_the_power_of"
	f_num = int(first_number)
	e.delete(0, END)

def button_pi():
	first_number = e.get()
	global f_num
	global math
	math = "pi"
	f_num = int(first_number)
	e.delete(0, END)

def button_square_root():
	first_number = e.get()
	global f_num
	global math
	math = "square_root"
	f_num = int(first_number)
	e.delete(0, END)

# Def buttons

button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(window, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(window, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(window, text="/", padx=41, pady=20, command=button_divide)

button_squared = Button(window, text="x²", padx=41, pady=20, command=button_squared)
button_cubed = Button(window, text="x³", padx=41, pady=20, command=button_cubed)
button_to_the_power_of = Button(window, text="x^", padx=41, pady=20, command=button_to_the_power_of)

button_pi = Button(window, text="𝝅", padx=41, pady=20, command=button_pi)

button_square_root = Button(window, text="2√", padx=41, pady=20, command=button_square_root)

 # put buttons on screen

button_1.grid(row=3, column=1)
button_2.grid(row=3, column=2)
button_3.grid(row=3, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=1, column=1)
button_8.grid(row=1, column=2)
button_9.grid(row=1, column=3)

button_0.grid(row=4, column=1)
button_clear.grid(row=6, column=2, columnspan=2)
button_add.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)

button_subtract.grid(row=6, column=1)
button_multiply.grid(row=7, column=1)
button_divide.grid(row=7, column=2)

button_squared.grid(row=4, column=2)
button_cubed.grid(row=4, column=3)
button_to_the_power_of.grid(row=7, column=3)

button_pi.grid(row=8, column=1)

button_square_root.grid(row=8, column=2)

window.mainloop()