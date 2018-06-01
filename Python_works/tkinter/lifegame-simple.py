from random import randint
from tkinter import *

# 変数・定数の定義 --- (*1)
COLS, ROWS = [30, 20] # ステージのサイズを定義
CW = 20 # セルの描画サイズ
data = [] # ステージデータ
for y in range(0, ROWS): # ステージをランダムに初期化
    data.append([(randint(0, 9) == 0) for x in range(0, COLS)])

# ライフゲームのルールを実装したもの --- (*2)
def check(x, y):
    # 周囲の生存セルを数える
    cnt = 0
    tbl = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    for t in tbl:
        xx, yy = [x + t[0], y + t[1]]
        if 0 <= xx < COLS and 0 <= yy < ROWS:
            if data[yy][xx]: cnt += 1

        # ルールに沿って次世代の生死を決める
        if cnt == 3: return True # 誕生
        if data[y][x]:
            if 2 <= cnt <= 3: return True # 生存
            return False # 過疎 or 過密

    return data[y][x]

# データを次の世代に進める --- (*3)
def next_turn():
    global data
    data2 = []
    for y in range(0, ROWS):
        data2.append([check(x, y) for x in range(0, COLS)])
    data = data2 # データの内容を次の世代へ差し替え

# 画面を構築 --- (*4)
win = Tk() # ウィンドウを作成
cv = Canvas(win, width = 600, height = 400) # キャンバスを作成
cv.pack()

# ステージを描画 --- (*5)
def draw_stage():
    cv.delete('all') # 既存の描画内容を破棄
    for y in range(0, ROWS):
        for x in range(0, COLS):
            if not data[y][x]: continue
            x1, y1 = [x * CW, y * CW]
            cv.create_oval(x1, y1, x1 + CW, y1 + CW,
                fill="red", width=0) # 生きているセルを描画

# 300ミリ秒ごとに世代を進める --- (*6)
def game_loop():
    next_turn() # 世代を進める
    draw_stage() # ステージを描画
    win.after(300, game_loop) # 指定時間後に再度描画

game_loop() # ゲームループを実行
win.mainloop() # イベントループ