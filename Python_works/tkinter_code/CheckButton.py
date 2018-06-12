from tkinter import *
from tkinter import ttk

def button1_clicked():
    print('v1 = %s' % v1.get())
    quit()

def cb1_clicked():
    print('v1 = %s' % v1.get())

root = Tk()
root.title('Checkbutton 1')

# Frame
frame1 = ttk.Frame(root, padding=(10,5))
frame1.grid()

#Checkbutton 1
v1 = StringVar()
cb1 = ttk.Checkbutton(
    frame1,
    padding=5,
    text='Option 1',
    onvalue='A',
    offvalue='B',
    variable=v1,
    command=cb1_clicked)

#Button
button1 = ttk.Button(
    frame1, 
    text='OK', 
    padding=5,
    command=button1_clicked)

#Layout
cb1.grid(row=0,column=0)
button1.grid(row=1, column=0)

root.mainloop()