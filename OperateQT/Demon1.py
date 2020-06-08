#  @Function:  
# 　＠Time:2020/5/25 21:11
#  @Author:Flank
import os
from PySide2.QtWidgets import *


def handleCalc():
    info=testEdit.toPlainText()#获取文本框的输入
    QMessageBox.about(window,"输入值",info)

app = QApplication()

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle("薪资统计")

testEdit = QPlainTextEdit(window)
testEdit.setPlaceholderText("请输入薪资表")
testEdit.resize(300, 350)
testEdit.move(10, 25)

btn = QPushButton("统计", window)
btn.move(380, 80)
btn.clicked.connect(handleCalc)

window.show()

app.exec_()
