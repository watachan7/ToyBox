from tkinter import *
from tkinter import ttk

pbval = 0

def button_click():
    global pbval
    pbval = pbval + 1
    pb.configure(value=pbval)
    
def button2_click():
    pb2.stop()
    
if __name__ == '__main__':
    
    root = Tk()
    root.title('Progress')
    root.columnconfigure(0, weight=1);
    root.rowconfigure(0, weight=1);
    
    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(sticky=(N,W,S,E))
    frame1.columnconfigure(0, weight=1);
    frame1.rowconfigure(0, weight=1);
    
    # プログレスバー (確定的)
    pb = ttk.Progressbar(
        frame1, 
        orient=HORIZONTAL, 
        length=200, 
        mode='determinate')
    pb.configure(maximum=10, value=pbval)
    pb.grid(row=0, column=0, sticky=(N,E,S,W))

    # 進捗ボタン
    button1 = ttk.Button(frame1, text='OK', command=button_click)
    button1.grid(row=0, column=1, padx=5, sticky=(E))
    
    # プログレスバー (不確定的)
    pb2 = ttk.Progressbar(
        frame1, 
        orient=HORIZONTAL, 
        length=200, 
        mode='indeterminate')
    pb2.configure(maximum=10, value=0)
    pb2.grid(row=1, column=0, sticky=(N,E,S,W))
    pb2.start(100)

    # 停止ボタン
    button2 = ttk.Button(frame1, text='Stop', command=button2_click)
    button2.grid(row=1,column=1,padx=5,sticky=(E))
    
    root.mainloop()