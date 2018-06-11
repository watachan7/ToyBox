from tkinter import *
from PIL import Image
import os
os.chdir("C://Users//RGBK0025-1//Desktop//作業フォルダ//Gits//wltln_repo//ToyBox//Python_works//tkinter_code")

#----------------------------------------------------------------------


def filenameMaker(num):
    return "%03d.png" % num


class MainWindow():

    #----------------

    def __init__(self, main):
        # 画像を表示するキャンバスを作る
        self.canvas = Canvas(main, width=200, height=200)
        self.canvas.grid(row=0, column=0, columnspan=2, rowspan=4)

        # 画像(000.pngから004.pngの5枚)を取り込む
        self.my_images = []
        self.file_num = 0
        for i in range(0, 5):
            self.my_images.append(PhotoImage(file=filenameMaker(i)))
        self.my_image_number = 0

        # 保存用の番号を確保
        self.save_file_num = 0

        # 最初の画像をセット
        self.image_on_canvas = self.canvas.create_image(
            0, 0, anchor=NW, image=self.my_images[self.my_image_number])

        # 各種ボタンを作る
        # 次の画像を表示するボタン
        self.button_next = Button(
            main, text="Next", command=self.onNextButton, width=20, height=5)
        self.button_next.grid(row=2, column=4, columnspan=2, rowspan=2)
        # 前の画像を表示するボタン
        self.button_back = Button(
            main, text="Back", command=self.onBackButton, width=20)
        self.button_back.grid(row=4, column=4, columnspan=2)
        # 選択領域を保存するボタン
        self.button_save = Button(
            main, text="Save", command=self.onSaveButton, width=25, height=5)
        self.button_save.grid(row=2, column=6, columnspan=3, rowspan=2)
        # 保存用番号を一つ戻るボタン
        self.button_saveb = Button(
            main, text="Save Back", command=self.onSavebButton, width=25)
        self.button_saveb.grid(row=4, column=6, columnspan=3)

        # メッセージを表示するEntryを作る
        # 現在の画像番号を表示するEntry
        self.message_num = Entry(width=50)
        self.message_num.insert(
            END, ("This image is " + filenameMaker(self.my_image_number)))
        self.message_num.grid(row=6, column=4, columnspan=5)
        # 次の保存番号を表示するEntry
        self.message = Entry(width=50)
        self.message.insert(END, ("Next save-name is " +
                                  "save-" + filenameMaker(self.save_file_num)))
        self.message.grid(row=7, column=4, columnspan=5)

        # スライダ用の変数を確保
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0

        # 画像切り出し用のラインをキャンバスに描画
        self.canvas.create_line(self.left, 0, self.left,
                                200, tag="left_line", fill='green')
        self.canvas.create_line(self.right, 0, self.right,
                                200, tag="right_line", fill='red')
        self.canvas.create_line(
            0, self.top, 200, self.top, tag="top_line", fill='green')
        self.canvas.create_line(0, self.bottom, 200,
                                self.bottom, tag="bottom_line", fill='red')

        # 画像切り出し用のスライダを作る
        self.left = Scale(main, label='left', orient='h',
                          from_=0, to=200, length=200, command=self.onSliderLeft)
        self.left.grid(row=4, column=0, columnspan=2, rowspan=2)

        self.right = Scale(main, label='right', orient='h',
                           from_=0, to=200, length=200, command=self.onSliderRight)
        self.right.grid(row=6, column=0, columnspan=2, rowspan=2)

        self.top = Scale(main, label='top', orient='v',
                         from_=0, to=200, length=200, command=self.onSliderTop)
        self.top.grid(row=4, column=2, rowspan=4)

        self.bottom = Scale(main, label='bottom', orient='v',
                            from_=0, to=200, length=200, command=self.onSliderBottom)
        self.bottom.grid(row=4, column=3, rowspan=4)

        # 画像切り出し用のラインを表示している画像に合わせて移動
        self.left.set(0)
        self.right.set(self.my_images[self.my_image_number].width())
        self.top.set(0)
        self.bottom.set(self.my_images[self.my_image_number].height())

    #----------------

    def onBackButton(self):
        # 最後の画像に戻る
        if self.my_image_number == 0:
            self.my_image_number = len(self.my_images) - 1
        else:
            # 一つ戻る
            self.my_image_number -= 1

        # 表示画像を更新
        self.canvas.itemconfig(self.image_on_canvas,
                               image=self.my_images[self.my_image_number])

        # 表示画像にあわせて画像切り出し用のラインの位置を更新
        self.left.set(0)
        self.right.set(self.my_images[self.my_image_number].width())
        self.top.set(0)
        self.bottom.set(self.my_images[self.my_image_number].height())


        # Entryの中身を更新
        self.message_num.delete(0, END)
        self.message_num.insert(
            END, ("This image is " + filenameMaker(self.my_image_number)))

    def onNextButton(self):
        # 一つ進む
        self.my_image_number += 1

        # 最初の画像に戻る
        if self.my_image_number == len(self.my_images):
            self.my_image_number = 0

        # 表示画像を更新
        self.canvas.itemconfig(self.image_on_canvas,
                               image=self.my_images[self.my_image_number])

        # 表示画像にあわせて画像切り出し用のラインの位置を更新
        self.left.set(0)
        self.right.set(self.my_images[self.my_image_number].width())
        self.top.set(0)
        self.bottom.set(self.my_images[self.my_image_number].height())

        # Entryの中身を更新
        self.message_num.delete(0, END)
        self.message_num.insert(
            END, ("This image is " + filenameMaker(self.my_image_number)))

    def onSaveButton(self):
        # 表示画像を取り込み
        self.temp_image = Image.open(filenameMaker(self.my_image_number))
        # 選択位置で切り出し
        self.cropped_image = self.temp_image.crop(
            (self.left.get(), self.top.get(), self.right.get(), self.bottom.get()))
        # 保存
        self.cropped_image.save("save-" + filenameMaker(self.save_file_num))

        self.save_file_num += 1

        # Entryの中身を更新
        self.message.delete(0, END)
        self.message.insert(END, ("Next save-name is " +
                                  "save-" + filenameMaker(self.save_file_num)))

    def onSavebButton(self):
        self.save_file_num -= 1

        if self.save_file_num == -1:
            self.save_file_num = 0

        # Entryの中身を更新
        self.message.delete(0, END)
        self.message.insert(END, ("Next save-name is " +
                                  "save-" + filenameMaker(self.save_file_num)))

    def onSliderLeft(self, args):
        # change line
        self.canvas.delete("left_line")
        self.canvas.create_line(
            self.left.get(), 0, self.left.get(), 200, tag="left_line", fill='green')

    def onSliderRight(self, args):
        # change line
        self.canvas.delete("right_line")
        self.canvas.create_line(
            self.right.get(), 0, self.right.get(), 200, tag="right_line", fill='red')

    def onSliderTop(self, args):
        # change line
        self.canvas.delete("top_line")
        self.canvas.create_line(0, self.top.get(), 200,
                                self.top.get(), tag="top_line", fill='green')

    def onSliderBottom(self, args):
        # change line
        self.canvas.delete("bottom_line")
        self.canvas.create_line(0, self.bottom.get(), 200,
                                self.bottom.get(), tag="bottom_line", fill='red')


#----------------------------------------------------------------------

root = Tk()
MainWindow(root)
root.mainloop()