import tkinter 
 
window = tkinter.Tk() 
 
tkinter.Button(window, text = "ボタン").pack() 
tkinter.Checkbutton(window, text = "チェックボタン").pack() 
 
entry = tkinter.Entry(window) 
entry.insert(tkinter.END, "エントリ") 
entry.pack() 
 
frame = tkinter.LabelFrame(window, text = "ラベル付きフレーム") 
frame.pack() 
tkinter.Label(frame, text = "ラベル").pack() 
 
listbox = tkinter.Listbox(window, height = 3) 
listbox.insert(tkinter.END, "リストボックス") 
listbox.insert(tkinter.END, "項目2") 
listbox.pack() 
 
tkinter.Scale(window, orient = tkinter.HORIZONTAL).pack() 
tkinter.Spinbox(window).pack() 
 
window.mainloop()