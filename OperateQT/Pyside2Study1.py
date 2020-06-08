#  @Function:  PySide2学习demon
#　＠Time:2020/5/23 22:17
#  @Author:Flank

import sys, os
from PySide2.QtWidgets import *

# 添加插件路径到操作系统变量中
plugin_path = '/home/lmx/anaconda3/lib/python3.6/site-packages/PySide2/plugins/platforms'
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

app = QApplication()  # 实例化一个应用程序对象
window=QWidget()
window.resize(200,120)


# 定义一个Button
btnQuit = QPushButton("Quit",window)
# 设置矩形框的大小
btnQuit.setGeometry(10, 40, 180, 40)
# 连接到app的quit槽函数，即退出
btnQuit.clicked.connect(app.quit())

# 实例化一个标签对象
label = QLabel('Hello,World',window)

window.show()
app.exec_()


