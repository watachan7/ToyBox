from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Button Example')

s = StringVar()

# Frame as Widget Container
frame1 = ttk.Frame(
    root,
    padding=5)
frame1.grid()

# Button 1
def dvd_clicked():
    button1.state(['pressed'])
    button2.state(['!pressed'])
    s.set("DVD clicked.")

icon1 = PhotoImage(file='pen.png')

button1 = ttk.Button(
    frame1,
    image=icon1,
    text='DVD',
    compound=TOP,
    command=dvd_clicked)
button1.grid(row=1,column=1)

# Button 2
def download_clicked():
    button1.state(['!pressed'])
    button2.state(['pressed'])
    s.set("Download clicked.")

icon2 = PhotoImage(file='pen.png')

button2 = ttk.Button(
    frame1,
    image=icon2,
    text='Download',
    compound=TOP,
    command=download_clicked)
button2.grid(row=1,column=2)

# Label 1
label1 = ttk.Label(
    frame1,
    textvariable=s)
label1.grid(row=2,column=1,columnspan=2)

root.mainloop()