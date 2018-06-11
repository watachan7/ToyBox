from tkinter import *
from tkinter import ttk

def button_click():
    show_selection()
    
def show_selection():
    for i in lb.curselection():
        print(lb.get(i))

if __name__ == '__main__':
    root = Tk()
    root.title('Scrollbar 1')
    
    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    
    # Listbox
    currencies = ('JPY', 'USD', 'EUR', 'CNY', 'MXN', 'CAD')
    v1 = StringVar(value=currencies)
    lb = Listbox(frame1, listvariable=v1,height=3)
    lb.grid(row=0, column=0)
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1, 
        orient=VERTICAL, 
        # 縦方向にスクロール
        command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=0,column=1,sticky=(N,S))
    
    #Button
    button1 = ttk.Button(frame1, text='OK', command=button_click)
    button1.grid(row=1, column=0, columnspan=2)
    
    root.mainloop()