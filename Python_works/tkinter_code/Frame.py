from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Frame Test')

frame1 = ttk.Frame(
    root,
    height=200,
    width=300,
    relief='sunken',
    borderwidth=5)
frame1.grid()

# frame1 = ttk.Frame(root)
# frame1['height'] = 200
# frame1['width'] = 300
# frame1['relief'] = 'sunken'
# frame1['borderwidth'] = 5
# frame1.grid()

root.mainloop()