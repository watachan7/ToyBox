from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button Example')

frame1 = ttk.Frame(
    root,
    padding=5)
frame1.grid()

button1 = ttk.Button(
    frame1,
    width=5,
    text='1')
button1.grid(row=1,column=1)

button2 = ttk.Button(
    frame1,
    width=5,
    text='2')
button2.state(['disabled'])
button2.grid(row=1,column=2)

root.mainloop()