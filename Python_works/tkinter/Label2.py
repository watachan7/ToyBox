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
    image=icon)
label1.grid(row=1,column=1)

# String
s = StringVar()
s.set('Going Back To School')

# Label 2
label2 = ttk.Label(
    frame1,
    textvariable=s,
    width=30,
    anchor=W,
    padding=(5,10))
label2.grid(row=1,column=2)

root.mainloop()