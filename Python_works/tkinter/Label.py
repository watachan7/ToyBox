from tkinter import *
from tkinter import ttk

root = Tk()
frame1 = ttk.Frame(root)
frame1.grid()

label1 = ttk.Label(
    frame1,
    text='Hello',
    background='#0000aa',
    foreground='#ffffff',
    padding=(5,10))
label1.grid(row=1,column=1)

label2 = ttk.Label(
    frame1,
    text='World',
    background='#ffffff',
    width=20,
    anchor=E,
    padding=(5,10))
label2.grid(row=1,column=2)

root.mainloop()

