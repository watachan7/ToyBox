from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Label Example')

# Frame as Widget Container
frame1 = ttk.Frame(root)
frame1.grid()

# Label 1
icon = PhotoImage(file='pen.png')

label1 = ttk.Label(
    frame1,
    image=icon,
    text='Earth',
    compound='top')
label1.grid(row=1,column=1)

root.mainloop()