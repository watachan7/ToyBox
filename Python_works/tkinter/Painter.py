import tkinter as tk

class Scribble:

    def callback():
        print("called the callback!")

    # ボタンが押された
    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = self.width.get())

    # ドラッグ
    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                                fill = self.color.get(),
                                width = self.width.get())
        self.sx = event.x
        self.sy = event.y

    # ウィンドウを作る
    def create_window(self):
        window = tk.Tk()
        window.title('Painterz')

        # 画面サイズ設定
        self.canvas = tk.Canvas(window, bg = "white", width = 600, height = 300)
        self.canvas.pack()

        # create a menu
        menu = tk.Menu(window)
        window.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.callback)
        filemenu.add_command(label="Open...", command=self.callback)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.callback)

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.callback)

        #終了ボタン追加
        quit_button = tk.Button(window, text = "終了", command = window.quit)
        quit_button.pack(side = tk.RIGHT)

        # マウス動作
        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)

        # 色を選ぶ
        COLORS = ["red", "green", "blue", "#FF00FF", "black"]
        self.color = tk.StringVar()                    
        self.color.set(COLORS[1])                             
        b = tk.OptionMenu(window, self.color, *COLORS) 
        b.pack(side = tk.LEFT)

        # 線の太さを選ぶ
        self.width = tk.Scale(window, from_ = 1, to = 15, orient = tk.HORIZONTAL) 
        self.width.set(5)                                       
        self.width.pack(side = tk.LEFT)
        
        return window;
    
    def __init__(self):
        self.window = self.create_window();  # 呼び出すときはself. + メソッド名
            
    def run(self):
        self.window.mainloop()

# 開始   
Scribble().run()