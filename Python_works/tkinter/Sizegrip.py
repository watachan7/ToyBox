from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    root = Tk()
    root.title('Resize Sizegrip')
    root.minsize(300, 200)
    root.columnconfigure(0, weight=1);
    root.rowconfigure(0, weight=1);

    # サイズグリップ
    sizegrip = ttk.Sizegrip(root)
    sizegrip.grid(row=1, column=0, sticky=(S,E))
    
    # フレーム
    s = ttk.Style()
    s.configure('MyFrame.TFrame', background='white')
    # Creating a ttk.Frame
    frame1 = ttk.Frame(root, padding=10, style='MyFrame.TFrame')
    frame1.grid(row=0, column=0, sticky=(N,W,S,E))
    frame1.columnconfigure(0, weight=1);
    frame1.rowconfigure(0, weight=1);
    
    # ボタン
    button1 = ttk.Button(frame1, text='OK', command=quit)
    button1.grid(row=0, column=0, sticky=(S,E))
    
    root.mainloop()