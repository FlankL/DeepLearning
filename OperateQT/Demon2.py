#  @Function:从QT Designer生成的ui文件中加载
# 　＠Time:2020/5/25 21:48
#  @Author:Flank
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
import os



def handleCalc():
    info = ui.testEdit.toPlainText()  # 获取文本框的输入
    QMessageBox.about(ui, "输入值", info)


os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

app = QApplication()
ui = QUiLoader().load('Calc.ui')
ui.btn.clicked.connect(handleCalc)

ui.show()
app.exec_()


