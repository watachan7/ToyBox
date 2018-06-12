from tkinter import *
from tkinter import ttk

def button1_clicked():
    print('v1 = %s' % v1.get())
    quit()

def rb_clicked():
    print('v1 = %s' % v1.get())

root = Tk()
root.title('Radiobutton 1')

# Frame
frame1 = ttk.Frame(root,padding=10)
frame1.grid()

# Label Frame
lf = ttk.Labelframe(
    frame1, 
    text='Options',
    padding=5)
lf.grid(row=0,column=0,pady=5)

#Radiobutton 1
v1 = StringVar()
rb1 = ttk.Radiobutton(
    lf,
    text='Option 1',
    value='A',
    variable=v1,
    command=rb_clicked)
rb1.grid(row=0)

#Radiobutton 2
rb2 = ttk.Radiobutton(
    lf,
    text='Option 2',
    value='B',
    variable=v1,
    command=rb_clicked)
rb2.grid(row=1)

#Button
button1 = ttk.Button(
    frame1, 
    text='OK', 
    padding=5,
    command=button1_clicked)

#Layout
button1.grid(row=1)

root.mainloop()