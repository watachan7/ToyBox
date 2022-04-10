# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPalette, QPixmap

import sys
import os

app = QtWidgets.QApplication([])
ui_path = "uis"
dlg1 = uic.loadUi(f"{ui_path}/tops.ui")
dlg2 = uic.loadUi(f"{ui_path}/ui2.ui")

#----------------画面１------------------
# def changeView_1to2():
#     dlg1.hide()
#     dlg2.show()

def push_button_1():
    result = QMessageBox.question(None, "Study", "これまでの会話を学習しますか？", QMessageBox.Ok, QMessageBox.Cancel)
    if result == QMessageBox.Ok:
        talkline = dlg1.textEdit.toPlainText().split()
        print(talkline)

def push_button_2():
    result = QMessageBox.question(None, "exit", "アプリを終了しますか？", QMessageBox.Ok, QMessageBox.Cancel)
    if result == QMessageBox.Ok:
        sys.exit()

def push_button_3():
    question = dlg1.textEdit_2.toPlainText()
    dlg1.textEdit.append("user: " + question)
    result = ''
    dlg1.textEdit.append("ais: " + result)
    dlg1.textEdit_2.clear()

dlg1.pushButton_1.clicked.connect(push_button_1)
dlg1.pushButton_2.clicked.connect(push_button_2)
dlg1.pushButton_3.clicked.connect(push_button_3)

#----------------画面２------------------
def changeView_2to1():
    dlg2.hide()
    dlg1.show()

dlg2.pushButton.clicked.connect(changeView_2to1)

if __name__ == "__main__":
    dlg1.show()
    app.exec()