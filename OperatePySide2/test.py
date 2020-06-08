#  @Function:  
#　＠Time:2020/5/25 下午5:25
#  @Author:Flank
import os
from PySide2 import QtWidgets
plugin_path = '/home/lmx/anaconda3/lib/python3.6/site-packages/PySide2/Qt/plugins/platforms'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
app = QtWidgets.QApplication()

window = QtWidgets.QWidget()
window.resize(200, 120)

btn_quit = QtWidgets.QPushButton("Quit", window)
# 设置矩形框的大小
btn_quit.setGeometry(10, 40, 180, 40)
# 连接到app的quit槽函数，即退出
btn_quit.clicked.connect(app.quit)

window.show()
app.exec_()