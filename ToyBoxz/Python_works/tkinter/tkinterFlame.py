from tkinter import *
from tkinter import ttk
 
 
class CalcApp(ttk.Frame):
    """アプリ(予定)."""
 
    def init(self, master=None):
        super().init(master)
 
 
def main():
    root = Tk()
    root.title('testFrame')
    CalcApp(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()
