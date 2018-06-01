from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button Example')

# Frame as Widget Container
frame1 = ttk.Frame(
    root,
    padding=5)
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

# Button 1
def button1_clicked():
    root.quit()

button1 = ttk.Button(
    frame1,
    text='OK',
    command=button1_clicked)
button1.grid(row=2,column=1,columnspan=2)

root.mainloop()